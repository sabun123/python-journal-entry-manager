def view_entry():
  print('** View a specific entry')
  selected_entry = input('Which entry would you like to view? ')
  print('')
  with open('journal.txt', 'r') as file:
    for index, line in enumerate(file, start=1):
      if index == int(selected_entry):
        print(line.strip())