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






