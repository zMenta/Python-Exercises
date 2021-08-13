

#Functions

def helping():
    """
    ->Function creating a help experience. Type on the screen what you want to search for help and write "exit" to exit the helping function.
    """
    #c = color
    c = {
        "normal": "\033[0;0;0m",
        "red": "\033[0;31m",
        "blueBg": "\033[1;0;44m",
        "neg": "\033[7m"
    }

    opt = "" #opt = option 
    while opt != "exit":
        opt = input("Type what you want to search for help: ")
        if opt == "exit":
            break
        try:
            # print(f"{c['blueBg']}Accessing help for '{opt}' {c['normal']}")
            print(c['neg'])
            help(opt)
            print(c['normal'])
        except:
            print("No help found.")


#Main Body
helping()
print("\033[1;31mHelping terminated!\033[0;0;0m")
