import emoji

def myfunction(word) :

    if word == ":)" :

        emoji1 = word.replace(":)", emoji.emojize(":slightly_smiling_face:"))
        return emoji1

    else : 

        emoji1 = emoji.emojize(":slightly_frowning_face:")
        return emoji1



def function(name):

    first = name.split(" ")

    if len(first) == 4 :

        name1 = first[0] + " " + first[1].replace(":)", emoji.emojize(":slightly_smiling_face:"))
        name2 = first[2] + " " + first[3].replace(":(", emoji.emojize(":slightly_frowning_face:"))

        print(name1, name2)

    else :
        
        word = first[1]
        print(first[0], myfunction(word))

level = input()
function(level)
