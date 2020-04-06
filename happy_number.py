number = input()

temp = 0

while (int(number) > 1):
    for i in number:
        temp = temp + int(i)**2

    number = str(temp)
    temp = 0
    print(number)

#print(number)

if(number == "1"):
    print("happy")

