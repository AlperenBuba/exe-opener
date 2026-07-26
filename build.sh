#!/usr/bin/env bash
set -euo pipefail

echo "[*] Installing PyInstaller..."
pip install pyinstaller --quiet --break-system-packages

echo "[*] Building..."

TCL_DIR=$(python3 -c "
import os
for d in ['/usr/share/tcltk/tcl8.6', '/usr/lib/tcl8.6', '/usr/share/tcl8.6']:
    if os.path.isdir(d): print(d); break
")

TK_DIR=$(python3 -c "
import os
for d in ['/usr/share/tcltk/tk8.6', '/usr/lib/tk8.6', '/usr/share/tk8.6']:
    if os.path.isdir(d): print(d); break
")

ADD_DATA=""
if [ -n "$TCL_DIR" ]; then
    ADD_DATA="$ADD_DATA --add-data $TCL_DIR:tcl"
fi
if [ -n "$TK_DIR" ]; then
    ADD_DATA="$ADD_DATA --add-data $TK_DIR:tk"
fi

pyinstaller --onefile --windowed --name "EXEOpener" $ADD_DATA main.py

echo "[+] Done: dist/EXEOpener"
