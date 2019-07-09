import random
words = open("words.txt").read().splitlines()
randomword = random.choice(words)

# Build a hangman image to print on screen
hangman_img = ['''

     +---+

     |   |

         |

         |

         |

         |

  =========''', '''

 

    +---+

    |   |

    O   |

        |

        |

        |

  =========''', '''

 

    +---+

    |   |

    O   |

    |   |

        |

        |

  =========''', '''

 

    +---+

    |   |

    O   |

   /|   |

        |

        |

  =========''', '''

 

    +---+

    |   |

    O   |

   /|\  |
        |

        |

  =========''', '''

 

    +---+

    |   |

    O   |

   /|\  |

   /    |

        |

  =========''', '''

 

    +---+

    |   |

    O   |

   /|\  |

   / \  |

        |

 =========''']
    

number_of_tries = 0
tries_left = 7
guesslist = []
while tries_left > 0:
    
    print(randomword)
    randomword_display = '*' * len(randomword)
    print(randomword_display)
    guess = input("Guess a letter from the word above or guess the whole word: ")
    
    if len(guess) > 1: # if they guess a whole word
            if guess == randomword:
                print( randomword + " is the correct word. You won!")
                break
            else:
                print("You guessed the wrong word! Please try again")
                print("You have " + str(tries_left) + " tries left to guess the whole word")   
    else: # if they guess a letter
            if guess in guesslist:
                print("You already guessed that one")
            elif guess in randomword: # if letter is correct
                print("You guessed a correct letter!")
                print("You have " + str(tries_left) + " tries left to guess the whole word")
                guesslist.append(guess)
                
            else: # if letter is incorrect
                print("You guessed the wrong letter! Please try again")
                print("You have " + str(tries_left) + " tries left to guess the whole word")
                guesslist.append(guess)
                tries_left -= 1
                number_of_tries += 1
                print (hangman_img[number_of_tries - 1])
                if tries_left == 0: # if max number of tries is reached
                    try_again = input("Game over! Try again? y/n ")
                    if try_again == "y":
                        number_of_tries = 0
                    elif try_again == "n":
                        print("Thank you, come again")
                        input("Press Enter to confirm and leave the game...")
                    else:
                        print("Please enter a valid choice: y or n ") 
                        
                

