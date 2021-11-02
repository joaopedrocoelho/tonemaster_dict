import json

def sort_by_frequency(e):
    return int(e["frequency"])

def sort_list():
    with open("./四字成语频率列表.json", "r", encoding='utf-8-sig') as idiom_list, open("./idioms.json", "r", encoding='utf-8') as idioms_dict_json:
        sorted_list = []
        unsorted_list = []
        idioms = json.load(idiom_list)
        idioms_dict = json.load(idioms_dict_json)
        idioms.sort(reverse=True, key=sort_by_frequency) 
    for idiom_f in idioms:
        found = False
        for idiom in idioms_dict:
            if idiom_f['idiom'] == idiom['simplified']:
                found = True
                print("Adding %s"%idiom_f['idiom'])
                sorted_list.append(idiom)
    for idiom in idioms_dict:
        if idiom not in sorted_list:
            print("Adding extra idiom %s"%idiom['simplified'])
            unsorted_list.append(idiom) 

    with open("./idioms-sorted.json","x",encoding="utf-8") as sorted_file, open("./idioms-extra.json", "x", encoding='utf-8') as extra_file:
        print("saving sorted file...")
        json.dump(sorted_list, sorted_file, ensure_ascii=False)
        print("saving extra file...")
        json.dump(unsorted_list, extra_file, ensure_ascii=False)
        print("All done!")
sort_list()
