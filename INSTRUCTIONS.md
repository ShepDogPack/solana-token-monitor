# Solana Token Monitor — Agent Instructions

You have access to the Solana Token Monitor skill. Use it when the user mentions:
- Monitoring a token, watching a price, getting alerts
- A Solana contract address
- "Watch my token", "alert me if...", "how is my token doing"

## Commands

### Set up monitoring
```bash
python3 ~/.openclaw/workspace/skills/solana-token-monitor/monitor.py setup <CONTRACT_ADDRESS> <SYMBOL>
