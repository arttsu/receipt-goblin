# Receipt Goblin Bot

A Telegram bot to help convert supermarket receipts into detailed ledger transactions.

## Workflow

1. Me: Send a photo of a supermarket receipt.
2. Bot: Send a message with a proposed [ledger](https://ledger-cli.org/) transaction with fine-grained categories (generated via an LLM)
3. [FUTURE] Me: Approve the proposal (via 👍) or send a message with a correction
4. [FUTURE] Bot: In case of 👍, append the transaction to the ledger file.

## Service setup (Fedora)

### 1) Create a dedicated user

```bash
sudo useradd --system --create-home receipt-goblin
```

### 2) Clone the repo

```bash
sudo mkdir /opt/receipt-goblin
sudo chown receipt-goblin:receipt-goblin /opt/receipt-goblin
sudo -u receipt-goblin git clone https://github.com/arttsu/receipt-goblin.git /opt/receipt-goblin
```

### 3) Install uv

```bash
sudo dnf install uv -y
```

### 4) Create the service

```bash
sudo cp /opt/receipt-goblin/receipt-goblin.example.service /etc/systemd/system/receipt-goblin.service
```

### 5) Set environment variables

```bash
sudo nano /etc/systemd/system/receipt-goblin.service
```

### 6) Enable and start the service

```
sudo systemctl daemon-reload
sudo systemctl enable receipt-goblin
sudo systemctl start receipt-goblin
```
