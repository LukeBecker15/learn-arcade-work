import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():

    my_file = open("AliceInWonderLand200.txt")

    dictionary_list = ["dictionary.txt"]


    print("--Linear Search--")

    for line in my_file:

        split_line(line)
        word_list = split_line(line)
        for word in my_file:
            key = word.upper()
            current_position = 0
            while current_position < len(dictionary_list) and dictionary_list[current_position] == key:
                current_position += 1
            if dictionary_list != key:
                print("possible misspelled word:", key)

            # Create variable for line number

    print("--Binary Search--")
    for line in my_file:

        split_line(line)
        word_list = split_line(line)
        for word in my_file:
            key = word.upper()
            lower_bound = 0
            upper_bound = len(dictionary_list) - 1
            found = False

            while lower_bound <= upper_bound and not found:
                middle_pos = (lower_bound + upper_bound) // 2

                if dictionary_list[middle_pos] < key:
                    lower_bound = middle_pos + 1
                elif dictionary_list[middle_pos] > key:
                    upper_bound = middle_pos - 1
                else:
                    found = True

                if found:
                    print(middle_pos)


main()
