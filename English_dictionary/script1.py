import json
from difflib import get_close_matches


data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return(data[word])

    elif word.title() in data:
        return(data[word.title()])

    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print(f"Did you mean {get_close_matches(word, data.keys())[0]} ?")
        a = input("Y or N:")
        a = a.lower()
        if a == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif a == 'n':
            print('Please recheck the word you entered')
        else:
            print("We didn't understand your entry")

    else:
        print('Please recheck the word you entered')


while(True):
    word = input("Enter a word to find its meaning:")
    meanings = translate(word)
    for item in meanings:
        print(item)
