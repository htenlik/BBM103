def is_it_sorted(input_list):  # List was checked for sorted or not.
    if all(input_list[i] <= input_list[i + 1] for i in range(len(input_list) - 1)):
        return True


def bubble_sort(input_list, output_file):
    for i in range(len(input_list)):
        for j in range(len(input_list) - 1):
            if input_list[j] > input_list[j + 1]:
                swap = input_list[j]  # Numbers swapped using an extra variable.
                input_list[j] = input_list[j + 1]
                input_list[j + 1] = swap

        output_file.write("Pass {}: ".format(i+1))
        for j in range(len(input_list)):
            output_file.write(str(input_list[j]))
            if j != len(input_list) - 1:  # Spaces added between numbers.
                output_file.write(" ")
        if is_it_sorted(input_list):  # List checked for is it finished or not.
            break
        else:  # If it's not keep going.
            output_file.write("\n")


def insertion_sort(input_list, output_file):
    for i in range(1, len(input_list)):
        value = input_list[i]
        x = i - 1
        while (x >= 0) and (input_list[x] > value):  # Right place searched until found it.
            input_list[x+1] = input_list[x]
            x = x - 1
        input_list[x+1] = value

        output_file.write("Pass {}: ".format(i))
        for j in range(len(input_list)):
            output_file.write(str(input_list[j]))

            if j != len(input_list) - 1:
                output_file.write(" ")

        if is_it_sorted(input_list):
            break
        else:
            output_file.write("\n")


def main():
    with open("input.txt", "r") as input_file:
        input_list = []
        for line in input_file:  # Input.txt extracted.
            numbers = [int(num) for num in line.strip().split()]
            input_list.extend(numbers)

    with open("output_bubble.txt", "w") as output_bubble:
        if len(input_list) <= 1 or is_it_sorted(input_list):  # Checked is it sorted before sorting.
            output_bubble.write("Already sorted!")
        else:
            bubble_sort(input_list.copy(), output_bubble)

    with open("output_insertion.txt", "w") as output_insertion:
        if len(input_list) <= 1 or is_it_sorted(input_list):  # Checked is it sorted before sorting.
            output_insertion.write("Already sorted!")
        else:
            insertion_sort(input_list, output_insertion)


if __name__ == "__main__":
    main()
