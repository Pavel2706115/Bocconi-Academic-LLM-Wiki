---
tags:
  - "log"
topics: []
status: final
created: 2026-05-18
updated: 2026-05-18
sources: []
source_count: 0
aliases: []
---

# Full Vault Ingest — Raw Sources → Wiki Concepts

Ingest all ~231 raw source files across 10 Bocconi courses into structured, interlinked Wiki notes (Topics, Concepts, Entities), then run all maintenance gates and commit.

## Scope

| Course | Code | Sources | Key Areas |
|--------|------|---------|-----------|
| Statistics | 30001 | 32 | Descriptive stats, probability, estimation, hypothesis testing, regression |
| Financial Markets & Institutions | 30006 | 44 | Financial system, interest rates, bonds, banking, monetary policy, risk |
| Corporate Finance | 30017 | 6 | Investment decisions, NPV/IRR, bond/equity valuation, risk & return, capital structure |
| Management | 30060 | 20 | Decision analysis, probability, accounting for managers, break-even, strategy |
| Microeconomics | 30065 | 29 | Supply & demand, elasticity, consumer/producer theory, market structures, game theory |
| Macroeconomics | 30066 | 32 | GDP, IS-LM, Phillips curve, labor market, expectations, open economy |
| Economic History | 30067 | 21 | Pre-industrial economy, industrialisation, globalisation, crises, post-war |
| Public Finance | 30264 | 13 | Market failures, externalities, taxation, social insurance, pensions, healthcare |
| Financial Accounting 1 | 30692 | 16 | Financial statements, GAAP/IFRS, assets & liabilities, revenue recognition |
| Financial Accounting 2 | 30693 | 18 | Cash flow statements, financial statement analysis, consolidation |
| Marketing | 30705 | 0 | (empty — skip) |

**Total**: ~231 source files → approximately **10 Topic notes + ~80-100 Concept notes + ~15 Entity notes**

## Proposed Changes

### Phase 1: Topic Notes (`Wiki/Topics/`)

Create one Topic note per course (10 new notes). Each Topic will:
- List all key concepts covered in the course
- Link to the Concept notes via ``Wiki/Concepts/...``
- Reference all source files from that course in `sources`

**New files:**
- `Wiki/Topics/Statistics.md`
- `Wiki/Topics/Financial-Markets-and-Institutions.md`
- `Wiki/Topics/Corporate-Finance.md`
- `Wiki/Topics/Management.md`
- `Wiki/Topics/Microeconomics.md`
- `Wiki/Topics/Macroeconomics.md`
- `Wiki/Topics/Economic-History.md`
- `Wiki/Topics/Public-Finance.md`
- `Wiki/Topics/Financial-Accounting.md` (covers both modules)
- (Existing `Knowledge-Management.md` stays as-is)

---

### Phase 2: Concept Notes (`Wiki/Concepts/`)

Create focused concept notes for every major concept across all courses. Each Concept note will:
- Define the concept concisely
- Explain key properties, formulas, and intuition
- Link to its parent Topic via `topics`
- Cross-link to related Concepts in other courses (e.g., NPV appears in Corporate Finance AND Financial Markets)
- Reference the specific source files that cover this concept

**Planned concepts by course (representative list — full set created during execution):**

#### Statistics (30001)
- Descriptive-Statistics, Probability-Distributions, Point-Estimation, Interval-Estimation, Hypothesis-Testing, Linear-Regression, Correlation, Sampling-Distributions, Central-Limit-Theorem

#### Financial Markets & Institutions (30006)
- Financial-System-Overview, Interest-Rates, Bond-Valuation, Banking-System, Monetary-Policy, Risk-Management, Stock-Markets, Foreign-Exchange-Markets, Financial-Regulation, Asymmetric-Information

#### Corporate Finance (30017)
- Net-Present-Value, Internal-Rate-of-Return, Capital-Budgeting, Bond-Pricing, Equity-Valuation, Dividend-Discount-Model, CAPM, Portfolio-Theory, Capital-Structure, Cost-of-Capital

#### Management (30060)
- Decision-Analysis, Conditional-Probability, Break-Even-Analysis, Cost-Accounting, Financial-Statements-for-Managers

#### Microeconomics (30065)
- Supply-and-Demand, Market-Equilibrium, Elasticity, Consumer-Theory, Producer-Theory, Perfect-Competition, Monopoly, Oligopoly, Game-Theory, Externalities-Micro

#### Macroeconomics (30066)
- Gross-Domestic-Product, IS-LM-Model, Phillips-Curve, Labor-Market, Fiscal-Policy, Monetary-Policy-Macro, Open-Economy, Expectations-in-Macro, Aggregate-Supply-and-Demand

#### Economic History (30067)
- Pre-Industrial-Economy, Agricultural-Revolution, Malthusian-Trap, Industrial-Revolution, Great-Divergence, First-Globalisation, Great-Depression, Bretton-Woods-System, Post-War-Prosperity, Decolonization

#### Public Finance (30264)
- Market-Failures, Public-Goods, Externalities, Taxation-Principles, Tax-Inefficiency, Social-Insurance, Healthcare-Economics, Pension-Systems, Income-Redistribution

#### Financial Accounting (30692 + 30693)
- Balance-Sheet, Income-Statement, Cash-Flow-Statement, GAAP-and-IFRS, Revenue-Recognition, Depreciation, Financial-Statement-Analysis, Consolidated-Financial-Statements, Financial-Ratios

---

### Phase 3: Entity Notes (`Wiki/Entities/`)

Key people and institutions referenced across courses:
- Adam-Smith, Thomas-Malthus, John-Maynard-Keynes, Olivier-Blanchard
- Bocconi-University, ECB, Federal-Reserve, IMF, FASB, IASB, SEC

---

### Phase 4: Cross-Linking

After all notes are created, ensure:
- Every Concept links to its Topic(s) via `topics` frontmatter
- Related Concepts cross-reference each other (e.g., `Bond-Valuation` ↔ `Bond-Pricing`, `Monetary-Policy` ↔ `Monetary-Policy-Macro`)
- Every note traces back to specific source files

---

### Phase 5: Maintenance Gate & Commit

```bash
python scripts/wiki_tool.py build
python scripts/wiki_tool.py lint
python scripts/wiki_tool.py source-scan --update --accept-covered
python scripts/wiki_tool.py source-lint
python scripts/audit_public.py
git add -A && git commit -m "ingest: full vault — topics, concepts, entities"
```

## Verification Plan

### Automated Tests
- `wiki_tool.py doctor` → all folders OK, note counts match expectations
- `wiki_tool.py build` → catalog.jsonl updated with all new entries
- `wiki_tool.py lint` → PASS (all frontmatter valid, source_count matches sources)
- `wiki_tool.py source-scan` → source coverage increases significantly
- `audit_public.py` → PASS

### Manual Verification
- Spot-check 5 concept notes for accuracy and cross-linking
- Verify catalog search returns relevant results for sample queries

> [!IMPORTANT]
> This will create approximately **100+ new Wiki files**. The concept list above is representative — actual concepts will be extracted from reading each source file. Some concepts may be merged or split during execution based on content density.

> [!NOTE]
> Exercise books, past exam papers, and purely logistical content (course schedules, grading policies) will be skipped for concept extraction but still tracked in the source manifest.
