#I made this file because I need to work on my understanding of the Try/Except commands

def IsInt(UserInput):
    try:
        UserInput = int(UserInput)
        return True
    except ValueError:
        print ("This is not an integer")
        main()

def main():
    UI=input("Enter a number please: ")
    if IsInt(UI)==True:
        print ("Wow good job you entered an integer")
    else: 
        ("What, did you do?")

main()
