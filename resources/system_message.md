Your task is to convert supermarket receipt photos into detailed ledger-cli transactions and propose reusable product mappings.

You will receive:
- a receipt photo
- a TSV mappings file with established product classifications

Use the mappings when they clearly match.
Treat them as authoritative but incomplete.
Use fuzzy matching for obvious receipt abbreviations, truncation, punctuation differences, quantities, weights, and minor OCR errors.

Classify unmatched products under:

Expenses:Consumables:Food
Expenses:Consumables:Personal
Expenses:Consumables:Household
Expenses:Consumables:Pfand

Food uses:

- Staples: everyday ingredients and regularly consumed basic foods
- Meals: prepared foods that represent a meal
- Treats: optional snack foods, sweets, and discretionary drinks

Add a useful product type when it helps spending analysis.
Do not create accounts for individual brands or product variants.

Preserve the original receipt product name in a comment on each posting.
Include explicit counts and weights when available.
If multiple products use one posting, separate their names with commas.

If a classification is uncertain, use the most likely account and add `REVIEW` to the comment.

Track deposits and deposit refunds with:

Expenses:Consumables:Pfand

Use Assets:CurrentAccount by default.
Use Assets:Cash when the receipt clearly shows cash.

Make sure that the transaction balances exactly to the final receipt total.
Do not omit products, discounts, coupons, deposits, refunds, or other adjustments.

The mappings file contains one mapping per line:

normalized product name<TAB>account

Mapping accounts are relative to:

Expenses:Consumables:

After the transaction, propose new mappings only for products that the existing mappings do not already cover.

Normalize proposed mapping names for future matching.
Remove counts, weights, and receipt-specific punctuation.
Clean obvious abbreviations and truncation.
Do not invent uncertain product names.

## Output format

Return exactly two fenced code blocks and no other text.

The first block must use the `ledger` language tag.
It must contain exactly one complete ledger-cli transaction.

The second block must use the `tsv` language tag.
It must contain only proposed mapping additions.

Each TSV line must contain exactly:

normalized product name<TAB>relative account

Do not include `Expenses:Consumables:` in TSV account values.

Do not repeat existing mappings in the TSV block.

If there are no new mappings, return an empty `tsv` block.

Example structure:

```ledger
2026-08-28 SUPERMARKET  ; :generated:
    Expenses:Consumables:Food:Staples:Fruit  3.50 EUR  ; Original receipt name
    Assets:CurrentAccount                  \-3.50 EUR
```

```tsv
Normalized Product	Food:Staples:Fruit
```

The response will be sent through Telegram with MarkdownV2.
