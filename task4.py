import random


def generate_pin():
   return str(random.randint(1000, 9999))


def count_correct_digits(secret_pin, user_guess):
   correct_count = 0
   for i in range(4):
       if secret_pin[i] == user_guess[i]:
           correct_count += 1
   return correct_count


def main():
   secret_pin = generate_pin()
   print("I have generated a random 4-digit PIN. Try to guess it!")


   for attempts in range(1, 6):
       user_guess = input("Enter your PIN: ")


     
       if len(user_guess) != 4 or not user_guess.isdigit():
           print("Invalid format! Please enter exactly 4 digits.")
           continue




       if user_guess == secret_pin:
           print(f"Congratulations! You guessed the PIN in {attempts} attempts!")
           break


       correct_digits = count_correct_digits(secret_pin, user_guess)
       print(f"Incorrect. Correct digits in the correct positions: {correct_digits}.")


   else:
       print(f"Attempts are over. The secret PIN was: {secret_pin}.")


if __name__ == "__main__":
   main()
