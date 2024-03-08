def filter_and_print_range(input_list, min_val, max_val):
    #write your code here
    output = ''
    for string in iter(input_list):
        
        num = int(string)
        
        if min_val >= num and num >= max_val:
            output += str(num) + ','

    print (output , end='')


if __name__ == '__main__':
    # Get input for the list of integers
    user_input = input("Enter a space-separated string of numbers: ")
    integer_list = user_input.split()

    # Get input for the range (min and max values)
    user_input = input("Enter the min and max values separated by a space: ")
    range_list = user_input.split()
    min_val, max_val = int(range_list[0]) , int(range_list[1])

    # Call the function to filter and print the numbers in the given range

    filter_and_print_range(integer_list, min_val, max_val)