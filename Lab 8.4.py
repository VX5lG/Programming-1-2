# Axel
# Period 4
# 11/20/2015

# lab 8.4

# get estimated population

year = int(input)
secYear = 60*60*24*365
birthYear = secYear/7
deathYear = secYear/13
immYear = secYear/35
populatoin = 307357870
population += birthYear*year
population += immYear*year

# print
print (population)

