def process_input(input_string):
    # Split into separate strings
    
    string_data_set = input_string.split()

    # Convert strings to floats
    data_set = []
    max_value = 0
    for string in iter(string_data_set):

        data_set.append(float(string))
        max_value += float(string)
    
    # Get max and average
    
    average_value = max_value / len(data_set)
    return max_value, average_value

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function and get the results
    max_value, average_value = process_input(user_input)

    print(f'Max Value: {max_value:.2f}')
    print(f'Average Value: {average_value:.2f}')
