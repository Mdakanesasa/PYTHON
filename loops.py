print("WELCOME TO ISG")
acc= input("do you have a account")
if acc== "yes":
    print("please log in:\n")
    username= input("username: ")
    password=input("enter passowrd: ")
    count = 2
    while count > 0:
        if password=="6666":
           print("welcome")
           break
        else:
            retry=input("retry")
            count = 2
            
            count-=1
            if retry==password:
               print("welcome")
            else:
                print("login failed")
            break
            
elif acc=="no":    
    name = input("first name: ")
    surname = input("surname: ")
    email=input("email: ")
    contact=input("phone number: ")
    password=input("enter password")
    print("CONFIRM PASSWORD")
    password2=input("confrim password")
    if password==password2:
        print("account confirmed")
        print("registration successful")         
        print("welcome to your child's profile, what would you like to view")
        print("\n1.behaviour\n2.accademics\n3.sport activities\n4.homework")
    else:
        select= input("select any: ")
        if select=="2":
                print("promoted to the next grade")
                select = input(":")
        elif select=="3":
                 print("soccer mondays")
                 print("netball tuesdays")
                 print("rygby friday")              
        elif  select=="1":
                print("fast leaner")
                print("calm")
                print("good accademics")           
        elif  select=="4":
                print("research about eskom")

print("deposit for next year")    
print("ADD CARD PAYMENT")
no=input("enter card number")
accno=input("enter account number")
ccv=input("enter ccv number")
date=input("enter expiry date")
otp=input("enter OTP pin")
if otp=="5555":
   print("card edded")
else:
    print("try the otp pin again")

