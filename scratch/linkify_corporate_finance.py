import re
from pathlib import Path

# Paths
ROOT = Path(__file__).resolve().parent.parent
FILE_PATH = ROOT / "Raw" / "Sources" / "30017 CORPORATE FINANCE" / "Slides_A_CF_26.md"

replacements = {
    # 1. Opportunity Cost of Capital (Cost-of-Capital)
    "opportunity cost of capital": "[[Wiki/Concepts/Cost-of-Capital|opportunity cost of capital]]",
    "Opportunity cost of capital": "[[Wiki/Concepts/Cost-of-Capital|Opportunity cost of capital]]",
    "Opportunity Cost of Capital": "[[Wiki/Concepts/Cost-of-Capital|Opportunity Cost of Capital]]",
    
    # 2. Net Present Value (Net-Present-Value)
    "Net Present Value": "[[Wiki/Concepts/Net-Present-Value|Net Present Value]]",
    "net present value": "[[Wiki/Concepts/Net-Present-Value|net present value]]",
    "Net present value": "[[Wiki/Concepts/Net-Present-Value|Net present value]]",
    
    # 3. Internal Rate of Return (Internal-Rate-of-Return)
    "Internal Rate of Return": "[[Wiki/Concepts/Internal-Rate-of-Return|Internal Rate of Return]]",
    "internal rate of return": "[[Wiki/Concepts/Internal-Rate-of-Return|internal rate of return]]",
    "Internal rate of return": "[[Wiki/Concepts/Internal-Rate-of-Return|Internal rate of return]]",
    
    # 4. Depreciation and Amortization / Depreciation Tax Shield / Depreciation
    "Depreciation and Amortization": "[[Wiki/Concepts/Depreciation-and-Amortization|Depreciation and Amortization]]",
    "depreciation and amortization": "[[Wiki/Concepts/Depreciation-and-Amortization|depreciation and amortization]]",
    "Depreciation Tax Shield": "[[Wiki/Concepts/Depreciation-and-Amortization|Depreciation Tax Shield]]",
    "depreciation tax shield": "[[Wiki/Concepts/Depreciation-and-Amortization|depreciation tax shield]]",
    "Depreciation": "[[Wiki/Concepts/Depreciation-and-Amortization|Depreciation]]",
    "depreciation": "[[Wiki/Concepts/Depreciation-and-Amortization|depreciation]]",
    
    # 5. Gordon Growth Model / Equity Valuation
    "Gordon Growth Model": "[[Wiki/Concepts/Equity-Valuation|Gordon Growth Model]]",
    "Gordon growth model": "[[Wiki/Concepts/Equity-Valuation|Gordon growth model]]",
    "Equity Valuation": "[[Wiki/Concepts/Equity-Valuation|Equity Valuation]]",
    "equity valuation": "[[Wiki/Concepts/Equity-Valuation|equity valuation]]",
    
    # 6. Bond Valuation / Valuing Bonds
    "Bond Valuation": "[[Wiki/Concepts/Bond-Valuation|Bond Valuation]]",
    "bond valuation": "[[Wiki/Concepts/Bond-Valuation|bond valuation]]",
    "Valuing Bonds": "[[Wiki/Concepts/Bond-Valuation|Valuing Bonds]]",
    "valuing bonds": "[[Wiki/Concepts/Bond-Valuation|valuing bonds]]",
    
    # 7. Capital Budgeting
    "Capital Budgeting": "[[Wiki/Concepts/Capital-Budgeting|Capital Budgeting]]",
    "capital budgeting": "[[Wiki/Concepts/Capital-Budgeting|capital budgeting]]",
    
    # 8. Capital Structure Decision / Capital Structure
    "Capital Structure Decision": "[[Wiki/Concepts/Capital-Structure|Capital Structure Decision]]",
    "Capital Structure": "[[Wiki/Concepts/Capital-Structure|Capital Structure]]",
    "capital structure": "[[Wiki/Concepts/Capital-Structure|capital structure]]",
    
    # 9. Free Cash Flow Valuation / Free Cash Flow
    "Free Cash Flow Valuation": "[[Wiki/Concepts/Cash-Flow-Statement|Free Cash Flow]] Valuation",
    "Free Cash Flow": "[[Wiki/Concepts/Cash-Flow-Statement|Free Cash Flow]]",
    "free cash flow": "[[Wiki/Concepts/Cash-Flow-Statement|free cash flow]]",
    
    # 10. Financial System Overview / Financial Markets
    "Financial markets": "[[Wiki/Concepts/Financial-System-Overview|Financial markets]]",
    "financial markets": "[[Wiki/Concepts/Financial-System-Overview|financial markets]]",
    
    # 11. Stock Markets (Primary/Secondary Markets, Common/Preferred Stock, ADRs)
    "Secondary Markets": "[[Wiki/Concepts/Stock-Markets|Secondary Markets]]",
    "Primary Markets": "[[Wiki/Concepts/Stock-Markets|Primary Markets]]",
    "Common stock": "[[Wiki/Concepts/Stock-Markets|Common stock]]",
    "Preferred stock": "[[Wiki/Concepts/Stock-Markets|Preferred stock]]",
    "Common Stock": "[[Wiki/Concepts/Stock-Markets|Common Stock]]",
    "Preferred Stock": "[[Wiki/Concepts/Stock-Markets|Preferred Stock]]",
    "ADRs": "[[Wiki/Concepts/Stock-Markets|ADRs]]",
    
    # 12. Interest Rates / Yield Curve / Default Risk / Risk-free rate
    "Interest Rates": "[[Wiki/Concepts/Interest-Rates|Interest Rates]]",
    "interest rates": "[[Wiki/Concepts/Interest-Rates|interest rates]]",
    "Interest rates": "[[Wiki/Concepts/Interest-Rates|Interest rates]]",
    "Yield Curve": "[[Wiki/Concepts/Interest-Rates|Yield Curve]]",
    "yield curve": "[[Wiki/Concepts/Interest-Rates|yield curve]]",
    "Default Risk": "[[Wiki/Concepts/Interest-Rates|Default Risk]]",
    "default risk": "[[Wiki/Concepts/Interest-Rates|default risk]]",
    "risk-free rate": "[[Wiki/Concepts/Interest-Rates|risk-free rate]]",
    
    # 13. Asymmetric Information (Separation of ownership and management)
    "separation of ownership and management": "[[Wiki/Concepts/Asymmetric-Information|separation of ownership and management]]",
    "Separation of ownership and management": "[[Wiki/Concepts/Asymmetric-Information|Separation of ownership and management]]",
    
    # 14. Corporate Finance Topic
    "Corporate Finance": "[[Wiki/Topics/Corporate-Finance|Corporate Finance]]",
    "corporate finance": "[[Wiki/Topics/Corporate-Finance|corporate finance]]",
    
    # 15. Short acronyms
    "PVGO": "[[Wiki/Concepts/Equity-Valuation|PVGO]]",
    "NPV": "[[Wiki/Concepts/Net-Present-Value|NPV]]",
    "IRR": "[[Wiki/Concepts/Internal-Rate-of-Return|IRR]]",
}

