language_and_words = {}
language_list = []


def read_asjp_file(filename):
    return open(str(filename), "r")


# Going through the input file and finding the entries for the different languages
# Then taking the next 40 words after a found language and putting them into the dictionary with the language
# as well as adding the languages to a list

def split_file(textfile):
    lines = textfile.readlines()
    k = 0
    for line in lines:
        k += 1
        line = line.split()

        # finding a language entry
        if not line[0].isalnum():
            language_list.append(line[0].split("{")[0])
            # adding the next 40 words(excluding the already calculated score
            word_list = lines[k + 1:k + 41]
            final_wordlist = []
            for words in word_list:
                words = words.split()
                try:
                    final_wordlist.append(words[2])
                except IndexError:
                    final_wordlist.append("")

            language_and_words[line[0].split("{")[0]] = final_wordlist


split_file(read_asjp_file("listss16.txt"))
print language_and_words
