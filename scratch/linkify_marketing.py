import os
import re
import glob
import sys
from pathlib import Path

# Reconfigure stdout to prevent encoding errors on non-ASCII characters
sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
DIR_PATH = ROOT / "Raw" / "Sources" / "30705 MARKETING"

replacements = {
    # 1. Sustainable Marketing and Trust
    "Sustainable Marketing and Trust": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|Sustainable Marketing and Trust]]",
    "Sustainable Marketing": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|Sustainable Marketing]]",
    "sustainable marketing": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|sustainable marketing]]",
    "Trust in Marketing": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|Trust in Marketing]]",
    "trust-oriented marketing": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|trust-oriented marketing]]",
    "Trust-oriented marketing": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|Trust-oriented marketing]]",
    "Customer Lifetime Value": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|Customer Lifetime Value]]",
    "Customer lifetime value": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|Customer lifetime value]]",
    "Customer Equity": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|Customer Equity]]",
    "customer equity": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|customer equity]]",
    "Corporate Social Responsibility": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|Corporate Social Responsibility]]",
    "corporate social responsibility": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|corporate social responsibility]]",
    "Diversity Brand Index": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|Diversity Brand Index]]",
    "Net Promoter Score": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|Net Promoter Score]]",
    "DBI": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|DBI]]",
    "CSR": "[[Wiki/Concepts/Sustainable-Marketing-and-Trust|CSR]]",
    
    # 2. Marketing Environment and Competition
    "Marketing Environment and Competition": "[[Wiki/Concepts/Marketing-Environment-and-Competition|Marketing Environment and Competition]]",
    "Marketing Environment": "[[Wiki/Concepts/Marketing-Environment-and-Competition|Marketing Environment]]",
    "marketing environment": "[[Wiki/Concepts/Marketing-Environment-and-Competition|marketing environment]]",
    "Competitive Environment": "[[Wiki/Concepts/Marketing-Environment-and-Competition|Competitive Environment]]",
    "competitive environment": "[[Wiki/Concepts/Marketing-Environment-and-Competition|competitive environment]]",
    "Macro Environment": "[[Wiki/Concepts/Marketing-Environment-and-Competition|Macro Environment]]",
    "macro-environment": "[[Wiki/Concepts/Marketing-Environment-and-Competition|macro-environment]]",
    "Micro Environment": "[[Wiki/Concepts/Marketing-Environment-and-Competition|Micro Environment]]",
    "micro-environment": "[[Wiki/Concepts/Marketing-Environment-and-Competition|micro-environment]]",
    "Strategic Group": "[[Wiki/Concepts/Marketing-Environment-and-Competition|Strategic Group]]",
    "strategic group": "[[Wiki/Concepts/Marketing-Environment-and-Competition|strategic group]]",
    "Strategic Groups": "[[Wiki/Concepts/Marketing-Environment-and-Competition|Strategic Groups]]",
    "strategic groups": "[[Wiki/Concepts/Marketing-Environment-and-Competition|strategic groups]]",
    "Structure-Conduct-Performance": "[[Wiki/Concepts/Marketing-Environment-and-Competition|Structure-Conduct-Performance]]",
    "SCP Paradigm": "[[Wiki/Concepts/Marketing-Environment-and-Competition|SCP Paradigm]]",
    "SCP model": "[[Wiki/Concepts/Marketing-Environment-and-Competition|SCP model]]",
    
    # 3. Demand Estimation and Market Share
    "Demand Estimation and Market Share": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|Demand Estimation and Market Share]]",
    "Demand Estimation": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|Demand Estimation]]",
    "demand estimation": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|demand estimation]]",
    "Market Potential": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|Market Potential]]",
    "market potential": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|market potential]]",
    "Potential Gap": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|Potential Gap]]",
    "potential gap": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|potential gap]]",
    "Market Share": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|Market Share]]",
    "market share": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|market share]]",
    "Absolute Market Share": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|Absolute Market Share]]",
    "Relative Market Share": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|Relative Market Share]]",
    "Penetration Index": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|Penetration Index]]",
    "penetration index": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|penetration index]]",
    "Weighted Coverage Index": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|Weighted Coverage Index]]",
    "weighted coverage index": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|weighted coverage index]]",
    "Selection Index": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|Selection Index]]",
    "selection index": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|selection index]]",
    "Customer Portfolio Quality Index": "[[Wiki/Concepts/Demand-Estimation-and-Market-Share|Customer Portfolio Quality Index]]",
    
    # 4. Consumer Behavior Models
    "Consumer Behavior Models": "[[Wiki/Concepts/Consumer-Behavior-Models|Consumer Behavior Models]]",
    "Consumer Behavior": "[[Wiki/Concepts/Consumer-Behavior-Models|Consumer Behavior]]",
    "consumer behavior": "[[Wiki/Concepts/Consumer-Behavior-Models|consumer behavior]]",
    "Purchasing Process": "[[Wiki/Concepts/Consumer-Behavior-Models|Purchasing Process]]",
    "purchasing process": "[[Wiki/Concepts/Consumer-Behavior-Models|purchasing process]]",
    "Customer Journey Map": "[[Wiki/Concepts/Consumer-Behavior-Models|Customer Journey Map]]",
    "Customer Journey": "[[Wiki/Concepts/Consumer-Behavior-Models|Customer Journey]]",
    "customer journey": "[[Wiki/Concepts/Consumer-Behavior-Models|customer journey]]",
    "Psychological Involvement": "[[Wiki/Concepts/Consumer-Behavior-Models|Psychological Involvement]]",
    "psychological involvement": "[[Wiki/Concepts/Consumer-Behavior-Models|psychological involvement]]",
    "Expected Value Model": "[[Wiki/Concepts/Consumer-Behavior-Models|Expected Value Model]]",
    "Fishbein Model": "[[Wiki/Concepts/Consumer-Behavior-Models|Fishbein Model]]",
    "Conjunctive Model": "[[Wiki/Concepts/Consumer-Behavior-Models|Conjunctive Model]]",
    "conjunctive model": "[[Wiki/Concepts/Consumer-Behavior-Models|conjunctive model]]",
    "Disjunctive Model": "[[Wiki/Concepts/Consumer-Behavior-Models|Disjunctive Model]]",
    "disjunctive model": "[[Wiki/Concepts/Consumer-Behavior-Models|disjunctive model]]",
    "Lexicographic Model": "[[Wiki/Concepts/Consumer-Behavior-Models|Lexicographic Model]]",
    "lexicographic model": "[[Wiki/Concepts/Consumer-Behavior-Models|lexicographic model]]",
    "Choice-Set Models": "[[Wiki/Concepts/Consumer-Behavior-Models|Choice-Set Models]]",
    "Choice-Set": "[[Wiki/Concepts/Consumer-Behavior-Models|Choice-Set]]",
    "choice-set": "[[Wiki/Concepts/Consumer-Behavior-Models|choice-set]]",
    "Purchasing Roles": "[[Wiki/Concepts/Consumer-Behavior-Models|Purchasing Roles]]",
    "purchasing roles": "[[Wiki/Concepts/Consumer-Behavior-Models|purchasing roles]]",
    
    # 5. Commercial Distribution and Retail
    "Commercial Distribution and Retail": "[[Wiki/Concepts/Commercial-Distribution-and-Retail|Commercial Distribution and Retail]]",
    "Commercial Distribution": "[[Wiki/Concepts/Commercial-Distribution-and-Retail|Commercial Distribution]]",
    "commercial distribution": "[[Wiki/Concepts/Commercial-Distribution-and-Retail|commercial distribution]]",
    "Retail Format": "[[Wiki/Concepts/Commercial-Distribution-and-Retail|Retail Format]]",
    "Retail Formats": "[[Wiki/Concepts/Commercial-Distribution-and-Retail|Retail Formats]]",
    "retail formats": "[[Wiki/Concepts/Commercial-Distribution-and-Retail|retail formats]]",
    "Distribution Formats": "[[Wiki/Concepts/Commercial-Distribution-and-Retail|Distribution Formats]]",
    "distribution formats": "[[Wiki/Concepts/Commercial-Distribution-and-Retail|distribution formats]]",
    "Commercial Services": "[[Wiki/Concepts/Commercial-Distribution-and-Retail|Commercial Services]]",
    "commercial services": "[[Wiki/Concepts/Commercial-Distribution-and-Retail|commercial services]]",
    
    # 6. Marketing Segmentation and Positioning
    "Marketing Segmentation and Positioning": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|Marketing Segmentation and Positioning]]",
    "STP Process": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|STP Process]]",
    "Market Segmentation": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|Market Segmentation]]",
    "market segmentation": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|market segmentation]]",
    "Segment Targeting": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|Segment Targeting]]",
    "Targeting": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|Targeting]]",
    "targeting": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|targeting]]",
    "Product Positioning": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|Product Positioning]]",
    "Positioning": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|Positioning]]",
    "positioning": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|positioning]]",
    "Perceptual Map": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|Perceptual Map]]",
    "perceptual map": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|perceptual map]]",
    "Preferences Map": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|Preferences Map]]",
    "preferences map": "[[Wiki/Concepts/Marketing-Segmentation-and-Positioning|preferences map]]",
    
    # 7. Product Range and Branding
    "Product Range and Branding": "[[Wiki/Concepts/Product-Range-and-Branding|Product Range and Branding]]",
    "Product Range": "[[Wiki/Concepts/Product-Range-and-Branding|Product Range]]",
    "product range": "[[Wiki/Concepts/Product-Range-and-Branding|product range]]",
    "Product Mix": "[[Wiki/Concepts/Product-Range-and-Branding|Product Mix]]",
    "product mix": "[[Wiki/Concepts/Product-Range-and-Branding|product mix]]",
    "Product Line": "[[Wiki/Concepts/Product-Range-and-Branding|Product Line]]",
    "product line": "[[Wiki/Concepts/Product-Range-and-Branding|product line]]",
    "Branding Strategy": "[[Wiki/Concepts/Product-Range-and-Branding|Branding Strategy]]",
    "branding strategy": "[[Wiki/Concepts/Product-Range-and-Branding|branding strategy]]",
    "Branded House": "[[Wiki/Concepts/Product-Range-and-Branding|Branded House]]",
    "branded house": "[[Wiki/Concepts/Product-Range-and-Branding|branded house]]",
    "House of Brands": "[[Wiki/Concepts/Product-Range-and-Branding|House of Brands]]",
    "house of brands": "[[Wiki/Concepts/Product-Range-and-Branding|house of brands]]",
    "BCG Matrix": "[[Wiki/Concepts/Product-Range-and-Branding|BCG Matrix]]",
    "BCG matrix": "[[Wiki/Concepts/Product-Range-and-Branding|BCG matrix]]",
    "New Product Development": "[[Wiki/Concepts/Product-Range-and-Branding|New Product Development]]",
    "NPD": "[[Wiki/Concepts/Product-Range-and-Branding|NPD]]",
    
    # 8. Pricing Policies and Bundling
    "Pricing Policies and Bundling": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|Pricing Policies and Bundling]]",
    "Pricing Strategy": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|Pricing Strategy]]",
    "pricing strategy": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|pricing strategy]]",
    "Price Setting": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|Price Setting]]",
    "price setting": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|price setting]]",
    "Break-even Price": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|Break-even Price]]",
    "break-even price": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|break-even price]]",
    "Indifference Price": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|Indifference Price]]",
    "indifference price": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|indifference price]]",
    "Price Discrimination": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|Price Discrimination]]",
    "price discrimination": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|price discrimination]]",
    "Price Differentiation": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|Price Differentiation]]",
    "price differentiation": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|price differentiation]]",
    "Bundling": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|Bundling]]",
    "bundling": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|bundling]]",
    "Unbundling": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|Unbundling]]",
    "unbundling": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|unbundling]]",
    "Skimming Pricing": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|Skimming Pricing]]",
    "skimming pricing": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|skimming pricing]]",
    "Penetration Pricing": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|Penetration Pricing]]",
    "penetration pricing": "[[Wiki/Concepts/Pricing-Policies-and-Bundling|penetration pricing]]",
    
    # 9. Marketing Communication and Advertising
    "Marketing Communication and Advertising": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|Marketing Communication and Advertising]]",
    "Marketing Communication": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|Marketing Communication]]",
    "marketing communication": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|marketing communication]]",
    "Communication Mix": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|Communication Mix]]",
    "communication mix": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|communication mix]]",
    "Advertising Brief": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|Advertising Brief]]",
    "advertising brief": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|advertising brief]]",
    "Advertising Message": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|Advertising Message]]",
    "advertising message": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|advertising message]]",
    "Media Strategy": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|Media Strategy]]",
    "media strategy": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|media strategy]]",
    "Online Advertising": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|Online Advertising]]",
    "online advertising": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|online advertising]]",
    "Direct Marketing": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|Direct Marketing]]",
    "direct marketing": "[[Wiki/Concepts/Marketing-Communication-and-Advertising|direct marketing]]",
    
    # 10. Distribution Channels and Trade Marketing
    "Distribution Channels and Trade Marketing": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|Distribution Channels and Trade Marketing]]",
    "Distribution Channels": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|Distribution Channels]]",
    "distribution channels": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|distribution channels]]",
    "Distribution Channel": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|Distribution Channel]]",
    "distribution channel": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|distribution channel]]",
    "Channel Architecture": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|Channel Architecture]]",
    "channel architecture": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|channel architecture]]",
    "Direct Channel": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|Direct Channel]]",
    "direct channel": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|direct channel]]",
    "Indirect Channel": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|Indirect Channel]]",
    "indirect channel": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|indirect channel]]",
    "Omni-channel": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|Omni-channel]]",
    "omni-channel": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|omni-channel]]",
    "Omni-Channel": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|Omni-Channel]]",
    "Push and Pull Policies": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|Push and Pull Policies]]",
    "Push Policy": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|Push Policy]]",
    "push policy": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|push policy]]",
    "Pull Policy": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|Pull Policy]]",
    "pull policy": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|pull policy]]",
    "Trade Marketing": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|Trade Marketing]]",
    "trade marketing": "[[Wiki/Concepts/Distribution-Channels-and-Trade-Marketing|trade marketing]]",
    
    # 11. Central Topic (to be mapped only outside equations)
    "Marketing": "[[Wiki/Topics/Marketing|Marketing]]",
    "marketing": "[[Wiki/Topics/Marketing|marketing]]",
}

