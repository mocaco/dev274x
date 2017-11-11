### Element_Quiz ###
#
# function get_names - function to collect input of 5 unique element names
# the function accepts no arguments and returns a list of 5 input strings (element names)
# define a list to hold the input
# collect input of a element name
# if input it is not already in the list add the input to the list
# don't allow empty strings as input
# once 5 unique inputs return the list
def get_names():
    result = []
    count = 0
    while len(result) < 5:
        add_item = input("Enter the name of an element:").lower()
        if add_item != '':
            if add_item not in result:
                result.append(add_item)
            else:
                print(add_item, "was already entered          <--no duplicates allowed")
    return result

# main program flow
#!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt
elements = open('elements1_20.txt', 'r')
elements.seek(0)
el_list = []
el_string = ' '
while el_string:
    el_string = elements.readline().strip('\n')
    el_list.append(el_string.lower())
input_list = get_names()
correct = 0
correct_answers = ''
wrong_answers = ''
for answer in input_list:
    if answer in el_list:
        correct += 1
        correct_answers += answer.title() + ' '
    else:
        wrong_answers += answer.title() + ' '
print (correct*20, "% correct")
print ("Found:", correct_answers)
print ("Not Found:", wrong_answers)

