hairColors = ["Brown", "Blue", "Red", "Blonde", "Black", "Purple"]

# print (hairColors[2])

people = ["Bob Ross", "Kendra", "Liv", "Taylor Swift", "Lil Nas X", "Kat"]

# print(people[1]) + "has:" + (hairColors[1]) + "hair.")

peopleAndColors = ("Bob Ross" : "Brown", "Kendra" : "Blue", "Liv" : "Red",
                    "Taylor Swift" : "Blonde", "Lil Nas X" : "Black",
                    "Kat" : ["Purple", "Blue"])

peopleAndColors.update({"Ed Sheeran" : "Red"})

print(peopleAndColors)

peopleAndColors.pop({"Ed Sheeran" : "Red"})

print(peopleAndColors)

# print("Bob Ross has:")
