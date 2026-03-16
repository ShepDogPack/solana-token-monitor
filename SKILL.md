---
name: solana-token-monitor
description: >
  Monitor any Solana token 24/7 using DexScreener. Get Telegram alerts for price
  moves, whale buys, volume spikes, and new holder milestones. Built by the creator
  of $SHEP — a real Solana token founder who needed this and built it.
  Use when: (1) you launched a Solana token and want passive monitoring, (2) you
  want whale alerts on any Solana token, (3) you want daily/hourly token reports.


  openclaw:
    emoji: "🐕"
    version: "1.0.0"
    author: "ShepDog (https://shepdogcoin.com)"
    tags: ["crypto", "solana", "defi", "token", "monitoring", "alerts"]
    requires:
      bins: ["curl", "python3"]
---

# Solana Token Monitor

Monitor any Solana token 24/7. Built by a real Solana token founder.

## Setup (2 minutes)

1. Find your token's contract address on DexScreener or Solscan
2. Tell your OpenClaw: **"Set up Solana token monitor for contract address [YOUR_ADDRESS]"**
3. Your OpenClaw will save the config and start monitoring on the next heartbeat

That's it. No API keys. No paid subscriptions. Fully autonomous once configured.

## What It Monitors

- **Price** — alerts when price moves >5% in either direction within 1 hour
- **Volume** — alerts when 1-hour volume spikes >2x the 24-hour average
- **Liquidity** — alerts when liquidity drops >20% (potential rug warning)
- **Market cap milestones** — notifies at $10K, $50K, $100K, $500K, $1M
- **Whale activity** — alerts on single transactions >$500 USD

## Alert Levels

- 🔴 **URGENT** — liquidity drop >20%, price crash >15%, whale dump detected
- 🟡 **NOTABLE** — price move >5%, volume spike, milestone hit
- ⚪️ **FYI** — daily summary report (price, volume, holders, 24h change)

## Commands

Tell your OpenClaw:
- **"Monitor [CONTRACT_ADDRESS] for my token [SYMBOL]"** — sets up monitoring
- **"Token report for [SYMBOL]"** — get an instant status report
- **"Stop monitoring [SYMBOL]"** — disables alerts
- **"Show all monitored tokens"** — list active monitors

## How It Works

This skill uses the free DexScreener API (no key required):
`https://api.dexscreener.com/tokens/v1/solana/{CONTRACT_ADDRESS}`

Your OpenClaw checks during heartbeats (every 30 minutes by default).
Alert thresholds are configurable in your token's config file.

## Config File Location

After setup: `~/.openclaw/workspace/data/token-monitors/{SYMBOL}.json`


## Built By

This skill was built by the creator of $SHEP — a Solana meme coin.

🐕 $SHEP — The Loyal Crypto Companion
Website: https://shepdogcoin.com
X: https://x.com/ShepDogCoin

---

*Free to use. If this helps you, consider checking out $SHEP.*


