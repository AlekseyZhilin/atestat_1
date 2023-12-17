from datetime import datetime


class Note:
    numb = 0

    def __init__(self, name: str, text: str):
        Note.numb += 1

        self._id = Note.numb
        self._name = name
        self._text = text
        self._crete_date = _set_date_time()
        self._change_date = self._crete_date

    @property
    def name(self):
        return self._name

    @property
    def text(self):
        return self._text

    @property
    def id(self):
        return self._id

    @name.setter
    def name(self, name):
        self._name = name
        self._change_date = _set_date_time()

    @text.setter
    def text(self, text):
        self._text = text
        self._change_date = _set_date_time()

    @property
    def crete_date(self):
        return self._crete_date

    @property
    def change_date(self):
        return self._change_date

    def get_note(self) -> list:
        return [self.id, self.name, self.text, self.crete_date, self.change_date]

    def set_param_date(self, create_date, change_date):
        self._crete_date = _str_to_date(create_date)
        self._change_date = _str_to_date(change_date)

    def __str__(self):
        return (f"{self._id})...тема: {self._name}\n"
                f"текст: {self._text}\n"
                f"дата создания:       {_set_date_format(self.crete_date)}\n"
                f"последнее изменение: {_set_date_format(self._change_date)}")

    def __eq__(self, other):
        if isinstance(other, Note):
            return self.id == other.id
        raise NotImplemented

    def __hash__(self):
        return self.id

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if isinstance(other, Note):
            return self.id < other.id
        raise NotImplemented


class Notebook:
    def __init__(self):
        self._note_book = dict()

    def add(self, name: str, text: str, create_date=None, change_date=None) -> bool:
        note = make_note(name, text)
        if create_date is not None and change_date is not None:
            note.set_param_date(create_date, change_date)
        self._note_book[note.id] = note
        return True

    def delete(self, numb: int) -> bool:
        if self._note_book.get(numb) is None:
            return False
        self._note_book.pop(numb)
        return True

    def change_text(self, numb: int, text: str) -> bool:
        elem = self._note_book.get(numb)
        if elem is None:
            return False
        elem.text = text
        return True

    def change_name(self, numb: int, text: str) -> bool:
        elem = self._note_book.get(numb)
        if elem is None:
            return False
        elem.name = text
        return True

    def print_notebook(self, sort=id) -> str:
        sort_func = _sort_id
        if sort == "change_date":
            sort_func = _sort_change_date

        res = _header_table("Список заметок:\n")
        for elem in sorted(self._note_book.values(), key=sort_func):
            res = _elem_to_str(res, elem)

        return res.rstrip()

    def print_note(self, numb: int):
        res = ""
        elem = self._note_book.get(numb)
        if elem is not None:
            res = _header_table("Выбранная заметка:\n")
            res = _elem_to_str(res, elem)

        return res.rstrip()

    def get_data(self):
        return self._note_book.values()

    def write_notes(self, notes: list):
        if len(notes) > 0:
            self._note_book.clear()
            Note.numb = 0
        for el in notes:
            self.add(el[1], el[2], el[3], el[4])


def _header_table(header: str):
    header += _table()
    return header


def _elem_to_str(begin_str: str, elem) -> str:
    begin_str += str(elem)
    begin_str += '\n'
    begin_str += _table()
    return begin_str


def _sort_id(note: Note):
    return note.id


def _sort_change_date(note: Note):
    return note.change_date


def _table():
    numb = 41
    return "-" * numb + '\n'


def _set_date_time() -> datetime:
    return datetime.now()


def _set_date_format(set_date: datetime) -> str:
    return set_date.strftime("%d.%m.%Y, %H:%M:%S")


def _str_to_date(str_date_str: str) -> datetime:
    # return datetime.strptime(str_date_str, "%Y-%m-%d %H:%M:%S")
    return datetime.fromisoformat(str_date_str)


def make_note(name: str, text: str):
    return Note(name, text)
