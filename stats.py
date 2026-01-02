def get_book_here(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def get_num_words(text):
    return len(text.split())

def count_char(text):
    c1 = [i.lower() for i in text]
    c2 = set(c1)
    B=dict()
    for m in c2:
        B[m] = c1.count(m)
    return B

def fast_sort(dict_list_items):
    return dict_list_items["num"]

def sorting_dict(dict):
    l1=list()
    for key in dict:
        l1.append({"char": key, "num": dict[key]})
    l1.sort(reverse=True, key=fast_sort)
    return l1