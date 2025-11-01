volume = 17

def salute(name='User'):
  print(f'Hello {name}!')
  #print('Let\'s learn some Python together.')


people = ['Alice', 'Bob', 'Charlie']

for name in people:
  salute(name)

for i in range(1, 4):
  print(people[i-1])

def volume():
  # Change the volume if it's too loud or too quiet
  if volume < 20:
      volume = 50
      print("That's better!")
      print("It's kinda quiet.")
  elif 20 <= volume < 40:
      print("It's nice for background music")
  elif 40 <= volume < 60:
      print("Perfect, I can hear all the details")
  elif 60 <= volume < 80:
      print("Nice for parties")
  elif 80 <= volume < 100:
      print("A bit loud!")
  else:
      print("My ears are hurting! :(")
