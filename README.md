# Shell emulator (variant 16)

CLI emulator of a UNIX-like shell working over an in-memory virtual
file system (VFS).

## Commands
- `exit` — leave the emulator.
- `ls`, `cd` — see below.

Arguments in single/double quotes are parsed as one argument.
The prompt contains the VFS name: `vfs:~$`.

## Build
```
make run      # start the emulator
```

## Configuration (stage 2)
```
python3 src/main.py [--vfs DIR] [--script FILE]
```
- `--vfs` — physical path of the VFS (its base name is shown in the prompt).
- `--script` — startup script. One command per line, `#` starts a
  comment. Input and output are echoed like a dialogue; a failed line is
  reported and the script goes on. All parameters are printed at start
  as `[debug]` lines. Demo: `sh scripts/stage2_params.sh`.