# Sort keys by length descending to match longer multi-word phrases first
sorted_keys = sorted(replacements.keys(), key=len, reverse=True)
# Compile regular expression using word boundaries
regex_pattern = re.compile(r'\b(' + '|'.join(map(re.escape, sorted_keys)) + r')\b')

def replace_match(match):
    matched_text = match.group(1)
    return replacements[matched_text]

def linkify_text(text):
    return regex_pattern.sub(replace_match, text)

def process_file():
    print(f"Reading {FILE_PATH.name}...")
    if not FILE_PATH.is_file():
        print("Error: Target file not found!")
        return
        
    content = FILE_PATH.read_text(encoding="utf-8")
    
    # Split off frontmatter to protect it from linkification
    frontmatter_match = re.match(r'^(---\n.*?\n---\n)(.*)$', content, re.DOTALL)
    if frontmatter_match:
        frontmatter, body = frontmatter_match.groups()
    else:
        frontmatter, body = "", content
        
    # Split body by double brackets to isolate existing links
    parts = re.split(r'(\[\[.*?\]\])', body)
    
    modified_count = 0
    for i in range(len(parts)):
        # Only modify parts outside of brackets (even indices)
        if i % 2 == 0:
            original = parts[i]
            linkified = linkify_text(original)
            if linkified != original:
                modified_count += 1
                parts[i] = linkified
                
    if modified_count > 0:
        new_body = "".join(parts)
        FILE_PATH.write_text(frontmatter + new_body, encoding="utf-8")
        print(f"Successfully updated file body with new wikilinks across {modified_count} text blocks!")
    else:
        print("No new wikilinks were needed or added.")

if __name__ == "__main__":
    process_file()
