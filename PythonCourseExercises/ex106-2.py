#c = color
c = {
    "normal": "\033[0;0;0m",
    "red": "\033[0;31m",
    "blue": "\033[1;0;44m",
    "neg": "\033[7m",
    "green": "\033[0;30;42m"
}

#hel = help
def hel(msg):
    from time import sleep
    title("Accessing the help system.",'blue')
    print(c['neg'])
    help(msg)
    print(c["normal"])
    sleep(0.5)

def title(msg, color="normal"):
    """
    -> creates a title. With optional color.

    Color must be implemented as a c dictionary/tuple or list.
    """
    size = len(msg) + 4
    print(c[color],)
    print("="*size)
    print(f"  {msg}")
    print("="*size)
    print("\033[m")


#Main Body

#opt = option
opt = ""

while True:
    title("Help System",'green')
    opt = input("Function or library: ")
    if opt == "exit":
        break
    else:
        hel(opt)

