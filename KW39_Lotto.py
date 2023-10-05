import random
import matplotlib.pyplot as plt

def lotto_draw(maxNum):
    numbers = list(range(1, maxNum+1))
    i = 1
    while i <= 6:
        x = random.randint(0, maxNum-i)
        numbers[maxNum-i], numbers[x] = numbers[x], numbers[maxNum-i]
        i += 1
    return numbers[39:maxNum]


def refresh_stats(dict,draw):
    for x in dict:
        if x in draw:
            dict[x] += 1
    return dict,draw


if __name__ == '__main__':
    maxNum = 45
    i = 0
    dict = {x: 0 for x in range(1, maxNum+1)}
    while i<1000:
        dict,output = refresh_stats(dict,lotto_draw(maxNum))
        print(output)
        i += 1

    for x in dict:
        plt.bar(x,dict[x])
    plt.show()



