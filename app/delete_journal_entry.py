def delete_entry():
  print('** Delete an entry')
  print('')
  entry_to_delete = input('Which entry would you like to delete? ')

  with open('journal.txt', 'r') as file:
    lines = file.readlines()
    del lines[int(entry_to_delete) - 1]
  
  with open('journal.txt', 'w') as file:
    file.writelines(lines)
