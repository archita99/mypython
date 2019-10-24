i = 3
while i >0:
    un = input("Username : ") 
    ps = input("Password : ")
    if (un == "Bhaluu" and ps == "bUchii123"):
        print("Login Successful")
        print("Welcome "+un)
        break
    else:
        print("Wrong username and password combination!!")
        i = i - 1
        if i!= 0:
            print("You have "+str(i)+" attempts left")
        else:
            print("No. of attempts has been exceeded. Program is terminating...")
        
    
