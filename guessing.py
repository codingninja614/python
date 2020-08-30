import random
print("NUMBER GUESSING GAME")
number=random.randint(1,9)
probability=0
print("Guess a number (between 1 and 9):")
while probability<5:
  probability=int(input())
  if probability==number:
      print("Congratulations YOU WON! :))")
      break
  elif probability<number:
      print("PLEASE GUESS A NUMBER HIGHER THAN:",probability)
  else:
      print("GUESS A NUMBER LOWER THAN",probability)
  if not probability<5:
    print("YOU LOSE!!!. THE NUMBER IS",number)
