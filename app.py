from app.greet import greet
from app.display_options import display_options
from app.list_journal_entries import list_entries
from app.add_journal_entry import add_entry
from app.delete_journal_entry import delete_entry
from app.view_journal_entry import view_entry

greet()

while True:
  display_options()
  selected_command = input('What would you like to do?: ')

  match selected_command:
    case '1':
      add_entry()
    case '2':
      list_entries()
    case '3':
      view_entry()
    case '4':
      delete_entry()
    case '5':
      print('Exiting the app...')
      print('See you again!')
      quit()
    case _:
      print('Invalid Command')