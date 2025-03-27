def get_word_num(book_string):
    word_list = book_string.split()
    return len(word_list)

def get_char_num(book_string):
    text = book_string.lower()
    char_dict = {}

    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
        
    return char_dict

def sort_dict(char_dict):
    list_of_values = []

    #places the char dict values in a sorted list and filters out the values belonging to non-alpha keys
    for k,v in char_dict.items():
        if k.isalpha() == True:
            list_of_values.append(v)
            list_of_values.sort(reverse=True)
        else:
            continue

    sorted_list = []

    #using the previous sorted list, new dicts are created and placed in a new list
    for i in range(len(list_of_values)):
        for key, value in char_dict.items():
            if key.isalpha() == True:
                if list_of_values[i] == value:
                    new_dict = {}
                    new_dict[key] = value
                else:
                    continue
                sorted_list.append(new_dict)

    return sorted_list
