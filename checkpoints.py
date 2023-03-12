#Answer1
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)
#Answer2
n = int(input("Enter a number: "))
result = n + n*n + n*n*n
print(result)
#Answer3
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
#Answer4
for num in range(2000, 3201):
    if num % 7 == 0 and num % 5 != 0:
        print(num, end=" ")    
#Answer5
num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print(factorial)
#Answer6
string = input("Enter a string: ")
result = ""
for i in range(len(string)):
    if i % 2 == 0:
        result += string[i]
print(result)
#Answer7
price = int(input("Enter the price: "))
if price >= 500:
    discounted_price = price / 2
elif price >= 200 and price < 500:
    discounted_price = price * 0.7
else:
    discounted_price = price * 0.9
print("Discounted price:", discounted_price)
