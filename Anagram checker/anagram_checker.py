def anagram_checker(word_1, word_2):
    word_1 = word_1.lower()
    word_2 = word_2.lower()

    word_dict_1 = {}
    word_dict_2 = {}

    for i in range(len(word_1)):
        word_dict_1[word_1[i]] = word_dict_1.get(word_1[i], 0) + 1
        word_dict_2[word_2[i]] = word_dict_2.get(word_2[i], 0) + 1
    if word_dict_1 == word_dict_2:
        return "Anagram"
    else:
        return "Not an anagram"


def main():
    print(anagram_checker("listen", "silent"))
    print(anagram_checker("hello", "world"))
    print(anagram_checker("Dormitory", "dirtyroom"))


if __name__ == "__main__":
    main()
