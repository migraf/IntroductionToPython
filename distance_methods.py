__author__ = "Michael Graf"

def init_list(wrong_word, target_word):
    out_list = []

    for i in range(len(wrong_word) + 1):
        inner_list = []
        for j in range(len(target_word) + 1):
            inner_list.append(j + i)
        out_list.append(inner_list)

    return out_list


def delete_rest(initialized_list, wrong_word, target_word):
    subs = 0

    for i in range(1, len(initialized_list)):
        for j in range(1, len(initialized_list[i])):
            if wrong_word[i - 1] == target_word[j - 1]:
                subs = 0
            else:
                subs = 1
            initialized_list[i][j] = min(initialized_list[i - 1][j] + 1,
                                         initialized_list[i][j - 1] + 1,
                                         initialized_list[i - 1][j - 1] + subs)

    return initialized_list


def calc_L_distance(wrong_word, target_word):
    l_list = delete_rest(init_list(wrong_word, target_word)
                         , wrong_word, target_word)

    return l_list[len(wrong_word)][len(target_word)]


# Normalizes the Levensthein distance by dividing by the length of the longer of the two words
def calc_normalized_L_dist(word1, word2):
    if len(word1) > len(word2):
        return (calc_L_distance(word1, word2)) / float(len(word1))
    else:
        return (calc_L_distance(word1, word2)) / float(len(word2))
