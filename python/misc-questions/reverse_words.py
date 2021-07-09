def reverse(word):
#    word = list(word)
#    length = len(word)
#
#    for i in range(length >> 1):
#        word[i], word[length - i - 1] = word[length - i - 1], word[i]
#
#    return "".join(word)
    if not word:
        return ""

    return reverse(word[1:]) + word[0]


def reverse_words(sentence):
    if not sentence:
        return ""

    return "".join(reverse_words(sentence[1:]) + " " + reverse(sentence[0]))


sentence = "Hello World I am a goombah"
print(reverse_words(sentence.split(" ")))
