'''
Task: you have a listof all ahoes in your small store [model, size]
sort and print list by model and size

shoes = [['B', 0], ['A', 8], ['A', 7], ['C', 9], ['A', 0], ['B', 7], ['C', 8], ['B', 8]]

*can you also sort by first size and then model

'''

shoes = [['B', 0], ['A', 8], ['A', 7], ['C', 9], ['A', 0], ['B', 7], ['C', 8], ['B', 8]]

shoes.sort(key = lambda x : (x[0], x[1]))

#print shoes[model, size]
print("Sorted shoes:")
for i in shoes:
    print(*i, sep="-")