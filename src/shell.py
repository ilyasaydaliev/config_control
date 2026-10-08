import shlex


class ShellError(Exception):
    """Ошибка, не останавливающая работу программы"""


def parse(line):
    try:
        parts = shlex.split(line, comments=True)
    except ValueError as err:
        raise ShellError(f"parse error: {err}") from err
    if not parts:
        return None, []
    return parts[0], parts[1:]


class Shell:
    """Состояния оболочки и имплементация команд"""

    def __init__(self, vfs_name="vfs"):
        """Создание имени оболочки `vfs_name`"""
        self.vfs_name = vfs_name
        self.running = True

    def prompt(self):
        return f"{self.vfs_name}:~$ "

    def execute(self, line):
        """Ввод строки и ее вывод"""
        name, args = parse(line)
        if name is None:
            return ""
        handler = getattr(self, "cmd_" + name.replace("-", "_"), None)
        if handler is None:
            raise ShellError(f"{name}: command not found")
        return handler(args)

    def cmd_ls(self, args):
        """Заглушка"""
        return f"ls {args}"

    def cmd_cd(self, args):
        """Заглушка"""
        return f"cd {args}"

    def cmd_exit(self, args):
        """Выход из оболочки"""
        if args:
            raise ShellError("exit: too many arguments")
        self.running = False
        return ""
