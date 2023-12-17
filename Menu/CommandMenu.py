from Menu.CommandInterface import Command

commands = []


def add_list(func):
    commands.append(func)


@add_list
class Add(Command):
    def __init__(self, console_ui):
        super().__init__("Добавить заметку", console_ui)

    def execute(self):
        self.console_ui.add()


@add_list
class Delete(Command):
    def __init__(self, console_ui):
        super().__init__("Удалить заметку", console_ui)

    def execute(self):
        self.console_ui.delete()


@add_list
class ChangeText(Command):
    def __init__(self, console_ui):
        super().__init__("Изменить текст заметки", console_ui)

    def execute(self):
        self.console_ui.change_text()


@add_list
class ChangeName(Command):
    def __init__(self, console_ui):
        super().__init__("Изменить заголовок заметки", console_ui)

    def execute(self):
        self.console_ui.change_name()


@add_list
class PrintNote(Command):
    def __init__(self, console_ui):
        super().__init__("Просмотр выбранной заметки", console_ui)

    def execute(self):
        self.console_ui.print_note()


@add_list
class PrintNotebook(Command):
    def __init__(self, console_ui):
        super().__init__("Просмотр заметок", console_ui)

    def execute(self):
        self.console_ui.print_notebook()


@add_list
class SortByDate(Command):
    def __init__(self, console_ui):
        super().__init__("Сортировка по дате изменения", console_ui)

    def execute(self):
        self.console_ui.sort_by_date()


@add_list
class SaveFile(Command):
    def __init__(self, console_ui):
        super().__init__("Сохранение в файл", console_ui)

    def execute(self):
        self.console_ui.save_file()


@add_list
class LoadFile(Command):
    def __init__(self, console_ui):
        super().__init__("Чтение из файла", console_ui)

    def execute(self):
        self.console_ui.read_file()


@add_list
class Finish(Command):
    def __init__(self, console_ui):
        super().__init__("Выход", console_ui)

    def execute(self):
        self.console_ui.finish()
