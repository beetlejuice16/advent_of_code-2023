from typing import Tuple, List

list_of_numbers = []
digits = [f"{x}" for x in range(1, 10)]
# part 2
spelled_out = ["one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]
digits.extend(spelled_out)

with open("./input.txt", mode='r') as f:
    for line in f.readlines():
        digit_order: List[Tuple] = []
        for digit in digits:
            start_ind = 0
            for i, _ in enumerate(line):
                if start_ind > i:
                    continue
                digit_found_ind = line.find(digit, start_ind)
                if digit_found_ind >= 0:
                    digit_order.append((digit_found_ind, digit))
                    start_ind = digit_found_ind + len(digit)
        # Bubble sort
        for i, _ in enumerate(digit_order):
            for j in range(len(digit_order) - 1 - i):
                if digit_order[j][0] > digit_order[j + 1][0]:
                    tmp = digit_order[j]
                    digit_order[j] = digit_order[j + 1]
                    digit_order[j + 1] = tmp

        first_char = ""
        first_digit_i = digits.index(digit_order[0][1])
        if first_digit_i > 8:
            first_char = digits[first_digit_i - 9]
        else:
            first_char = digit_order[0][1]

        last_char = ""
        last_digit_i = digits.index(digit_order[-1][1])
        if last_digit_i > 8:
            last_char = digits[last_digit_i - 9]
        else:
            last_char = digit_order[-1][1]

        two_digit = int(first_char + last_char)
        list_of_numbers.append(two_digit)
    print(sum(list_of_numbers))
