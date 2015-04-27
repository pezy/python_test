# cars number
cars = 100
# a car have 4 space
space_in_a_car = 4.0
# drivers number
drivers = 30
# passengers number
passengers = 90
# the number which car haven't driver
cars_not_driven = cars - drivers
# the number which car have driver
cars_driven = drivers
# the number that total cars can pass people
carpool_capacity = cars_driven * space_in_a_car
# the average of passengers in each car.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "we can transport", carpool_capacity, "people today."
print "we have", passengers, "to carpool today."
print "we need to put about", average_passengers_per_car, "in each car."
