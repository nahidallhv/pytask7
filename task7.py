import random
import math

def kvHesablama():
    num = []
    for _ in range(5):
        num.append(random.randint(20, 50))
    print("Random ededler : ",num)
    for i in range(len(num)):
        if num[i] % 2 == 0:
            num[i] = math.pow(num[i], 2)
    print("Cut eded kvadrati : ", num)
kvHesablama()
