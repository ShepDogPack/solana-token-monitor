#!/usr/bin/env python3
"""
Solana Token Monitor — Core monitoring script
Built by ShepDog (shepdogcoin.com)
Uses DexScreener public API (no key required)
"""

import json
import sys
import urllib.request
import urllib.error
import os
from datetime import datetime, timezone

DEXSCREENER_URL = "https://api.dexscreener.com/tokens/v1/solana/{}"
DATA_DIR = os.path.expanduser("~/.openclaw/workspace/data/token-monitors")


def fetch_token_data(contract_address: str):
    """Fetch token data from DexScreener API."""
    url = DEXSCREENER_URL.format(contract_address)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "SolanaTokenMonitor/1.0"})
        with urllib.request.urlopen(req, timeout=10) as response:
            data = json.loads(response.read().decode())
            pairs = data if isinstance(data, list) else data.get("pairs", [])
            if not pairs:
                return None
            return max(pairs, key=lambda p: float(p.get("liquidity", {}).get("usd", 0) or 0))
    except Exception as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        return None


def load_config(symbol: str):
    """Load token monitor config."""
    path = os.path.join(DATA_DIR, f"{symbol.upper()}.json")
    if not os.path.exists(path):
        return None
    with open(path) as f:
        return json.load(f)


def save_config(symbol: str, config: dict):
    """Save token monitor config."""
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, f"{symbol.upper()}.json")
    with open(path, "w") as f:
        json.dump(config, f, indent=2)


def setup_monitor(contract_address: str, symbol: str, telegram_chat_id: str = None):
    """Set up monitoring for a token."""
    print(f"Setting up monitor for ${symbol.upper()} ({contract_address})...")
    data = fetch_token_data(contract_address)
    if not data:
        print(f"❌ Could not fetch data for {contract_address}. Check the contract address.")
        sys.exit(1)

    price = float(data.get("priceUsd", 0) or 0)
    market_cap = float(data.get("marketCap", 0) or 0)
    volume_24h = float(data.get("volume", {}).get("h24", 0) or 0)
    liquidity = float(data.get("liquidity", {}).get("usd", 0) or 0)

    config = {
        "symbol": symbol.upper(),
        "contract": contract_address,
        "chain": "solana",
        "telegram_chat_id": telegram_chat_id,
        "thresholds": {
            "price_change_pct": 5.0,
            "volume_spike_multiplier": 2.0,
            "liquidity_drop_pct": 20.0,
        },
        "milestones": [10000, 50000, 100000, 500000, 1000000],
        "milestones_hit": [],
        "last_check": {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "price_usd": price,
            "market_cap": market_cap,
            "volume_24h": volume_24h,
            "liquidity_usd": liquidity,
        },
        "created_at": datetime.now(timezone.utc).isoformat(),
        "enabled": True,
    }

    save_config(symbol, config)
    print(f"""
✅ Monitor configured for ${symbol.upper()}!

Current stats:
  Price:      ${price:.8f}
  Market Cap: ${market_cap:,.0f}
  Volume 24h: ${volume_24h:,.2f}
  Liquidity:  ${liquidity:,.2f}

Alerts will trigger on:
  • Price move > 5%
  • Volume spike > 2x 24h average
  • Liquidity drop > 20%
  • Market cap milestones

Config saved to: {DATA_DIR}/{symbol.upper()}.json
""")


def check_monitor(symbol: str):
    """Check a token and return any
