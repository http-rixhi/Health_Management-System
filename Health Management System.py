# Health Management System
"""
A program to manage your daily diets & exercise records with date and time stamps.
"""
n = str(input("Enter Your name: "))
name = n.lower()

i=0
while i<1:
    def getdate():
        import datetime
        return datetime.datetime.now()

    print("What you want to do?")
    print("1. LOG\n2. RETRIEVE")
    x= int(input("Enter Your Choice: "))


    if x==1:    # FOR LOG
        print("What you want to LOG?")
        print("1. DIET \n2. EXERCISE")
        log_choice = int(input("Enter Your Choice: "))

        if log_choice == 1:    # FOR DIET
            f = open(f"{name}diet.txt", "a")
            diet = input("Enter Your Diet: ")
            f.write(f"[{getdate()}]  {diet}\n")
            f.close()

        elif log_choice == 2:    # FOR EXERCISE
            f = open(f"{name}exrc.txt", "a")
            exercise = input("Enter Your Exercise: ")
            f.write(f"[{getdate()}]  {exercise}\n")
            f.close()

        else:
            print("Invalid Choice Inputted.")


    elif x== 2:      # FOR RETRIEVE
        print("What you want to RETRIEVE?")
        print("1. DIET \n2. EXERCISE")
        retrieve_choice = int(input("Enter Your Choice: "))

        if retrieve_choice == 1:    # FOR DIET
            f= open(f"{name}diet.txt")
            diet_logs = f.read()
            print(diet_logs)
            f.close()

        elif retrieve_choice == 2:    # FOR EXERCISE
            f= open(f"{name}exrc.txt")
            exrc_logs = f.read()
            print(exrc_logs)
            f.close()

        else:
            print("Invalid Choice Inputted.")

    else:
        print("Invalid Choice Inputted.")

    print("")
    rep = str(input("Do You Want to Continue (Y/N): "))
    replay = rep.lower()
    if replay == "y":
        i = 0
    elif replay == "n":
        i += 1
    else:
        print("Invalid Choice Inputted.")
        break