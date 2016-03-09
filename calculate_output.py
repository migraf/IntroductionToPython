__author__ = "Anton Benz"

from distance_methods_lists import *
from languages import *


def distance_two_languages(language_one, language_two):
#use input as keys in order to get respective lists of words
    language_corpus = Languages("listss16.txt")
    words_lang1 = language_corpus.dictionary[language_one]
    words_lang2 = language_corpus.dictionary[language_two]
#calculate normalized levenstein distance of both languages
    dist = levenstein_list_normalized(words_lang1, words_lang2)
#
# insert other distance methods
#
    return dist

# output for the caparison of two selected languages
def compare_two_languages_output(language_one, language_two, output):
    answer = language_one + " and " + language_two + " have been compared.\n" \
            "Below you can find the results for the different \ndistance methods \n" \
            "============================================================\n" \
            "Levenstein distance: %.4f" \
            "\nn-gram distance:" % (output)
    return answer

def compare_one_language_output(dict, language_one):
    languages_and_distances = lstein_list_on_dictionary(dict, language_one)
    languages_sorted_by_distance = sorted(languages_and_distances, key = languages_and_distances.get)
    languages_sorted_by_distance.remove(language_one)
    reverseSort = []
    for language in reversed(languages_sorted_by_distance):
        reverseSort.append(language)
    answer = language_one + " has been compared to all other languages.\n \n" \
                        "The most similar language is: "+ reverseSort[0] +"\n" \
                        "============================================================\n" \
                        "The least similar language is: " + reverseSort[len(reverseSort)-1] + "\n" \
                         "============================================================\n"

    ninety = 0
    eighty = 0
    seventy = 0
    rest = 0
    for language in reverseSort:

        if languages_and_distances[language] >= 0.9:
            ninety += 1
        elif languages_and_distances[language] >= 0.8:
            eighty += 1
        elif languages_and_distances[language] >= 0.7:
            seventy += 1
        else:
            rest += 1

    over_ninety = ninety/float(len(reverseSort))
    over_eighty = eighty/float(len(reverseSort))
    over_seventy = seventy/float(len(reverseSort))
    rest = rest/float(len(reverseSort))

    answer += "%.4f%% of all languages are more than 90%% similar. \n" \
              "%.4f%% of all languages are more than 80%% similar. \n" \
              "%.4f%% of all languages are more than 70%% similar. \n" \
              "%.4f%% of all languages are less than 70%% similar. \n" \
              "============================================================\n" \
              %(over_ninety,over_eighty,over_seventy, rest)
    for language in reverseSort:
            answer += language + ": %.4f\n" %(languages_and_distances[language])
    return answer



