#if the english contains the word idiom
#add word to idiom list
import re
import json

def find_word(string, word):
    pattern = re.compile(r'\b({0})\b'.format(word), flags=re.IGNORECASE)
    return bool(pattern.search(string)) 

def filter_idioms():
    idioms = []
    with open("../original.json", "r", encoding="utf-8") as cedict_dict:
        cedict = json.load(cedict_dict)
        print("Opened cedict...")
        for word in cedict:
            
            if find_word(word['english'], 'idiom'):
                print(word['traditional'], find_word(word['english'],'idiom'))
                idioms.append(word)
    with open("./idioms.json","x", encoding="utf-8") as idioms_dict:
        json.dump(idioms,idioms_dict, ensure_ascii=False)

filter_idioms()