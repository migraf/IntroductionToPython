__author__ = "Michael Graf"

from distance_methods import *
from input_reader import *

# Gives the average normalized levhenstein distance of two wordlists
def levenstein_list_normalized(list1,list2):
    leven_sum = 0
    for i in range(len(list1)):
        leven_sum += calc_normalized_L_dist(list1[i],list2[i])

    return leven_sum/len(list1)


# Takes a dictionary of languages and their wordlists, compares  the given language to all
# the other languages in the dictionary
def lstein_list_on_dictionary(dict, language):
    compared_languages = {}
    list1 = dict.get(language)
    for lan in dict:
        list2 = dict.get(lan)
        compared_languages[lan] = levenstein_list_normalized(list1, list2)

    return compared_languages


print lstein_list_on_dictionary(split_file("listss16.txt"), "NAUNA")
