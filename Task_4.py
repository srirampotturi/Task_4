class Temperature:
    def ftc(self,a):
        c=(a-32)*5/9
        return c
    def ctf(self,a):
        f=(a*9/5)+32
        return f
temp=Temperature()
while True:
    print("1.Fahrenheit to celsius\n2.Celsius to Fahrenheit")
    ch=int(input("Enter your Choice: "))
    
    if ch==1:
        a=float(input("Enter Fahrenheit Degrees: "))
        print(temp.ftc(a))
    elif ch==2:
        a=float(input("Enter Celsius Degrees: "))
        print(temp.ctf(a))
    else:
        print("invalid Choice")
        break
    c=input("Do you want to caonyinue?(Yes/No): ")
    if c=="Yes" or c=="yes":
        continue
    else:
        print("Thanks for using")
        break