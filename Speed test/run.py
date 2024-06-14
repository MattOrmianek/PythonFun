""" This will be test for the speed of the code, comparing loops vs recursion """

# pylint: disable=consider-using-f-string,unspecified-encoding,consider-using-with,unused-variable
# pylint: disable=redefined-outer-name,invalid-name
import json
import time

POWER = 100000
NUMBER_OF_RUNS = 10


def loop(list_of_countries):
    """Loops through a list of countries and returns the length of the longest country name"""
    stars = ""
    total_length = 0
    for country in list_of_countries:
        total_length += len(country)
    result = total_length**POWER


def recursive_stars(list_of_countries, index=0, total_length=0):
    """Recursively adds stars to a string until it reaches the length of the longest country name"""
    if index >= len(list_of_countries):
        result = total_length**POWER
        return

    total_length += len(list_of_countries[index])
    recursive_stars(list_of_countries, index + 1, total_length)


def run_muliple_times(n, function, *args):
    """Runs a function n times and returns the average time it took to run"""
    avg_time = 0
    for i in range(n):
        start = time.time()
        function(*args)
        end = time.time()
        avg_time += end - start
    print("POWER '{}'".format(POWER))
    print("\t Average time for function '{}'".format(function.__name__))
    print("\t For {} runs: {:.3f} seconds".format(n, avg_time))
    print("\t For one run: {:.3f} seconds".format(avg_time / n))


if __name__ == "__main__":
    list_of_countires = json.load(open("countries.json"))["countires"]
    run_muliple_times(NUMBER_OF_RUNS, loop, list_of_countires)
    run_muliple_times(NUMBER_OF_RUNS, recursive_stars, list_of_countires)
