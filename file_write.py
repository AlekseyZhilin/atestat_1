import csv


def write_csv_file(path: str, data_list: list) -> bool:
    fields = ["_id", "_name", "_text", "_crete_date", "_change_date"]
    #TODO: предусмотреть запись заголовка
    rows = []
    for elem in data_list:
        rows.append(elem.get_note())

    try:
        with open(path, mode="w", newline="") as file:
            write_csv = csv.writer(file, delimiter=';')
            # write_csv.writerow(fields)
            write_csv.writerows(rows)
    except IOError as err:
        return False

    return True


def read_csv_file(path: str, notebook) -> bool:
    notes = []

    try:
        with open(path, mode="r", newline="") as file:
            rows_csv_file = csv.reader(file, delimiter=';')
            for row in rows_csv_file:
                notes.append(row)
            notebook.write_notes(notes)
    except IOError as err:
        return False

    return True






