from collections import OrderedDict

from previous_code import Light_son

# def build_person(first_name, last_name, age=''):
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# musician = build_person('jimi', 'hendrix', age='27')
# print(musician)
# def info(a, b, age=''):
#     # a=1
#     # b=2
#     print(a + b)
#     if age:
#         age = age + 1
#     return age

xiao_gugu = Light_son(11, 500)
xiao_gugu.applaud()


def great_house(name):
    """none的测试"""
    if name:
        print("yes!")
    else:
        print("No!")


great_house('None')


# def sum(arr):
#     if arr == []:
#         return 0
#     else:
#         number = arr.pop()
#         return number + sum(arr)
#
#
# print(sum([1,2, 3]))

# def sum(arr):
#     if arr == []:
#         return 0
#     else:
#         number = arr.pop()
#         return number + sum(arr)
#     ancer=''
#     for i in arr:
#
#         ancer+=str(1)+'+'
#
#
#
# print(ancer=sum([1, 2, 3]))

def summary(arr):
    if len(arr) == 1:
        print(str(arr[0]) + " = ", end="")
        return arr[0]
    else:
        number = arr.pop(0)
        print(str(number) + " + ", end="")
        return number + summary(arr)


print(summary([19, 0, 6, 2, 3]))

graph = {}
graph["start"] = {}
graph['start']['a'] = 5
graph['start']['b'] = 2
graph['a'] ={}
graph['a']['d'] = 4
graph['a']['c'] = 2
graph['b'] = {}
graph['b']['a'] = 8
graph['b']['c'] = 7
graph['c'] = {}
graph['c']['f'] = 1
graph['d'] = {}
graph['d']['c'] = 6
graph['d']['f'] = 3
graph['f'] = {}

infinity = float('inf')
costs = {}
costs['a'] = 5
costs['b'] = 2
costs['c'] = infinity
costs['d'] = infinity
costs['f'] = infinity

parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['c'] = None
parents['d'] = None
parents['f'] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)
print(costs)