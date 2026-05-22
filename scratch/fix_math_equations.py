import os
import re
import sys
import unicodedata
from pathlib import Path

# Ensure UTF-8 stdout configuration for Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

vault_root = Path(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi")

# Lowercase and Uppercase Greek letters dictionary for LaTeX conversion
GREEK_LOWER = {
    'α': r'\alpha',
    'β': r'\beta',
    'γ': r'\gamma',
    'δ': r'\delta',
    'ε': r'\epsilon',
    'ζ': r'\zeta',
    'η': r'\eta',
    'θ': r'\theta',
    'ι': r'\iota',
    'κ': r'\kappa',
    'λ': r'\lambda',
    'μ': r'\mu',
    'ν': r'\nu',
    'ξ': r'\xi',
    'ο': 'o',
    'π': r'\pi',
    'ρ': r'\rho',
    'σ': r'\sigma',
    'ς': r'\sigma',
    'τ': r'\tau',
    'υ': r'\upsilon',
    'φ': r'\phi',
    'χ': r'\chi',
    'ψ': r'\psi',
    'ω': r'\omega',
    'ϑ': r'\theta',
}

GREEK_UPPER = {
    'Γ': r'\Gamma',
    'Δ': r'\Delta',
    'Θ': r'\Theta',
    'Λ': r'\Lambda',
    'Ξ': r'\Xi',
    'Π': r'\Pi',
    'Σ': r'\Sigma',
    'Υ': r'\Upsilon',
    'Φ': r'\Phi',
    'Ψ': r'\Psi',
    'Ω': r'\Omega',
}

PROSE_KEYWORDS = {
    # Accounting & business terms
    'stock', 'common', 'share', 'market', 'value', 'cash', 'worth', 'interest', 
    'pays', 'cost', 'accumulated', 'depreciation', 'sold', 'refund', 'adjustment', 
    'beginning', 'inventory', 'period', 'purchased', 'equity', 'par', 
    'bank', 'months', 'principal', 'property', 'plant', 'equipment', 'original', 
    'satisfactory', 'damaged', 'merchandise', 'receive', 'rate', 'firm', 'callable',
    'gave', 'shares', 'new', 'total', 'gives', 'pays', 'back', 'satisfactory',
    
    # Common English prose words (grammar, conjunctions, prepositions, etc.)
    'the', 'and', 'but', 'or', 'for', 'with', 'about', 'against', 'between',
    'into', 'through', 'during', 'before', 'after', 'above', 'below', 'from',
    'up', 'down', 'out', 'off', 'over', 'under', 'again', 'further', 'then',
    'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any',
    'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'nor',
    'only', 'own', 'same', 'than', 'too', 'very', 'can', 'will', 'just',
    'should', 'now', 'that', 'this', 'these', 'those', 'thus', 'therefore',
    'however', 'indeed', 'moreover', 'likewise', 'instead', 'meanwhile',
    'nevertheless', 'nonetheless', 'furthermore', 'otherwise', 'besides',
    'which', 'who', 'whom', 'whose', 'what', 'whatever', 'whoever', 'whichever',
    'either', 'neither', 'because', 'since', 'although', 'though', 'unless',
    'until', 'while', 'whereas', 'whether', 'as', 'if'
}

def normalize_math_chars(text):
    """Normalize high-plane mathematical alphanumeric Unicode symbols in U+1D400-U+1D7FF range."""
    result = []
    for char in text:
        code = ord(char)
        if 0x1D400 <= code <= 0x1D7FF:
            result.append(unicodedata.normalize('NFKC', char))
        else:
            result.append(char)
    return "".join(result)

def is_likely_math(text):
    """Check if the matched single-dollar block is actually math, to protect currency."""
    if '\\' in text:
        return True
    
    # If it contains standard prose keywords, it is not math
    words = re.findall(r'[a-zA-Z]+', text.lower())
    if any(w in PROSE_KEYWORDS for w in words):
        return False
        
    # If it is just numbers, spaces, and hyphens/dashes, it's a currency range or number
    if re.match(r'^[\d\s,.\-–—]+$', text):
        return False
        
    # If it has standard mathematical symbols, it is likely math
    if any(sym in text for sym in ['=', '+', '*', '/', '^', '_', '<', '>', '≈', '≤', '≥', '±', '÷']):
        return True
        
    # If it contains Greek letters, it is math
    if re.search(r'[\u0370-\u03ff\u1f00-\u1fff]', text):
        return True
        
    # If it is a single variable (e.g. "$x$"), it is math
    if len(text.strip()) == 1 and text.strip().isalpha():
        return True
        
    return False

def process_math_block(math_content):
    """Apply LaTeX transformations inside a matched math block (inline or block)."""
    # 1. Normalize high-plane mathematical alphanumeric characters
    math_content = normalize_math_chars(math_content)

    # 2. Map standard Greek characters to LaTeX commands
    for char, latex_cmd in GREEK_LOWER.items():
        # Replace only if not already preceded by a backslash
        math_content = re.sub(r'(?<!\\)' + re.escape(char), lambda m, cmd=latex_cmd: cmd, math_content)
    for char, latex_cmd in GREEK_UPPER.items():
        math_content = re.sub(r'(?<!\\)' + re.escape(char), lambda m, cmd=latex_cmd: cmd, math_content)

    # 3. Clean up typical spacing and exponents
    # Change parenthesized exponent (2), (t), (n), (k) to ^2, ^t, ^n, ^k
    math_content = re.sub(
        r'([a-zA-Zα-ωΑ-Ωϑ]|\\[a-zA-Z]+|\))\s*\(([2knt])\)',
        r'\1^\2',
        math_content
    )

    return math_content

def clean_equation_text(content):
    """Clean all font corruption distortions globally across the file."""
    # 1. First, normalize high-plane mathematical alphanumeric characters
    content = normalize_math_chars(content)

    # 2. Delimiter substitutions (triple-dollar, quadruple-dollar, quintuple-dollar)
    content = content.replace('$$$$$', '$$')
    content = content.replace('$$$$', '$$\n$$')
    content = content.replace('$$$', '$')

    # 3. Replace Malayalam summation symbol
    content = content.replace('෍', '\\sum')

    # 4. Replace Malayalam bar accents (ഥ, ത, ҧ) using extended variable range
    content = re.sub(r'[ഥതҧ]{2,}', ' ', content) # Clean up consecutive bar symbols
    
    # 4.1. Accents followed by a command (prevent matching \bar or \hat recursively)
    content = re.sub(r'[ഥതҧ]\s*\\(?!bar\b|hat\b)([a-zA-Z]+)', r'\\bar{\\\1}', content)
    
    # 4.2. Accents followed by a letter and another letter/number (e.g. തx1 -> \bar{x}_1)
    content = re.sub(r'[ഥതҧ]\s*([a-zA-Zα-ωΑ-Ωϑ])\s*([a-zA-Z0-9])', r'\\bar{\1}_{\2}', content)
    
    # 4.3. Accents followed by a single letter (e.g. ഥ𝒙 -> \bar{x})
    content = re.sub(r'[ഥതҧ]\s*([a-zA-Zα-ωΑ-Ωϑ])', r'\\bar{\1}', content)
    
    # 4.4. Letter followed by accent and subscript (e.g. xതi -> \bar{x}_i)
    content = re.sub(r'([a-zA-Zα-ωΑ-Ωϑ]|\\[a-zA-Z]+)\s*[ഥതҧ]\s*([a-zA-Z0-9])', r'\\bar{\1}_{\2}', content)
    
    # 4.5. Letter followed by accent (e.g. xത -> \bar{x})
    content = re.sub(r'([a-zA-Zα-ωΑ-Ωϑ]|\\[a-zA-Z]+)\s*[ഥതҧ]', r'\\bar{\1}', content)
    
    # 4.6. Parenthesized accent after letter (e.g. X(ത) -> \bar{X})
    content = re.sub(r'([a-zA-Zα-ωΑ-Ωϑ]|\\[a-zA-Z]+)\s*\([ഥതҧ]\)', r'\\bar{\1}', content)
    
    # 4.7. Standalone / leftover accents
    content = re.sub(r'(?<![a-zA-Z\\])[ഥതҧ](?![a-zA-Z])', r'\\bar{X}', content)

    # 5. Sinhala/Ethiopic hat/estimator accents (෡, ෠, ෢, ෨, መ, ෝ, ො)
    # First, handle consecutive accents or standalone brackets
    content = content.replace('෡ ෡', '\\hat{\\beta}_0, \\hat{\\beta}_1')
    content = content.replace('(መ)', '\\hat{\\beta}_0')
    content = re.sub(r'\(෡\)', r'\\hat{P}', content) # isolated (෡)
    
    # Custom replacement for specific scrambled regression lines in Lesson 22-24:
    content = content.replace(
        '෡ 1 \\bar{x}(2) β0 ~N β0, σε(2) n(+) (n−1)sx(2)',
        '$$\\hat{\\beta}_0 \\sim N\\left(\\beta_0, \\sigma_\\epsilon^2 \\left(\\frac{1}{n} + \\frac{\\bar{x}^2}{(n-1)s_x^2}\\right)\\right)$$'
    )
    content = content.replace(
        '෡ **This result cannot** \\hat{β}1 −β1 β1 − β1 = ~N 0,1 **be used because** \\hat{S}E β1 σ **is not known!** 1 ε(2) σ ε 2 (n−1)sx',
        '$$\\frac{\\hat{\\beta}_1 - \\beta_1}{SE(\\hat{\\beta}_1)} = \\frac{\\hat{\\beta}_1 - \\beta_1}{\\frac{\\sigma_\\epsilon}{\\sqrt{(n-1)s_x^2}}} \\sim N(0,1)$$ **This result cannot be used because $\\sigma_\\epsilon$ is not known!**'
    )

    # 6. Replace Chi-Squared distortions first before mapping other [ොෝ] to hats
    content = re.sub(r'[ොෝ]\s*χ\s*\(2\)', r'\\chi^2', content)
    content = re.sub(r'[ොෝ]\s*χ', r'\\chi^2', content)
    content = re.sub(r'[ොෝ]\s*\\chi\s*\(2\)', r'\\chi^2', content)
    content = re.sub(r'[ොෝ]\s*\\chi', r'\\chi^2', content)

    # 5.1. Accents followed by a command (prevent matching \bar or \hat recursively)
    content = re.sub(r'[෡෠෢෨መොෝ]\s*\\(?!bar\b|hat\b)([a-zA-Z]+)', r'\\hat{\\\1}', content)
    
    # 5.2. Accents followed by a letter and another letter/number (e.g. ොyg -> \hat{y}_g, ොy1 -> \hat{y}_1)
    content = re.sub(r'[෡෠෢෨መොෝ]\s*([a-zA-Zα-ωΑ-Ωϑ])\s*([a-zA-Z0-9])', r'\\hat{\1}_{\2}', content)
    
    # 5.3. Accents followed by a single letter
    content = re.sub(r'[෡෠෢෨መොෝ]\s*([a-zA-Zα-ωΑ-Ωϑ])', r'\\hat{\1}', content)
    
    # 5.4. Letter followed by accent and subscript (e.g. yෝi -> \hat{y}_i)
    content = re.sub(r'([a-zA-Zα-ωΑ-Ωϑ]|\\[a-zA-Z]+)\s*[෡෠෢෨መොෝ]\s*([a-zA-Z0-9])', r'\\hat{\1}_{\2}', content)
    
    # 5.5. Letter followed by accent (e.g. P෡ -> \hat{P})
    content = re.sub(r'([a-zA-Zα-ωΑ-Ωϑ]|\\[a-zA-Z]+)\s*[෡෠෢෨መොෝ]', r'\\hat{\1}', content)
    
    # 5.6. Parenthesized accent after letter (e.g. X(෡) -> \hat{X})
    content = re.sub(r'([a-zA-Zα-ωΑ-Ωϑ]|\\[a-zA-Z]+)\s*\([෡෠෢෨መොෝ]\)', r'\\hat{\1}', content)
    
    # 5.7. Standalone / leftover accents
    content = re.sub(r'(?<![a-zA-Z\\])[෡෠෢෨መොෝ](?![a-zA-Z])', r'\\hat{P}', content)

    # 7. Piecewise cases braces (ቊ -> \{, ቐ -> \{ or \}, ሼ -> \{)
    content = content.replace('ቊ', '\\{')
    content = content.replace('ቐ', '\\{')
    content = content.replace('ሼ', '\\{')

    # 8. Financial Markets specific distortions (ቀ, ቁ, ቑ)
    content = content.replace('~~(ቀ)~~', '+')
    content = content.replace('ቀ', '+')
    content = content.replace('ቁ', '/')
    content = content.replace('ቑ', '-') 

    # 9. Process content inside standard $ and $$ math delimiters to map Greek characters to LaTeX commands
    def math_block_replacer(match):
        return '$$' + process_math_block(match.group(1)) + '$$'

    def inline_math_replacer(match):
        inner_text = match.group(1)
        if is_likely_math(inner_text):
            return '$' + process_math_block(inner_text) + '$'
        else:
            return '$' + inner_text + '$'  # Leave currency unchanged

    # Process block math first
    content = re.sub(r'\$\$(.*?)\$\$', math_block_replacer, content, flags=re.DOTALL)
    # Process inline math (avoid double dollar conflicts by checking single dollar constraints)
    content = re.sub(r'\$(?!\$)([^\$\n]+)\$', inline_math_replacer, content)

    return content

def process_file(file_path, dry_run=False):
    """Read, clean, and write a markdown file if modified."""
    try:
        original_content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

    cleaned_content = clean_equation_text(original_content)

    if cleaned_content != original_content:
        if dry_run:
            print(f"[DRY-RUN] File would be modified: {file_path}")
            # Show a small diff or preview
            lines_orig = original_content.splitlines()
            lines_clean = cleaned_content.splitlines()
            for idx, (lo, lc) in enumerate(zip(lines_orig, lines_clean)):
                if lo != lc:
                    print(f"  Line {idx+1}:")
                    print(f"    - {lo[:120].strip()}")
                    print(f"    + {lc[:120].strip()}")
                    break
        else:
            file_path.write_text(cleaned_content, encoding='utf-8')
            print(f"Modified: {file_path}")
        return True
    return False

def main():
    dry_run = "--write" not in sys.argv
    print(f"Starting math equation sanitization (Dry Run: {dry_run})")
    
    modified_count = 0
    total_files = 0
    
    for root, dirs, files in os.walk(vault_root):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in ['.git', '.obsidian', '.aider.tags.cache.v4', '__pycache__', 'scratch']]
        for file in files:
            if not file.endswith('.md'):
                continue
            
            file_path = Path(root) / file
            total_files += 1
            
            if process_file(file_path, dry_run=dry_run):
                modified_count += 1
                
    print(f"\nProcessing complete!")
    print(f"Total markdown files scanned: {total_files}")
    print(f"Total files modified: {modified_count}")
    if dry_run and modified_count > 0:
        print("Run the script with --write flag to apply these changes in-place.")

if __name__ == "__main__":
    main()
