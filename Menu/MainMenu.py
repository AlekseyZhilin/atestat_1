from Menu.CommandMenu import commands


class MainMenu:
    def __init__(self):
        self._main_menu = []

    def add_commands(self, command_list: list, console_ui):
        for cmd in command_list:
            self._main_menu.append(cmd(console_ui))

    def menu(self) -> str:
        res_menu = "-----Меню------\n"
        for numb, el in enumerate(self._main_menu, start=1):
            res_menu += f"{numb}) {el.description}\n"

        return res_menu

    def execute(self, choice: int):
        command = self._main_menu[choice]
        command.execute()

    def get_size(self) -> int:
        return len(self._main_menu)


def make_menu(console_ui):
    menu = MainMenu()
    menu.add_commands(commands, console_ui)
    return menu

