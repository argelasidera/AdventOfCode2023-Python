def get_text_value(substring: str, is_start: bool) -> int:
    number_dict = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    if is_start:
        for i in [3, 4, 5]:
            if substring[:i] in number_dict:
                return number_dict[substring[:i]]
    else:
        for i in [-3, -4, -5]:
            if substring[i:] in number_dict:
                return number_dict[substring[i:]]

    return -1


def find(string: str) -> int:
    s_len = len(string)

    f = -1
    l = -1

    i = 0
    j = s_len - 1

    while f == -1 or l == -1 and i < s_len and j > -1:
        if f == -1 and i < s_len:
            f_letter = get_text_value(string[0:i + 1], False)
            if string[i].isdigit():
                f = int(string[i])
            elif f_letter != -1:
                f = f_letter

        if l == -1 and j > -1:
            l_letter = get_text_value(string[j:s_len], True)
            if string[j].isdigit():
                l = int(string[j])
            elif l_letter != -1:
                l = l_letter

        i += 1
        j -= 1

    return int(f"{f}{l}")


def trebuchet(source_file: str):
    with open(source_file) as file:
        count = 0
        for line in file:
            count += find(line)

    print(count)


if __name__ == "__main__":
    trebuchet("text.txt")
