__author__ = "Anton Benz"

from distance_methods_lists import *



def distance_two_languages(language_one, language_two):
#use input as keys in order to get respective lists of words
   # language_corpus = Languages("listss16.txt")
   # words_lang1 = language_corpus.dictionary[language_one]
   # words_lang2 = language_corpus.dictionary[language_two]
    dictionary = split_file("listss16.txt")
    words_lang1 = dict_keys_as_list(dictionary[language_one])
    words_lang2 = dict_keys_as_list(dictionary[language_two])
#calculate normalized levenstein distance of both languages
    dist = [levenstein_list_normalized(words_lang1, words_lang2)]
#
# insert other distance methods
    dist.append(n_gram_dist_list_norm(words_lang1, words_lang2,2))
    dist.append(n_gram_dist_list_norm(words_lang1, words_lang2,3))
#
    return dist

# output for the caparison of two selected languages
def compare_two_languages_output(language_one, language_two, output):
    answer = language_one + " and " + language_two + " have been compared.\n" \
            "Below you can find the results for the different \ndistance methods \n" \
            "============================================================\n" \
            "Levenstein distance: %.4f" \
            "\n2-gram distance: %.4f " \
            "\n3-gram distance: %.4f" % (output[0], output[1], output[2])
    return answer

def compare_one_language_output(dict, language_one):

    #levenstein distance
    lv_languages_and_distances = lstein_list_on_dictionary(dict, language_one)
    n2_languages_and_distances = []
    n3_languages_and_distances = []
    languages_sorted_by_distance = sorted(lv_languages_and_distances, key = lv_languages_and_distances.get)
    languages_sorted_by_distance.remove(language_one)
    reverseSort = []
    for language in reversed(languages_sorted_by_distance):
        reverseSort.append(language)

    #calculate n-grams and levenstein for most similar and least similar language:
    dictionary = split_file("listss16.txt")
    compare_to = dict_keys_as_list(dictionary[language_one])
    words_lang1 = dict_keys_as_list(dictionary[reverseSort[0]])
    words_lang2 = dict_keys_as_list(dictionary[reverseSort[len(reverseSort)-1]])

    #calculate normalized levenstein distance of most similar language
    dist1 = [levenstein_list_normalized(compare_to, words_lang1)]
    #calculate n-grams of most similar language
    dist1.append(n_gram_dist_list_norm(compare_to, words_lang1,2))
    dist1.append(n_gram_dist_list_norm(compare_to,words_lang1,3))

    #calculate normalized levenstein distance of least similar language
    dist2 = [levenstein_list_normalized(compare_to, words_lang2)]
    #calculate n-grams of most similar language
    dist2.append(n_gram_dist_list_norm(compare_to, words_lang2,2))
    dist2.append(n_gram_dist_list_norm(compare_to, words_lang2,2))




    answer = language_one + " has been compared to all other languages.\n \n" \
                        "The most similar language is: "+ reverseSort[0] +"\n" \
                        "Levenstein Distance: %.4f\n" \
                        "2-gram Distance: %.4f\n" \
                        "3-gramd Distance: %.4f\n" %(dist1[0], dist1[1], dist1[2]) + "============================================================\n" \
                        "The least similar language is: " + reverseSort[len(reverseSort)-1] + "\n" \
                         "============================================================\n" \
                         "Levenstein Distance: %.4f\n" \
                        "2-gram Distance: %.4f\n" \
                        "3-gramd Distance: %.4f\n" \
                        "============================================================\n" %(dist2[0], dist2[1], dist2[2])

    ninety = 0
    eighty = 0
    seventy = 0
    rest = 0
    for language in reverseSort:

        if lv_languages_and_distances[language] >= 0.9:
            ninety += 1
        elif lv_languages_and_distances[language] >= 0.8:
            eighty += 1
        elif lv_languages_and_distances[language] >= 0.7:
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
            answer += language + ": %.4f\n" %(lv_languages_and_distances[language])
    return answer



