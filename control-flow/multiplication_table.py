number = int(input("Enter a number to see its multiplication table: "))
for num in range(1 , 11):
    mult = num *number
    print(f"{number} * {num} = {mult}")