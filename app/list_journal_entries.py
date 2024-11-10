def list_entries():
  print('** View all entries')
  print('')
  print('------------')
  with open('journal.txt', 'r') as file:
    for index, line in enumerate(file, start=1):
      print(f'{index}. {line.strip()}', end='\n')
  print('')
  print('------------')
  print('')