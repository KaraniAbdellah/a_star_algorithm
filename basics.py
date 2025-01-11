# lists & functions
num = [1, 2, 3, 4]
nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(num)
print(nums)
num = nums.pop(1)
num.reverse()
print(num) # [6, 5, 4]


# Dictionary
info = {
    0: "zero",
    "name" : "Abdellah",
    "LastName": "Karani",
    "age": 19, 
    "age": 20,
    "Check": True,
    "Favorite": ["Tomatoes", "Orange", "Apple"]
}
print(info["name"])
print(info.get("fname", "no key name here"))

info.update({'name': 'ahmed'})
info.pop('name')

print(info.keys())
print(info.values())



# tuples
# i can not change the tupes after affectation
print("-------------------")
coordinates = (1, 2)
# coordinates[0] = 10 # not support iteem assignement
print(coordinates)


# Generator Express
'''
    use () for use generators --> we create just a generate object
    to generate next item from this object use next()
        next(): generate item from sequence
'''
print("-------------------")
my_list = [x for x in range(1, 3)]
my_generator = (x for x in range(1, 10))

print(my_list) # [1, 2]
print(my_generator) # just address --> we store anything

print(next(my_generator)) # 1
print(next(my_generator)) # 2

for item in my_generator:
    print(item)









