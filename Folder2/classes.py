def Dog():
    hungry = False
    breed = ""
    dirty = False
    friends = 0

    def play(self):
        self.hungry = True
        self.dirty = True
        self.friends += 1

    def eat(self):
        self.hungry = False

    def bathe(self):
        self.dirty = False

    def walk(self):
        self.hungry = False
#-------------------------------------
ginger_bob_ross = Dog()

ginger_bob_ross.breed = "Husky"
ginger_bob_ross.play()
ginger_bob_ross.eat()

print("Ginger Bob Ross:")
print("Hungry?" + str(ginger_bob_ross.hungry))
print("Breed:" + str(ginger_bob_ross.breed))
print("Dirty?" + str(ginger_bob_ross.dirty))
print("Friends:" + str(ginger_bob_ross.friends))
