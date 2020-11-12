import random


def selection_sort(my_list):

    results = 0
    results_1 = 0

    for cur_pos in range(len(my_list)):

        min_pos = cur_pos
        results = results + 1


        for scan_pos in range(cur_pos + 1, len(my_list)):

            results_1 = results_1 + 1

            if my_list[scan_pos] < my_list[min_pos]:

                min_pos = scan_pos


        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp

    print(results)
    print(results_1)
def insertion_sort(my_list):
    """ Sort a list using the insertion sort """

    total = 0
    total_1 = 0


    for key_pos in range(1, len(my_list)):


        key_value = my_list[key_pos]


        scan_pos = key_pos - 1

        total = total + 1


        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1
            total_1 = total_1 + 1


        my_list[scan_pos + 1] = key_value

    print(total)
    print(total_1)


def print_list(my_list):
    for item in my_list:
        print(f"{item:3}", end="")
    print()


def main():

    list_for_selection_sort = []
    list_for_insertion_sort = []
    list_size = 1000
    for i in range(list_size):
        new_number = random.randrange(100)
        list_for_selection_sort.append(new_number)
        list_for_insertion_sort.append(new_number)

    print("Original List")
    print_list(list_for_selection_sort)


    print("Selection Sort")
    selection_sort(list_for_selection_sort)
    print_list(list_for_selection_sort)


    print("Insertion Sort")
    insertion_sort(list_for_insertion_sort)
    print_list(list_for_insertion_sort)


main()