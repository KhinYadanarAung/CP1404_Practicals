import random

def main():
    population = 1000
    BIRTH_LOW_RATE = 0.1
    BIRTH_HIGH_RATE = 0.2
    DIE_LOW_RATE = 0.05
    DIE_HIGH_RATE = 0.25
    born = 0.0
    for year in range (10):
        born = int(population * random.uniform(BIRTH_LOW_RATE,BIRTH_HIGH_RATE))
        died = int(population * random.uniform(DIE_LOW_RATE, DIE_HIGH_RATE))
        population = population + born - died
        print("Year",year+1)
        print("*****")
        print("{} gophers were born. {} died.".format(born,died))
        print("Population: ",population)
        print()


main()