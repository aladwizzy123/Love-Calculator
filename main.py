
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# coginate name
combinedname = name1 + name2
t = combinedname.count("t")
r = combinedname.count("r")
u = combinedname.count("u")
e = combinedname.count("e")
total = t+r+u+e

l = combinedname.count("l")
o = combinedname.count("o")
v = combinedname.count("v")
e = combinedname.count("e")
total1 = l+o+v+e

total_score = str(total)+str(total1)

if 10 > int(total_score) > 90:
  print(f"Your score is {total_score}, you go together like coke and mentos.")
elif 40<=int(total_score) <= 50:
  print(f"Your score is {total_score}, you are alright together.")
else:
  print(f"Your score is {total_score}.")