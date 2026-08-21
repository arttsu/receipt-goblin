# Receipt Goblin Bot

A Telegram bot to help convert supermarket receipts into detailed ledger transactions.

## Workflow

1. Me: Send a photo of a supermarket receipt.
2. Bot: Send a message with a proposed [ledger](https://ledger-cli.org/) transaction with fine-grained categories (generated via an LLM)
3. [FUTURE] Me: Approve the proposal (via 👍) or send a message with a correction
4. [FUTURE] Bot: In case of 👍, append the transaction to the ledger file.
