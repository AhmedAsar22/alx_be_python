number = int(input("Enter the size of the pattern"))
for i in number:
    print("i: "+i)
number = int(input("Enter the size of the pattern"))
for i in number:
    print("i: "+i)
num = int(input("Enter the size of the pattern: "))
x = 1
while x <= num:
    for i in range(1, num+1):
        print("*", end="")
    print()
    x +=1
