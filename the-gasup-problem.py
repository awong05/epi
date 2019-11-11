"""
In the gasup problem, a number of cities are arranged on a circular road. You
need to visit all the cities and come back to the starting city. A certain
amount of gas is available at each city. The amount of gas summed up over all
cities is equal to the amount of gas required to go around the road once. Your
gas tank has unlimited capacity. Call a city ample if you can begin at that city
with an empty tank, refill at it, then travel through all the remaining cities,
refilling at each, and return to the ample city, without running out of gas at
any point. See Figure 17.2 for an example.

Given an instance of the gasup problem, how would you efficiently compute an
ample city? You can assume that there exists an ample city.

Hint: Think about starting with more than enough gas to complete the circuit
without gassing up. Track the amount of gas as you perform the circuit, gassing
up at each city.

NOTES:
- Let z be a city where the amount of gas in the tank before we refuel at that
city is minimum.
- Since we never have less gas than we started with at z, and when we return to
z we have 0 gas (since it's given that the total amount of gas is just enough to
complete the traversal) it means we can complete the journey without running out
of gas.

"""

from collections import namedtuple


MPG = 20


def find_ample_city(gallons, distances):
    """
    Space complexity: O(1)
    Time complexity: O(n)

    """

    remaining_gallons = 0
    CityAndRemainingGas = namedtuple(
        'CityAndRemainingGas',
        ('city', 'remaining_gallons')
    )
    city_remaining_gallons_pair = CityAndRemainingGas(0, 0)
    num_cities = len(gallons)
    for i in range(1, num_cities):
        remaining_gallons += gallons[i - 1] - distances[i - 1] // MPG
        if remaining_gallons < city_remaining_gallons_pair.remaining_gallons:
            city_remaining_gallons_pair = CityAndRemainingGas(
                i, remaining_gallons
            )
    return city_remaining_gallons_pair.city
