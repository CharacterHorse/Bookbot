def get_num_words(text):
    text = text.split()
    return len(text)


def get_num_letters(text):
    counter = {}
    for char in text:
        char = char.lower()
        if char not in counter and char.isalpha():
            counter[char] = 1
        elif char.isalpha():
            counter[char] += 1
    return counter


def get_sorted_letter_dict(counter):
    count_dict = []
    for item in counter.items():
        count_dict.append({"char": item[0], "num": item[1]})

    def sort_on(dict):
        return dict["num"]

    count_dict.sort(reverse=True, key=sort_on)

    return count_dict
