def process_user_contacts(user_contacts):

    # Put word pairs into a dictionary
    
    tokens = user_contacts.split()

    contact_list = {}
    for i in range(len(tokens)):
        
        name_num_pair = tokens[i].split(',')
        
        name = name_num_pair[0]
        num = name_num_pair[1]

        contact_list.update({name : num})

    # Get contact name from input, output contact's phone number
    
    user_search = input("Enter the contact name: ")

    print (contact_list.get(user_search))
    
   
if __name__ == '__main__':
    # Get input for word pairs
    user_input = input("Enter word pairs (name, phone number): ")

    # Call the function to process user contacts
    process_user_contacts(user_input)
