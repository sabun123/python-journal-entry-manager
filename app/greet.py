import datetime

def greet():
  now = datetime.datetime.now()
  print('')
  print('*-----------------------------------------------*')
  print('welcome to the Python Journal Manager Program!')
  print('Time: ', now.strftime('%H:%M %p'))
  print('Date: ', now.strftime('%d %b %Y'))
  print('')
  print('')