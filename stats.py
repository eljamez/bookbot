def get_num_words(words):
    word_count = len(words.split())
    return word_count

def get_num_characters(words):
    char_count_dict = {}
    for char in words:
        lsChar = char.lower()
        if lsChar in char_count_dict:
            char_count_dict[lsChar] += 1
        else:
            char_count_dict[lsChar] = 1
    return char_count_dict

def sort_on(items):
    return items["num"]

def get_chars_sorted(dict):
    sorted_list = []
    for val in dict:
        letter_count = dict[val]
        sorted_list.append({"char":val, "num":letter_count})
    sorted_list.sort(reverse=True, key=sort_on)   
    return sorted_list 
