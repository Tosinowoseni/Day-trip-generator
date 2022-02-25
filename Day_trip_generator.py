# Day Trip Generator
import random

#(5 points): As a developer, I want to store my destinations, restauarants, mode of transportation, and entertainments in their own separate lists 
#list of destinations
destinations = ['london', 'New York', 'Paris', 'Italy']
print(destinations)

#mixed list
random_list = ['london', 'New York', 'Paris', 'Italy']

destination1 =  random.choice(destinations)
print(destination1)

restauarants = ['The palomar', 'Mastros steakhouse', 'Parc', 'Osteria']
print(restauarants)

#mixed list
random_list = ['The palomar', 'Mastros steakhouse', 'Parc', 'Osteria']

restaurant = random.choice(restauarants)
print(restaurant)

transportations = ['Motorcycle', 'Bus', 'Car', 'Airplane']
print(transportations)

#mixed list
random_list = ['Motorcycle', 'Bus', 'Car', 'Airplane']

transportation = random.choice(transportations)
print(transportation)

Entertainments = ['Concerts', 'Movie theatre', 'Race track', 'Clubbing']
print(Entertainments)

#mixed list
random_list = ['Concerts', 'Movie theatre', 'Race track', 'Clubbing']

Entertainment = random.choice(Entertainments)
print(Entertainment)

destination = random.choice(destinations)
print(destination)

restaurant = random.choice(restauarants)
print(restaurant)

transportation = random.choice(transportations)
print(transportation)

Entertainment = random.choice(Entertainments)
print(Entertainment)