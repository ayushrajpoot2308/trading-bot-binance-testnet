# Binance Futures Testnet Trading Bot (Python)

## Overview
A simplified Python trading bot for Binance USDT-M Futures **Testnet**.
Supports MARKET and LIMIT orders with proper CLI, logging, and error handling.

## Setup
1. Create a Binance Futures Testnet account
2. Generate API Key & Secret
3. Set environment variables:
   - BINANCE_API_KEY
   - BINANCE_API_SECRET

## Install
```bash
pip install -r requirements.txt
```

## Run Examples
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000
```

## Assumptions
- Testnet environment only
- Order responses depend on Binance availability

## Logs
Logs are written to `trading_bot.log`