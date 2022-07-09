n = int(input("Enter the value of n : "))
sum = 0
if not n:
    print("Series Not Defined")
else:
    for i in range(1, n + 1):
        sum = sum + (pow(i, i) / i)

print(f"Sum of the series for {n} values = {sum}")