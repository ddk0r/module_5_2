class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        title = str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
        return title

my_house1 = House('ЖК Армавирский', 18)
my_house2= House('Домик в деревне', 5)

print(my_house1)
print(my_house2)

print(len(my_house1))
print(len(my_house2))