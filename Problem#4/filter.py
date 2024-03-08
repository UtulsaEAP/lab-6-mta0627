'''
Name: Mason Anderson
Time: 3/8/24 4:39 PM
'''

def process_and_print(input_string):
      # Split into separate strings

    input_data = input_string.split()

    # Convert strings to integers and filter out negative values
    
    negative_numbers = []
    for string in iter(input_data):
        
        num = int(string)

        if num < 0:
            negative_numbers.append(num)

    # Sort integers in reverse order
  
    negative_numbers.sort(reverse=True)
    
    # Print sorted integers

    output = ''
    for num in iter(negative_numbers):
        
        string = str(num)

        output += string + ' '
    
    print(output , end='')
    

if __name__ == "__main__":
    # User inputs string w/ numbers
    user_input = input("Enter a space-separated string of numbers: ")

    # Call the function to process and print the result
    process_and_print(user_input)
