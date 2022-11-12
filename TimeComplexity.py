import random
from time import *

def prefix_average(list0):
    n = len(list0)
    averageList = [None] * n

    for j in range(n):
        total = 0
        for i in range(j+1):
            total = total + list0[i]
        averageList[j] = total/(j+1)

    return averageList


def prefix_average_with_sum(list0):
    n = len(list0)
    averageList = [None] * n

    for j in range(n):
        averageList[j] = sum(list0[0:j+1])/(j+1)

    return averageList


def prefix_average_with_running_average(list0):
    n = len(list0)
    averageList = [None] * n
    total = 0

    for j in range(n):
        total = total + list0[j]
        averageList[j] = total/(j+1)

    return averageList


def create_random_list_with_n_element(n):
    random_list = []
    for i in range(n):
        item = random.randint(0,100)
        random_list.append(item)
    return random_list

def try_all_solutions(n):
    list = create_random_list_with_n_element(n)

    start_time = time()
    prefix_average(list)
    end_time = time()
    elapsed = end_time - start_time
    print("The function prefix_average took {} seconds to finish for {} elemented list".format(elapsed , n))

    start_time = time()
    prefix_average_with_sum(list)
    end_time = time()
    elapsed = end_time - start_time
    print("The function prefix_average_with_sum took {} seconds to finish for {} elemented list".format(elapsed, n))

    start_time = time()
    prefix_average_with_running_average(list)
    end_time = time()
    elapsed = end_time - start_time
    print("The prefix_average_with_running_average took {} seconds to finish for {} elemented list".format(elapsed, n))

    print("__________________________________________________________________________________________________________________________")

def main():
   try_all_solutions(1)
   try_all_solutions(10)
   try_all_solutions(100)
   try_all_solutions(1000)
   try_all_solutions(10000)
   try_all_solutions(100000)
   try_all_solutions(1000000)


if __name__ == "__main__":
    main()