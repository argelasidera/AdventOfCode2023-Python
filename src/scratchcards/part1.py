from typing import List


def get_list_scores(count: int) -> List[int]:
    list_scores = [1]
    for i in range(count - 1):
        list_scores.append(list_scores[i] * 2)
    return list_scores


def scratchcards(text: str):
    with open(text) as file:
        winning_numbers = []
        my_numbers = []

        for line in file:
            nums = line.strip().split(": ")[1]
            [winning_number, my_number] = nums.split(" | ")
            win_num_dict = dict()

            for win_num in winning_number.split():
                win_num_dict[win_num] = True

            winning_numbers.append(win_num_dict)
            my_numbers.append(my_number.split())

        scores = get_list_scores(len(winning_numbers[0]))
        total_count = 0

        for i in range(len(winning_numbers)):
            card = winning_numbers[i]
            winning_count = 0

            for curr_my_num in my_numbers[i]:
                if curr_my_num in card:
                    winning_count += 1
            else:
                if winning_count > 0:
                    total_count += scores[winning_count-1]

        print(total_count)
        return total_count


if __name__ == "__main__":
    scratchcards("text.txt")
