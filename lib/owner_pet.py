class Pet():
    PET_TYPES = [
        "dog",
        "cat",
        "rodent",
        "bird",
        "reptile",
        "exotic"
    ]

    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise Exception("Invalid pet type")   
    pass

class Owner():
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet")
        pet.owner = self
        
    def get_sorted_pets(self):
        return sorted(Pet.all, key=lambda x: x.name)
    
    def __str__(self):
        return f"{self.name} has {self._pets} pets"
    
    def __repr__(self):
        return f"{self.name} has {self._pets} pets"
    pass

# tim = Owner("Tim")
# rio = Pet("Rio", "dog", tim)
# bailey = Pet("Biley", "dog", tim)
# tim.add_pet(rio)
# tim.add_pet(bailey)
# rachel = Owner("Rachel")
# jim = Pet("Jim", "dog", rachel)
# rachel.add_pet(jim)

# print(tim.pets())
# print(rachel.pets())
# print(tim.get_sorted_pets())