from distance_methods import *

# Gives the average normalized levhenstein distance of two wordlists
def levenstein_list_normalized(list1,list2):
    leven_sum = 0
    for i in list1.length:
        leven_sum += calc_normalized_L_dist(list1[i],list2[i])

    return leven_sum/list1.length
