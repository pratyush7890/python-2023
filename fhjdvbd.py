#rows = int(input("Enter the number of rows: "))

#for i in range(rows):
 #   for j in range(i+1):
  #      print("*", end=" ")
    #print()
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    for k in range(i + 1, rows + 1):
        print("**", end=" ")
    print()
