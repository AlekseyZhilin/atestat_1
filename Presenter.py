from file_write import write_csv_file, read_csv_file


class Presenter:
    def __init__(self, view, model):
        self._view = view
        self._model = model

    def add_note(self, name: str, text: str):
        if self._model.add(name, text):
            self._view.print_answer("Заметка добавлена")

    def delete_note(self, numb: int):
        if self._model.delete(numb):
            self._view.print_answer("Заметка удалена")
            return
        self._view.bad_answer()

    def change_text_note(self, numb: int, text: str):
        if self._model.change_text(numb, text):
            self._view.print_answer("Текст заметки изменён")
            return
        self._view.bad_answer()

    def change_name_note(self, numb: int, name: str):
        if self._model.change_name(numb, name):
            self._view.print_answer("Наименование заметки изменено")
            return
        self._view.bad_answer()

    def print_note(self, numb: int):
        res = self._model.print_note(numb)
        if res != "":
            self._view.print_answer(res)
            return
        self._view.bad_answer()

    def print_notebook(self):
        self._view.print_answer(self._model.print_notebook())

    def sort_by_date(self):
        self._view.print_answer(self._model.print_notebook("change_date"))

    def save_file(self, path=""):
        if write_csv_file(_path_file(path), self._model.get_data()):
            self._view.print_answer(f"Файл сохранён по адресу: {_path_file(path)}")
            return
        self._view.print_answer("Файл не сохранён")

    def read_file(self, path=""):
        if read_csv_file(_path_file(path), self._model):
            self._view.print_answer(f"Файл загружен: {_path_file(path)}")
            return
        self._view.print_answer("Файл не загружен")

    def finish(self):
        self._view.finish()


def _path_file(path: str) -> str:
    if path == "":
        return "notebook.csv"
    return path
