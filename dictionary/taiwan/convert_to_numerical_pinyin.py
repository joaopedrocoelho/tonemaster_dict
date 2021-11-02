import unicodedata
import json
import sys
import re

def to_tone_number(s):
    table = {0x304: ord('1'), 0x301: ord('2'), 0x30c: ord('3'),
         0x300: ord('4')}
    word = unicodedata.normalize('NFD', s).translate(table)
    word_list = list(word)
    

    for i in range((len(word_list) -1)):
           if(bool(re.search('\d', word_list[i])) and bool(re.search('[^ ]', word_list[i+1]))):
            
            word_list.insert(i+1,word_list.pop(i))
    

    return ''.join(word_list)  
    


def convert_dict(inputfile):
    new_dict = []
    with open(inputfile, "r", encoding="utf-8-sig") as input_file:
        original = json.load(input_file)
        print("Opened File..")
        for word in original:
            print("converting:")
            word['pinyin'] = to_tone_number(word['pinyin_accented'])
            print(word['traditional'])
            new_dict.append(word)
    with open("converted-dict.json", "x", encoding="utf-8") as convertedfile:
        print('Saving Converted file...')
        json.dump(new_dict,convertedfile, ensure_ascii=False)


input_file = sys.argv[1]

convert_dict(input_file)
