mylist = [" ","O"," "]
def shuffle_list(mylist):
    from random import shuffle
    shuffle(mylist)
    return mylist

# b = shuffle_list(mylist)
# print("Your shuffled list is: ",b)

def player_guess():
    guess = ""
    while guess not in ["0","1","2"]:
        guess = input("Pick a number: 0, 1 or 2: ")
    return int(guess)

# a = player_guess()
# print("You have picked: ",a)

def check_guess(mylist,guess):
    if mylist[guess] == "O":
        print("You guessed it right!")
    else:
        print("Your guess is wrong, better luck next time")
        print(mylist)

mixedup_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixedup_list,guess)