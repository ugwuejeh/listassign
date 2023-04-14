# a program that generates a list of 15 random integers, finds the largest and smallest numbers in the list, and prints them out:


import random
# we used random sample to Generate a list of 15 random integers between 0 and 100, with 15 as tolal numbere of list.
my_list = random.sample(range(0, 100), 15) 
print("List of numbers:", my_list)
# max() is an inbuild function for Finding  the largest number in the list
largest_num = max(my_list) 
print("Largest number in the list:", largest_num)
# min() is an inbuild function for Finding the smallest number in the list
smallest_num = min(my_list) 
print("Smallest number in the list:", smallest_num)

