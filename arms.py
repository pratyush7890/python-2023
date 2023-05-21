

num = int(input("Enter a number: "))


num_str = str(num)
n = len(num_str)


sum = 0
for digit in num_str:
    sum += int(digit) ** n

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


