import timeit
import math

author = "John Sheppard"

TIMES = 10


def test_time(f):
    print(timeit.timeit(f, number=TIMES) / TIMES)


def naive_check(number):
    """Method finds the prime numbers form 2 to number, by checking every number between"""

    # List of numbers to check
    num_list = [x for x in range(2, (number+1))]

    for num in range(2, number+1):
        # Loop checks whether any number from 2 to num - 1 is a factor of num
        for divider in range(2, num):
            if divider != num and num % divider == 0:
                num_list.remove(num)
                break

    return num_list


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

    # To get the primes we need to add 2 to each index from the check_list, if the list value wtih this index is True
    number_list = [index + 2 for index in range(0, len(check_list) - 1) if check_list[index]]

    return number_list


if __name__ == '__main__':

    # test_time(lambda: naive_check(naive_check(1000)))
    test_time(lambda: efficient_check(1000))
    test_time(lambda: sieve_check(40))
    print(sieve_check(40))
    print(efficient_check(40))
    print(naive_check(40))
