count = 0 #initialise variable count

while True:
    my_string = input("enter a string: ") # str is a function, bad coding practice
    
    if my_string == "####": # exit while loop
        print(count, "string with letter 'a'") # print the final amount before exiting programme
        break

    for letter in my_string:
        if letter == 'a':
            count += 1 # if string has letter a, increment count and move on to next word
            break # prevent repeated count of 'a'