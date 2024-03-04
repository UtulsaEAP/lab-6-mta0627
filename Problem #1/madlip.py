'''
Name: Mason Anderson
Time: 3/4/2024 2:43 PM

'''



def food_input():
    #type you while  loop here
    
    string = ''
    i=0
    while string != 'quit':
        
        user_input = input()
        tokens = user_input.split()

        number = tokens[1]
        string = tokens[0]

        if string != 'quit':
            if i == 0:
                output = f'Eating {number} {string} a day keeps you happy and healthy.'
            else:
                output = output + f'\nEating {number} {string} a day keeps you happy and healthy.'

        i += 1
    
    print (output)

if __name__ == "__main__":
    food_input()
