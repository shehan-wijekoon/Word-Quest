i=0
guessed_word =[]
print("""
██╗    ██╗ ██████╗ ██████╗ ██████╗      ██████╗ ██╗   ██╗███████╗███████╗████████╗
██║    ██║██╔═══██╗██╔══██╗██╔══██╗    ██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝
██║ █╗ ██║██║   ██║██████╔╝██║  ██║    ██║   ██║██║   ██║█████╗  ███████╗   ██║   
██║███╗██║██║   ██║██╔══██╗██║  ██║    ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   
╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    ╚██████╔╝╚██████╔╝███████╗███████║   ██║   
 ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝      ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   
""")
right_word = input("Enter your hidden word!:  ")
#print('Pass to your friend and give them a chance to guess')

while i<3:
    guess_word = input('Allright, Make a gess! : ')
    if guess_word == right_word:
        print('Your won!')
        print("Lets's play another round")
        break
    
    elif guess_word in guessed_word:
        print('You already guessed this word! Try another one.')
        print('')
    
    else:
        guessed_word.append(guess_word)
        print(' ')
        
        if len(guess_word) < len(right_word):
            print('Your guess is too low!')
        else:
            print('Your guess is too high!')
    i+=1

else:
    print('Your all 3 chances are over')