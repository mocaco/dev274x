def let_to_num(letter):
    phone_letters = [" ", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
    key = 0
    while key < 10:
        if letter in phone_letters[key]:
            return key
        else:
            key = key + 1
            return "Not Found."


def reverse_a_string(phrase):
    index = 0
    list_check = list()
    list_new = list()
    new_str = ""
    while index < len(phrase):
        list_check.insert(index, phrase[index])
        list_new.insert(0 , list_check.pop())
        new_str = new_str + list_new[index]
        index = index + 1
    return list_new


let_to_num(input("Input a letter:"))
reverse_a_string(input("Input a phrase:"))
