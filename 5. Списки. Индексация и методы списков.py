food = ['apple', 'coconut', 'banana']
food.append('teteva')
print(food)
food.extend(['string', 2])
print(food)
food.remove('apple')
print(food)
print('coconut' not in food)
print(food[0:2:2])