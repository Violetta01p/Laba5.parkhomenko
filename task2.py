import random
a = random.randint(1,50)




b = int(input("Enter number 1 to 50: "))
difference = abs(a - b)
if difference ==0 :
   print("Congratulations! You guessed the number!")


elif difference <=3 :
   print("Very close.")
elif difference <10:
   print("Close .")
else:
   print("Far. ")
