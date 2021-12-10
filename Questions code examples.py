

def login():

    name = str(input("What is your name: ")) 

    if name != str("Enzo"):
        print("Wrong Username")
    else: 
        print("Nice to meet you")

    password = int(input("What is your pin? "))

    if password != int(3011):
        print("This is WRONG")
    else:
            print("Welcome to your diary")
 
    if name and password != True:
        file = open("C:\Work\.pyNewdatabase.txt","rt")
        
def update():
        file = open("C:\Work\.pyNewdatabase.txt","wt")
        file.write(input("What's new:"))
 


def logout():
    
    close = str(input("Would you like to stop? "))
    if close != str("Yes") or str("yes"):
        file = open("C:\Work\.pyNewdatabase.txt","rt")
        file.close()
    else:
        update()

 
    
login()
update()
logout()




