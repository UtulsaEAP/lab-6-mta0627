def check_palindrome(user_input):
 #type your code here
    string = user_input.replace(' ','')
    
    reverse_string = ''
    for char in iter(string):
        reverse_string = char + reverse_string
    
    if string == reverse_string:
        print (f'palindrome: {user_input}')
    else:
        print (f'not a palindrome: {user_input}')


if __name__ == "__main__":
    user_input = input()
    check_palindrome(user_input)