# Sort keys by length descending to match longer multi-word phrases first
sorted_keys = sorted(replacements.keys(), key=len, reverse=True)
# Compile regular expression using word boundaries
regex_pattern = re.compile(r'\b(' + '|'.join(map(re.escape, sorted_keys)) + r')\b')

def replace_match(match):
    matched_text = match.group(1)
    return replacements[matched_text]

def linkify_text(text):
    # To prevent placing links inside LaTeX formulas, we split by $ to skip inline math
    # even indices are outside math, odd indices are inside math mode
    math_parts = re.split(r'(\$.*?\$)|\$\$(.*?)\$\$', text, flags=re.DOTALL)
    
    # Re-assemble while only applying linkify to non-math parts
    for i in range(len(math_parts)):
        part = math_parts[i]
        if part is None:
            continue
        # We check if it is part of a dollar split (which begins and ends with $)
        # re.split keeps groups in the result list. If it starts with $ or is None/empty, we skip it
        if not (part.startswith('$') or part.endswith('$')):
            math_parts[i] = regex_pattern.sub(replace_match, part)
            
    # filter out None values and join
    return "".join(p for p in math_parts if p is not None)

def process_file(file_path):
    print(f"Processing: {file_path.name}")
    content = file_path.read_text(encoding="utf-8")
    
    # Split off frontmatter to protect it from linkification
    frontmatter_match = re.match(r'^(---\n.*?\n---\n)(.*)$', content, re.DOTALL)
    if frontmatter_match:
        frontmatter, body = frontmatter_match.groups()
    else:
        frontmatter, body = "", content
        
    # Split body by double brackets to protect existing links
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
        file_path.write_text(frontmatter + new_body, encoding="utf-8")
        print(f"  Success: Updated with new concepts!")
    else:
        print("  No new links needed.")

def run_all():
    print(f"Linkifying all raw sources in {DIR_PATH}...")
    files = list(DIR_PATH.glob("*.md"))
    for f in files:
        process_file(f)

if __name__ == "__main__":
    run_all()
