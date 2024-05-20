def get_total_scratchcards(winning_numbers, my_numbers) -> int:
    cards_len = len(my_numbers)
    my_scratchcards = [1] * cards_len
    total = 0

    for i in range(cards_len):
        num_matches = 0
        for my_num in my_numbers[i]:
            if my_num in winning_numbers[i]:
                num_matches += 1
        else:
            for j in range(num_matches):
                if i+j+1 < cards_len:
                    my_scratchcards[i + j + 1] += my_scratchcards[i]
            total += my_scratchcards[i]

    return total


def scratchcards(text: str) -> int:
    with open(text) as file:
        winning_numbers = []
        my_numbers = []

        for line in file:
            cards = line.split(": ")[1]
            [winning_number, my_number] = cards.split("|")

            win_num_dict = dict()

            my_numbers.append(my_number.split())

            for win_num in winning_number.split():
                win_num_dict[win_num] = True
            else:
                winning_numbers.append(win_num_dict)

        return get_total_scratchcards(winning_numbers, my_numbers)


if __name__ == "__main__":
    scratchcards("text.txt")
