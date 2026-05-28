import re
import glob
import sys
from pathlib import Path

# Reconfigure stdout to prevent encoding errors on non-ASCII characters in paths/content
sys.stdout.reconfigure(encoding='utf-8')

def analyze_all():
    files = sorted(glob.glob('Raw/Sources/30705 MARKETING/*.md'), key=lambda p: int(Path(p).stem.split()[1]))
    
    report_lines = []
    
    for f in files:
        name = Path(f).name
        report_lines.append("="*60)
        report_lines.append(f"ANALYZING: {name}")
        report_lines.append("="*60)
        content = Path(f).read_text(encoding="utf-8")
        
        # Extract headings (level 1, 2, 3)
        headings = [line for line in content.splitlines() if line.startswith('#')]
        report_lines.append("Headings:")
        for h in headings:
            report_lines.append("   " + h)
            
        # Search for key terms (bolded or bulleted bolded)
        bold_terms = list(set(re.findall(r'\*\*([^*]+?)\*\*', content)))
        # Filter terms to keep only those that are likely concepts (short, 1-4 words)
        concept_terms = [t.strip() for t in bold_terms if 2 < len(t.strip()) < 40 and not t.strip().isdigit()]
        report_lines.append("\nPotential Concept Terms (Bolded, subset):")
        for t in sorted(concept_terms):
            report_lines.append(f"  - {t}")
        report_lines.append("\n")

    report_path = Path("scratch/marketing_analysis_report.txt")
    report_path.write_text("\n".join(report_lines), encoding="utf-8")
    print(f"Success: Analysis report written to {report_path}")

if __name__ == "__main__":
    analyze_all()
