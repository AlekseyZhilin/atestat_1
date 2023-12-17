from Menu.MainMenu import make_menu


class ConsoleView:
    def __init__(self, presenter, model):
        self._presenter = presenter(self, model())
        self._menu = make_menu(self)
        self._work = True

    def start_menu(self):
        self._hello()
        while self._work:
            print(self._menu.menu())
            self._execute()

    def _execute(self):
        choice = input("Выберете пункт: ")
        if self._check_text_for_int(choice):
            numb = int(choice)
            if 0 < numb <= self._menu.get_size():
                self._menu.execute(numb - 1)
                return

        print("Вы неверно указали пункт меню")

    def _check_text_for_int(self, text: str) -> bool:
        if text.isdigit():
            return True
        return False

    def print_answer(self, answer: str):
        print(answer)
        print()

    def _hello(self):
        print("Здравствуйте!\n")

    def bad_answer(self):
        print("Вы неверно выбрали номер заметки\n")

    def add(self):
        name = input("Введите наименование заметки: ")
        text = input("Введите текст: ")
        self._presenter.add_note(name, text)

    def delete(self):
        self.print_notebook()
        choice = input("Введите номер удаляемой темы: ")
        if self._check_text_for_int(choice):
            self._presenter.delete_note(int(choice))
            return
        self.bad_answer()

    def change_text(self):
        self.print_notebook()
        choice = input("Введите номер заметки, для изменения текста: ")
        if self._check_text_for_int(choice):
            text = input("Введите текст: ")
            self._presenter.change_text_note(int(choice), text)
            return
        self.bad_answer()

    def change_name(self):
        self.print_notebook()
        choice = input("Введите номер заметки, для изменения наименования: ")
        if self._check_text_for_int(choice):
            text = input("Введите наименование: ")
            self._presenter.change_name_note(int(choice), text)
            return
        self.bad_answer()

    def print_note(self):
        self.print_notebook()
        choice = input("Введите номер заметки, для просмотра: ")
        if self._check_text_for_int(choice):
            self._presenter.print_note(int(choice))
            return
        self.bad_answer()

    def print_notebook(self):
        self._presenter.print_notebook()

    def sort_by_date(self):
        self._presenter.sort_by_date()

    def save_file(self):
        path = input("Укажите имя записываемого файла (пустое значение - по умолчанию - notebook.csv): ")
        self._presenter.save_file(path)

    def read_file(self):
        path = input("Укажите имя считываемого файла (пустое значение - по умолчанию - notebook.csv): ")
        self._presenter.read_file()

    def finish(self):
        print("Досвидания!")
        self._work = False
