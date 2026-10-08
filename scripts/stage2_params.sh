#!/bin/sh
# Tests all command line parameters of the emulator.
cd "$(dirname "$0")/.." || exit 1
echo "== no parameters (stdin: exit) =="
echo exit | python3 src/main.py
echo "== --vfs only =="
echo exit | python3 src/main.py --vfs examples/vfs/files
echo "== --script only =="
python3 src/main.py --script scripts/basic.emu
echo "== both parameters =="
python3 src/main.py --vfs examples/vfs/files --script scripts/basic.emu
echo "== missing script =="
echo exit | python3 src/main.py --script no_such.emu
