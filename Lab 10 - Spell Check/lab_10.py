import re

def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def main():

    dictionary_file = open("dictionary.txt")
    dictionary_list = []

    for line in dictionary_file:
        line = line.strip()
        dictionary_list.append(line)

    dictionary_file.close()


    print("--Linear Search--")

    my_file = open("AliceInWonderLand200.txt")

    line_number = 0

    for line in my_file:
        line_number += 1
        line = line.strip()
        word_list = split_line(line)

        for word in word_list:
            word = word.strip()

            key = word.upper()
            current_position = 0
            while current_position < len(dictionary_list) and dictionary_list[current_position] != key:
                current_position += 1

            if current_position == len(dictionary_list):

                print("Line", line_number, "possible misspelled word:", key)


    my_file.close()





            # Create variable for line number

    print("--Binary Search--")
    my_file = open("AliceInWonderLand200.txt")
    line_number = 0

    for line in my_file:
        line_number += 1
        line = line.strip()
        word_list = split_line(line)

        for word in word_list:
            word = word.strip()


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
                elif dictionary_list[middle_pos] == key:
                    found = True

            if not found:
                print("Line", line_number, "possible misspelled word:", key)

    my_file.close()


main()
