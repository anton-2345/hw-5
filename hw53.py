import random
class Animal:
    def __init__(self, species, size, food, habitat, life_span):
        self.species = species
        self.size = size
        self.food = food
        self.habitat = habitat
        self.life_span = life_span
        self.specific = []

    def add_specific(self, age, satiety, gender):
        spec = {
            'age': age,
            'satiety': satiety,
            'gender': gender
        }
        self.specific.append(spec)

    def show(self):
        return self.specific

    def reproduction(self, n1, n2):
        ani1 = self.specific[n1]
        ani2 = self.specific[n2]
        if ani1['gender'] == ani2['gender']:
            print('impossible')
            return
        if self.habitat == 'water' and ani1['satiety'] > 50 and ani2['satiety'] > 50:
            for i in range(10):
                self.add_specific(0, 23, random.choice(['m', 'f']))
        elif self.habitat == 'air' and ani1['satiety'] > 42 and ani2['satiety'] > 42 and ani1['age'] > 3 and ani2['age'] > 3:
            for i in range(4):
                self.add_specific(0, 64, random.choice(['m', 'f']))
        elif self.habitat == 'land' and ani1['satiety'] > 20 and ani2['satiety'] > 20 and ani1['age'] > 5 and ani2['age'] > 5:
            for i in range(2):
                self.add_specific(0, 73, random.choice(['m', 'f']))

    def time(self, food_amount, all):
        food_new = 0
        food_new = food_amount
        for i in self.specific[:]:
            i['age'] += 1
            if i['age'] >= self.life_span:
                food_new += self.size
                self.specific.remove(i)
            else:
                if self.food == 'plant':
                    if food_new > 0:
                        i['satiety'] = min(i['satiety'] + 26, 100)
                        food_new -= 1
                    else:
                        i['satiety'] = max(0, i['satiety'] - 9)
                else:
                    do_eat = False
                    for another in all.values():
                        if another.food == 'plant' and another != self:
                            for prey in another.specific[:]:
                                if random.random() < 0.5:
                                    i['satiety'] = min(100, i['satiety'] + 53)
                                    another.specific.remove(prey)
                                    do_eat = True
                                    break
                            if do_eat:
                                break
                    if not do_eat:
                        i['satiety'] = max(0, i['satiety'] - 25)
            if i['satiety'] < 10:
                food_new += self.size
                self.specific.remove(i)

        return food_new

class Planet:
    def __init__(self):
        self.animals = {}
        self.food_amount = 10

    def add_species(self, species, size, food, habitat, life_span):
        self.animals[species] = Animal(species, size, food, habitat, life_span)

    def add_specific(self, species, age, satiety, gender):
        if species in self.animals:
            self.animals[species].add_specific(age, satiety, gender)
        else:
            print('impossible')

    def add_food(self, many):
        self.food_amount += many

    def show_specific(self, species):
        if species in self.animals:
            return self.animals[species].show()
        else:
            print('impossible')
            return []

    def simulate_reproduction(self, species, n1, n2):
        if species in self.animals:
            self.animals[species].reproduction(n1, n2)
        else:
            print('impossible')

    def simulate_time(self):
        food_new = 0
        for animal in self.animals.values():
            food_new += animal.time(self.food_amount, self.animals)
        self.food_amount += food_new

    def show_species_info(self):
        for species, animal in self.animals.items():
            print(f" {species}, size: {animal.size}, food: {animal.food}, habitat: {animal.habitat}, life_span: {animal.life_span}")


pl= Planet()

pl.add_species('zebra', 5, 'plant', 'land', 10)
pl.add_species('lion', 8, 'meat', 'land', 12)
pl.add_species('walrus', 8, 'plant', 'water', 20)
pl.add_species('pigeon', 2, 'plant', 'air', 7)
pl.add_species('falcon', 4, 'meat', 'air', 7)
pl.add_species('sparrow', 1, 'plant', 'air', 3)
pl.add_species('mole', 1, 'plant', 'land', 8)
pl.add_species('seal', 6, 'plant', 'water', 10)
pl.add_species('tiger', 9, 'meat', 'land', 12)
pl.add_species('rat', 2, 'plant', 'land', 4)
pl.add_species('polar bear', 10, 'meat', 'water', 10)
pl.add_species('chicken', 3, 'plant', 'land', 2)
print('on this planet you can meet such animals')
pl.show_species_info()
print('do you want to add extra food?')
n = int(input())
pl.add_food(n)
stop = True
while stop == True:
    print('do you want to add some animals?')
    choice = input()
    if choice == 'no':
        stop = False
    else:
        a = input('species')
        b = int(input('age'))
        c = int(input('satiety'))
        d = input('gender')
        pl.add_specific(a, b, c, d)
stop2 = True
while stop2 == True:
    ans = input('do you want to see specific?')
    if ans == 'no':
        stop2 = False
    else:
        sp = input('species')
        print(pl.show_specific(sp))
repr = input('for which species do you want to simulate reproduction?')
pl.simulate_reproduction( repr, 0, 1)
print('after reproduction:', pl.show_specific(repr))
print('time is passing')
pl.simulate_time()
stop3 = True
while stop3 == True:
    ans2 = input('do you want to see specific?')
    if ans2 == 'no':
        stop3 = False
    else:
        sp2 = input('species')
    print('after time simulation:', pl.show_specific(sp2))
