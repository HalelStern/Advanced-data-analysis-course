#present: Halel Stern
#Id: 212122147

def revword(new_word):
    new_word = new_word.lower().strip()[::-1]
    return(new_word)


def countword():
    text = open("text.txt", "r")
    count = 1
    for i in text:
        list_words = i.split(" ")
        if len(list_words) == 1:
            word = list_words[0].lower().strip()
            print(word)
        else:
            for j in list_words :
                x = revword(j).strip()
                if x == word:
                    count += 1
    print(count)

countword()

