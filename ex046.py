#Contagem regressiva

from time import sleep
from random import randint

colors = {
     0: "\033[1;31m",
     1: "\033[1;32m",
     2: "\033[1;33m",
     3: "\033[1;34m",
     4: "\033[1;35m",
     5: "\033[1;36m",
     6: "\033[1;37m"
}

for c in range(10,-1, -1):
    print("{}{}".format(colors[randint(0,6)], c))
    sleep(1)
print("Nuclear Warhead launching!!!")