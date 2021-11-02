import re
import json
import sys

words = []





def remove_non_chinese_chars(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as input_list:
        original_list = json.load(input_list)
    for word in original_list:
        if (re.search(r'[\u4e00-\u9fff]+', word['traditional'])):
            print("adding:", word['traditional'])
            words.append(word)
    with open(output_file, "x", encoding="utf-8") as output_file:
        json.dump(words,output_file, ensure_ascii=False) 



input_file = sys.argv[1]
output_file = sys.argv[2]
remove_non_chinese_chars(input_file, output_file)
