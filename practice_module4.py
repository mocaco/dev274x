"""
#Task2
mean_temp = open('mean_temp.txt','r')
headings = mean_temp.readline().split(",")
print(headings)
# [ ] The Weather: use while loop to print city and highest monthly average temp in celsius
city_temp =  mean_temp.readline()
while city_temp:
    city_string_list = city_temp.split(',')
    print(city_string_list[0],city_string_list[2])
    city_temp = mean_temp.readline()
mean_temp.close()
"""

#Task3
digits_of_pi = open('digits_of_pi.txt','r')
name = input("Input your name:")
print("Hi,", name)
seed = len(name)
digits_of_pi.seek(seed)
digit = digits_of_pi.read(seed)[0]
print(seed, digit)
guess = input("Enter a single digit to guess or 'q' to exit:")
correct = 0
wrong = 0
while guess.isdigit():
    if digit == '.':
        digit = digits_of_pi.read(seed + 1)
    elif digit == "\n":
        seed += 1
        digit = digits_of_pi.read(seed)
    elif guess.isdigit():
        if guess == digit:
            print ("Correct!")
            correct += 1
        else:
            print ("Wrong!")
            wrong += 1
print("Your correct scores:", correct)
print("Your lose scores:", wrong)
digits_of_pi.close()








