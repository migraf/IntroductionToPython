__author__ = "Anton Benz"

from distance_methods_lists import *



def distance_two_languages(language_one, language_two):
#use input as keys in order to get respective lists of words
    dictionary = split_file("listss16.txt")
    words_lang1 = dict_keys_as_list(dictionary[language_one])
    words_lang2 = dict_keys_as_list(dictionary[language_two])
#calculate normalized levenstein distance of both languages
    dist = [levenstein_list_normalized(words_lang1, words_lang2)]

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
            "Levenshtein distance: %.4f" \
            "\n2-gram distance: %.4f " \
            "\n3-gram distance: %.4f" % (output[0], output[1], output[2])
    return answer

def compare_one_language_output(dict, language_one):

    #levenstein distance
    lv_languages_and_distances = lstein_list_on_dictionary(dict, language_one)
    languages_sorted_by_distance = sorted(lv_languages_and_distances, key = lv_languages_and_distances.get)
    languages_sorted_by_distance.remove(language_one)



    #calculate n-grams and levenstein for most similar and least similar language:
    dictionary = split_file("listss16.txt")
    compare_to = dict_keys_as_list(dictionary[language_one])
    words_lang1 = dict_keys_as_list(dictionary[languages_sorted_by_distance[0]])
    words_lang2 = dict_keys_as_list(dictionary[languages_sorted_by_distance[len(languages_sorted_by_distance)-1]])

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
                        "============================================================\n" \
                            "According to the Levenshtein Distance measure,\n" \
                        "the most similar language is: "+ languages_sorted_by_distance[0] +"\n" \
                        "Levenshtein Distance: %.4f\n" \
                        "2-gram Distance: %.4f\n" \
                        "3-gram Distance: %.4f\n" %(dist1[0], dist1[1], dist1[2]) + "============================================================\n" \
                        "The least similar language is: " + languages_sorted_by_distance[len(languages_sorted_by_distance)-1] + "\n" \
                         "Levenshtein Distance: %.4f\n" \
                        "2-gram Distance: %.4f\n" \
                        "3-gram Distance: %.4f\n" \
                        "============================================================\n" %(dist2[0], dist2[1], dist2[2])

    ten = 0
    thirty = 0
    fifty = 0
    rest = 0
    for language in languages_sorted_by_distance:

        if lv_languages_and_distances[language] >= 0.9:
            ten += 1
        elif lv_languages_and_distances[language] >= 0.7:
            thirty += 1
        elif lv_languages_and_distances[language] >= 0.5:
            fifty += 1
        else:
            rest += 1

    over_ten = ten/float(len(languages_sorted_by_distance))
    over_thirty = thirty/float(len(languages_sorted_by_distance))
    over_fifty = fifty/float(len(languages_sorted_by_distance))
    over_rest = rest/float(len(languages_sorted_by_distance))

    answer += "Considering the Levenshtein Distance measure,\n" \
              "%s (%.4f%%) of all languages are less than 10%% similar. \n" \
              "%s (%.4f%%) of all languages are in between 10%% and 30%% similar. \n" \
              "%s (%.4f%%) of all languages are in between 30%% and 50%%\nsimilar. \n" \
              "%s (%.4f%%) of all languages are more than 50%% similar. \n" \
              "============================================================\n" \
              %(ten,over_ten*100, thirty,over_thirty*100, fifty,over_fifty*100,  rest,over_rest*100)

    for language in languages_sorted_by_distance:
            answer += language + ": %.4f\n" %(lv_languages_and_distances[language])
    return answer



