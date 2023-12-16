with open("./input.txt", mode='r') as f:
    list_of_numbers = []
    for line in f.readlines():
        first_char: str = ""
        for character in line:
            try:
                int(character)
            except ValueError:
                continue
            else:
                first_char = character
                break

        last_char: str = ""
        for character in line[::-1]:
            try:
                int(character)
            except ValueError:
                continue
            else:
                last_char = character
                break

        two_digit = int(first_char + last_char)
        list_of_numbers.append(two_digit)
    print(sum(list_of_numbers))
