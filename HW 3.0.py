x = int(input("Введіть перше число(x): "))
y = int(input("Введіть друге число(y): "))
if y > 0 and x > 0:
    print("Число знаходиться в першій чверті")
elif y > 0 and x < 0:
    print("Число знаходиться в друга чверті")
if y < 0 and x < 0:
    print("Число знаходиться в третя чверті")
elif y < 0 and x > 0 :
    print("Число знаходиться в четвертій чверті")
q = str(input("Бажаєте продовжити? (y/n)"))
while (q) == "y": 
    x = int(input("Введіть перше число(x): "))
    y = int(input("Введіть друге число(y): "))
    if y > 0 and x > 0:
        print("Число знаходиться в першій чверті")
    elif y > 0 and x < 0:
        print("Число знаходиться в друга чверті")
    if y < 0 and x < 0:
        print("Число знаходиться в третя чверті")
    elif y < 0 and x > 0 :
        print("Число знаходиться в четвертій чверті")
while (q) == "n":
    print("До зустрічі ")
