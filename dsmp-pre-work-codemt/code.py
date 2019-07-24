# --------------
##File path for the file 
file_path 


#Code starts here
def read_file(path):
    file = open(path,"r")
    sentence = file.readline()
    file.close()
    return sentence


sample_message = read_file(file_path)

print(sample_message)


# --------------
#Code starts here
def read_file(file_path_1,file_path_2):
    file_path_1 = open(file_path_1,"r")
    file_path_2 = open(file_path_2,"r")
    message_1 = file_path_1.readline()
    message_2 = file_path_2.readline()
    return message_1,message_2


def fuse_msg(message_a,message_b):
    quotient = int(message_b)//int(message_a)
    return str(quotient)

messages = read_file(file_path_1,file_path_2)  
print(messages)
message_1 = messages[0]
print(message_1)
message_2 = messages[1]
print(message_2)
secret_msg_1 = fuse_msg(message_1,message_2)
print(secret_msg_1)






# --------------
#Code starts here
def read_file(file_path_3):
    file = open(file_path_3,"r")
    message_3 = file.readlines()
    return message_3


def substitute_msg(message_c):
    sub = ''
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    else:
        sub = 'Marine Biologist'

    return sub   

messages = read_file(file_path_3)
print(messages)
message_3 = messages[0]
print(message_3)
secret_msg_2 = substitute_msg(message_3)
print(secret_msg_2)




# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

#Code starts here
def read_file(file_path_4,file_path_5):
    file1 = open(file_path_4,"r")
    file2 = open(file_path_5,"r")
    message_4 = file1.readline()
    message_5 = file2.readline()
    return message_4,message_5
#Function to compare message
def compare_msg(message_d,message_e):
    
    #Splitting the message into a list
    a_list=message_d.split()
    
    #Splitting the message into a list
    b_list=message_e.split()
    
    #Comparing the elements from both the lists
    c_list = [i for i in a_list if i not in b_list]
    
    #Combining the words of a list back to a single string sentence
    final_msg=" ".join(c_list)
    
    #Returning the sentence
    return final_msg


#Calling the function to read file
messages=read_file(file_path_4,file_path_5)
print(messages)
message_4 = messages[0]
message_5 = messages[1]

#Calling the function to read file
#message_5=read_file(file_path_5)

#Calling the function 'compare messages'
secret_msg_3=compare_msg(message_4,message_5)

#Printing the secret message
print(secret_msg_3)

#Code ends here






# --------------
#Code starts here
def read_file(file_path_6):
    file = open(file_path_6,"r")
    message_6 = file.readline()
    return message_6

# Function to filter message
def extract_msg(message_f):
    # Splitting the message into a list
    a_list = message_f.split()

    # Creating the lambda function to identify even length words
    even_word = lambda x: (len(x) % 2 == 0)

    # Splitting the message into a list
    b_list = (filter(even_word, a_list))

    # Combining the words of a list back to a single string sentence
    final_msg = " ".join(b_list)

    # Returning the sentence
    return final_msg


# Calling the function to read file
message_6 = read_file(file_path_6)
print(message_6)
# Calling the function 'filter_msg'
secret_msg_4 = extract_msg(message_6)

# Printing the secret message
print(secret_msg_4)

# Code ends here


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'

#Code starts here
def write_file(path,secret_msg):
    file = open(path,"a+")
    file.write(secret_msg)
    file.close()

secret_msg = " ".join(message_parts)
write_file(final_path,secret_msg)
print(secret_msg)


