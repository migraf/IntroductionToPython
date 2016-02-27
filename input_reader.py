__author__ = "Michael Graf"
# Going through the input file and finding the entries for the different languages
# Then taking the next 40 words after a found language and putting them into the dictionary with the language
# as well as adding the languages to a list
def split_file(textfile):

    language_and_words = {}

    input_file = open(str(textfile), "r")
    lines = input_file.readlines()
    k = 0
    for line in lines:
        k += 1
        line = line.split()

        # finding a language entry in the file
        if not line[0].isalnum():
            # adding the next 40 words(excluding the already calculated score
            word_list = lines[k+1:k+41]
            final_wordlist = []
            for words in word_list:
                words = words.split()
                try:
                    final_wordlist.append(words[2])
                except IndexError:
                    final_wordlist.append("")

            language_and_words[line[0].split("{")[0]] = final_wordlist

    return language_and_words

def dict_keys_as_list(dict):
    language_list = []
    for lan in dict:
        language_list.append(lan)

    return language_list












print split_file("listss16.txt")
