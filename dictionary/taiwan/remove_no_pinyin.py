import json
from dragonmapper import transcriptions

new_dict = []
def remove_without_pinyin():
    with open("moedict.json", "r", encoding="utf-8") as moedict_file:
        print("Opening dictionary...")
        moedict = json.load(moedict_file)
        
        for word_tw in moedict:
            word_tw_heteronym = word_tw['heteronyms'][0]
            

            if("pinyin" in word_tw_heteronym):
                new_word = {}
                new_word['traditional'] = word_tw['title']
                new_word['pinyin_accented'] = word_tw['heteronyms'][0]['pinyin']
                new_word['pinyin'] = transcriptions.accented_syllable_to_numbered(word_tw['heteronyms'][0]['pinyin'])
                print(new_word)
                new_dict.append(new_word)
    with open("moedict_filtered.json", "x", encoding="utf-8") as converted:
        print("Converting...")
        json.dump(new_dict, converted, ensure_ascii=False)
        print("Finished...")

remove_without_pinyin()