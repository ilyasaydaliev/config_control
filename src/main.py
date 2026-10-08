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


def main():
    repl(Shell())


if __name__ == "__main__":
    main()
