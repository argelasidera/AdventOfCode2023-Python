def find(string: str) -> int:
    s_len = len(string)

    f = -1
    l = -1

    i = 0
    j = s_len - 1

    while f == -1 or l == -1 and i < s_len and j > -1:
        if f == -1 and i < s_len:
            if string[i].isdigit():
                f = int(string[i])

        if l == -1 and j > -1:
            if string[j].isdigit():
                l = int(string[j])

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
