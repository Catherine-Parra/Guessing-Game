import random
import statistics

count_of_guesses = 0
list_of_guesses = []


def start_game():
    count_of_guesses = 0
    print('Welcome, thank you for playing the guessing game!')
    
    if(len(list_of_guesses) > 0):
        highest_score = min(list_of_guesses)
        print('The highest score so far is {}. Lets see if you can beat it!'.format(highest_score))
        
    solution = random.randint(1, 100)
    #print("Seed {}".format(solution))
    
    guess_input = 0
        
    while(guess_input != solution):
        user_input = input("Guess the number. ")
        try:
            guess_input = int(user_input)
            if guess_input > 100:
                raise SyntaxError("There has been an error. Please select a number from 1-100.")
            count_of_guesses = count_of_guesses + 1
            # add_to_list(guess_input)
        except ValueError:
            print("There has been an error. Enter a whole number")
        except SyntaxError as err:
            print("There has been an error. The number is between 1-100.")
        else:
            if guess_input > solution:
                print ("Its lower")
                
            elif guess_input < solution:
                print ("Its higher")
                
            
    print ("You got it!")
    add_to_list(count_of_guesses)
    stats()
        
        
def add_to_list(num):
    list_of_guesses.append(num)
    
def display():
    for num in list_of_guesses:
        print(num)
                 
def stats():
    print(f"Number of tries: {list_of_guesses}")

    results_mode = round(statistics.mode(list_of_guesses))
    print(f"The mode number is: {results_mode}")

    results_median = round(statistics.median(list_of_guesses))
    print(f"The median number is: {results_median}")

    results_mean = round(statistics.mean(list_of_guesses))
    print(f"The mean number is: {results_mean}")
    
   

    replay = input("Are you ready to play again?  Y/N ")

    if replay.lower() == "y":
        start_game()
    else:
        print('Thanks again for playing! Goodbye!')
        
        
            
start_game()
