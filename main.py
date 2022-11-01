print("List Generator")
print()
print("Please insert a number you want to start with, an ending number, and by how much should it increase.")
i = int(input("Start at:"))
h = int(input("End before:"))
j = int(input("Increment between values:"))
for list in range(i,h,j):
  print(list)