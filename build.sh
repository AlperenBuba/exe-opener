#!/usr/bin/env bash
set -euo pipefail

echo "[*] Installing PyInstaller..."
pip install pyinstaller --quiet

echo "[*] Building..."
pyinstaller --onefile --windowed --name "EXEOpener" main.py

echo "[+] Done: dist/EXEOpener"
