#!/bin/bash

set -e

echo "========================================"
echo " Microsoft Email Checker - Installer"
echo "========================================"

# 1️⃣ Check OS
if ! command -v apt >/dev/null 2>&1; then
  echo "❌ This installer supports Debian/Ubuntu-based systems only."
  exit 1
fi

# 2️⃣ Update system
echo "[1/6] Updating system packages..."
sudo apt update

# 3️⃣ Install system dependencies
echo "[2/6] Installing system dependencies..."
sudo apt install -y \
  git \
  python3 \
  python3-venv \
  python3-pip \
  curl \
  wget \
  ca-certificates \
  fonts-liberation \
  libnss3 \
  libatk-bridge2.0-0 \
  libatk1.0-0 \
  libcups2 \
  libdrm2 \
  libxkbcommon0 \
  libxcomposite1 \
  libxdamage1 \
  libxrandr2 \
  libgbm1 \
  libasound2 \
  libpangocairo-1.0-0 \
  libpango-1.0-0 \
  libgtk-3-0

# 4️⃣ Create virtual environment
echo "[3/6] Creating Python virtual environment..."
python3 -m venv mscheck

# 5️⃣ Activate venv and install Python deps
echo "[4/6] Installing Python dependencies..."
source mscheck/bin/activate
pip install --upgrade pip
pip install playwright pandas

# 6️⃣ Install Playwright browser
echo "[5/6] Installing Playwright Chromium..."
playwright install chromium

echo "[6/6] Done."

echo ""
echo "========================================"
echo " ✅ Installation completed successfully"
echo "========================================"
echo ""
echo "Next steps:"
echo "  source mscheck/bin/activate"
echo "  python mscheck.py"
echo ""
