from Notebook_model import Notebook as Notebook
from Presenter import Presenter as Presenter
from view import ConsoleView as ConsoleView


new_console = ConsoleView(Presenter, Notebook)
new_console.start_menu()
