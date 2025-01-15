class House:
    def __init__(self, name, number_of_floors):
        self.name = name # название ЖК
        self.number_of_floors = number_of_floors # кол-во этажей в доме

    def go_to(self, new_floor):
         if new_floor > self.number_of_floors or new_floor < 1:
             print('Такого этажа не существует')
         else:
             for floor in range(1, new_floor + 1):
                 print(floor)


        # if 1 <= new_floor <= self.number_of_floors:
        #     for floor in range(1, new_floor + 1):
        #         print(floor)
        # else:
        #     print("Такого этажа не существует")

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)