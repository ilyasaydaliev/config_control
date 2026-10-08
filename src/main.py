import argparse
import os

from shell import Shell, ShellError


def run_line(shell, line):
    try:
        out = shell.execute(line)
    except ShellError as err:
        print(err)
        return
    if out:
        print(out)


def repl(shell):
    while shell.running:
        try:
            line = input(shell.prompt())
        except EOFError:
            print()
            break
        except KeyboardInterrupt:
            print()
            continue
        run_line(shell, line)


def parse_args(argv=None):
    ap = argparse.ArgumentParser(description="UNIX-like shell emulator")
    ap.add_argument("--vfs", help="path to the physical VFS location")
    ap.add_argument("--script", help="path to the startup script")
    return ap.parse_args(argv)


def vfs_name(path):
    if not path:
        return "vfs"
    return os.path.basename(os.path.normpath(path)) or "vfs"


def debug_params(args):
    print("[debug] parameters:")
    for key, value in sorted(vars(args).items()):
        print(f"[debug]   {key} = {value}")


def run_script(shell, path):
    try:
        with open(path, encoding="utf-8") as src:
            lines = src.read().splitlines()
    except OSError as err:
        print(f"script error: cannot read {path}: {err.strerror}")
        return
    for line in lines:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        print(shell.prompt() + line)
        run_line(shell, line)
        if not shell.running:
            break


def main(argv=None):
    args = parse_args(argv)
    debug_params(args)
    shell = Shell(vfs_name(args.vfs))
    if args.script:
        run_script(shell, args.script)
    if shell.running:
        repl(shell)


if __name__ == "__main__":
    main()
