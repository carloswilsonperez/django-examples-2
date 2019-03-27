
# Function with default arguments

def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2

def population_density(population, land_area):
    """Calculate the population density of an area.

    INPUT:
    population: int. The population of that area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms
    of square km or square miles the function will return a density in those units.

    OUTPUT:
    population_density: population / land_area. The population density of a particular area.
    """
    return population / land_area

# Lambda Expressions --> Used to create anonymous functions
# With a lambda expression, this function:

def multiply(x, y):
    return x * y

# can be reduced to:

multiply = lambda x, y: x * y

# The map method

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)


# Filter method
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)

# We can replace both with lambda functions:

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)
