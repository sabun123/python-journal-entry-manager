def add_entry():
  print('** Add a new entry')
  new_entry = input('What would you like to add to your journal today? ')
  with open('journal.txt', 'a') as file:
    file.write(new_entry + '\n')