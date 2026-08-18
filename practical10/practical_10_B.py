import random as r 

computer = r.randint(1,50)
attempts = 7

while True:

  if attempts == 0:
    print("Attempts over, loss")
    print("Computer Chose: ", computer)
    break
  guess = int(input("Guess: "))
  if guess == computer:
    print("Won! ")
    break
  elif guess > computer:
    print("Try lower /n")
    print(attempts, "attempts remaining")
  else:
    print("Try higher /n")
    print(attempts, "attempts remaining")
    
