"""Write a program to sort stack"""

from Stack import stack
from random import randint

main = stack(20)

temp = stack(20)


for i in range(15):
    main.push(randint(1,20))

main.display()

def sortStackHelper(stk, temp):

    while(not stk.isEmpty()):
        min = stk.pop()
        while


sortStackHelper(main, temp)