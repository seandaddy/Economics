import numpy as np

number_of_agents = 1000
number_of_goods = 100

values = np.random.normal(loc=100, scale=20, size=number_of_agents)
valuations = np.sort(values)[::-1]
print("{0:.2f}".format(valuations[number_of_goods]))

max_welfare = sum(valuations[:100])
print(max_welfare)
