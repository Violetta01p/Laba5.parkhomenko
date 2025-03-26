import random


def get_random_color():
   colors = ["red", "orange", "yellow", "green", "blue", "purple"]
   return random.choice(colors)


def get_color_hint(color):
   warm_colors = ["red", "orange", "yellow"]
   cold_colors = ["blue", "green", "purple"]


   if color in warm_colors:
       return "warm"
   elif color in cold_colors:
       return "cold"


def main():
   secret_color = get_random_color()
   attempts = 0


   print("I have chosen a random color. Try to guess it!")
   print("The colors are: red, orange, yellow, green, blue, purple.")


   while attempts != 3:


       user_guess = input("Enter your guess: ").lower()




       if user_guess not in ["red", "orange", "yellow", "green", "blue", "purple"]:
           print("Invalid color! Please choose from red, orange, yellow, green, blue, or purple.")
           continue


       attempts += 1


       if user_guess == secret_color:
           print(f"Congratulations! You guessed the color correctly in {attempts} attempts!")
           break
       hint = get_color_hint(secret_color)
