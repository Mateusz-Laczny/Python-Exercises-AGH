author = "Garus Vakarian"

import math
import random


def fermats_check(number):
    """Program tests each number from 2 to given number with Fermat's little theorem"""

    number_list = [x for x in range(3, number+1)]

    for checked_num in range(4, number + 1):
        counter = 0
        check = True

        while True:
            counter += 1

            random_num = random.randint(2, checked_num - 2)

            if pow(random_num, checked_num - 1, checked_num) != 1:
                check = False

            if counter > 1000:
                break

            if not check:
                number_list.remove(checked_num)
                break

    return number_list


def prime_check(num_list):

    for number in num_list:
        for divider in range(2, int(math.sqrt(number)) + 1):
            if divider != number and number % divider == 0:
                num_list.remove(number)
                break

    return num_list


if __name__ == '__main__':
    print(prime_check(fermats_check(1000)))



