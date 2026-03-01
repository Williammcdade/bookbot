def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
<<<<<<< HEAD
        if lowered.isalpha():
            if lowered in chars:
                chars[lowered] += 1
                #chars[lowered].append()
            else:
                chars[lowered] = 1
    return chars

def sort_on_value(item):
    return item[1]

def get_sorted_chars_list(text):
    chars_dict = get_chars_dict(text)
    sorted_chars = sorted(chars_dict.items(), key=sort_on_value, reverse=True)
    return sorted_chars
=======
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sorted_dict(chars):
    chars_list = []
    for char in chars:
        if char not in chars_list:
            chars_list["char": char[0], "num": char[1]]
    return chars_list        
>>>>>>> 7fff7b9 (jic)
