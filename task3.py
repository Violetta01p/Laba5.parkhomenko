import random
code = random.randint(1, 20)




attempts = 3


while attempts > 0:


   guess = int(input("Guess the number (on 1 to 20): "))


   if guess == code:
       print("Congratules! You guessed code!")
       break
   else:
       attempts -= 1
       print("Wrong. Attempts left:", attempts)


if attempts == 0:
   print("Game over. Correct code was:", code)
