def words_in_book(filepath):
    filetext = get_book_text(filepath)

    num_words = len(filetext.split())

    return num_words


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents


def character_count(filepath):
    text = get_book_text(filepath)
    text = text.lower()
    character_dict = {}
    for char in text:
        if char not in character_dict:
            character_dict[char] = 1
        else:
            character_dict[char] += 1
    return character_dict


def sort_on(items):
    return items["num"]


def sort_dict(filepath):
    char_list = []
    chardict = character_count(filepath)
    for c in chardict:
        cdict = {
            "char": c,
            "num": chardict[c],
        }
        char_list.append(cdict)

    char_list.sort(reverse=True, key=sort_on)

    return char_list
