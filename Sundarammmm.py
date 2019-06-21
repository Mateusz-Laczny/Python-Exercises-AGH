author = "Modrin Solus"

import math
import timeit

TIMES = 10


def test_time(f):
    print(timeit.timeit(f, number=TIMES) / TIMES)


def efficient_check(number):
    """Method finds the prime numbers form 2 to number, by checking every number between"""

    # List of numbers to check
    num_list = [x for x in range(2, number + 1)]

    for num in range(2, number+1):
        # Loop checks whether any number from 2 to square root of num plus one is a factor of num
        for divider in range(2, int(math.sqrt(num)) + 1):
            if divider != num and num % divider == 0:
                num_list.remove(num)
                break

    return num_list


def sieve_check(number):
    """Method finds the prime numbers from 2 to number, with usage of the sieve of Eratosthenes"""

    # Filling list with True values
    check_list = [True for x in range(2, number + 1)]

    for num in range(2, number + 1):
        # Num - 2 because indexes start with 0
        if check_list[num - 2]:

            # First multiple is the number squared
            multiple = num**2

            # Checking all multiples less or equal to number
            while multiple <= number:
                check_list[multiple - 2] = False

                # Finding the next multiple
                multiple += num

    # To get the primes we need to add 2 to each index from the check_list, if the list value with this index is True
    number_list = [index + 2 for index in range(0, len(check_list) - 1) if check_list[index]]

    return number_list


def sundaram_check(number):
    """Method finds the prime numbers from 2 to number, with usage of the sieve of Sundaram"""

    new_number = int((number-2)/2)

    # Filling list with True values
    check_list = [True for x in range(new_number+2)]

    for num_i in range(1, new_number+1):
        num_j = num_i

        while True:

            if (num_j + num_i + 2*num_j*num_i) > new_number:
                break

            check_list[(num_j + num_i + 2*num_j*num_i)] = False
            num_j += 1

    # To get the primes we need to add 2 to each index from the check_list, if the list value with this index is True
    number_list = [2*index + 1 for index in range(0, len(check_list)) if check_list[index]]

    if number >= 2:
        number_list.insert(1, 2)

    return number_list


if __name__ == '__main__':
    print("Sundaram: %".format(test_time(lambda: sundaram_check(100000))))
    print("Erastotenes: %".format(test_time(lambda: sieve_check(100000))))
    print("Naive with upgrades: %".format(test_time(lambda: efficient_check(100000))))

