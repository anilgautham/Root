import random
#dict = {0:'Rock',1:'Paper',2:'Scissor',3:'Lizard',4:'Spock'}
comp = random.randint(0,4)
print("Let's play Rock,Paper,Scissors,Lizard,Spock.")
word = input("Enter your choice:\n")
word = word.title()
if comp == 0:
    print("Computer chose Rock\n")
    if word == "Paper":
        print("Paper covers Rock. You Win!!")
    elif word == "Scissors":
        print("Scissor is crushed by Rock. You Loose!!")
    elif word == "Rock":
        print("Computer chose Rock too. It's a tie!!")
    elif word == "Lizard":
        print("Lizard is crushed by Rock. You Loose!!")
    elif word == "Spock":
        print("Spock vaporizes Rock. You Win!!")
    else:
        print("Improper input. Please play again.")
elif comp == 1:
    print("Computer chose Paper\n")
    if word == "Paper":
        print("Computer chose Paper too. It's a tie!!")
    elif word == "Scissors":
        print("Scissor cuts Paper. You Win!!")
    elif word == "Rock":
        print("Rock is covered by Paper. You Loose!!")
    elif word == "Lizard":
        print("Lizard eats Paper. You Win!!")
    elif word == "Spock":
        print("Spock is disproved by Paper. You Loose!!")
    else:
        print("Improper input. Please play again.")
elif comp == 2:
    print("Computer chose Scissors\n")
    if word == "Paper":
        print("Scissors cuts Paper. You Loose!!")
    elif word == "Scissors":
        print("Computer chose Scissors too. It's a tie!!")
    elif word == "Rock":
        print("Rock crushes Scissors. You Win!!")
    elif word == "Lizard":
        print("Scissors decapitates Lizard. You Loose!!")
    elif word == "Spock":
        print("Spock smashes Scissors. You Win!!")
    else:
        print("Improper input. Please play again.")
elif comp == 3:
    print("Computer chose Lizard\n")
    if word == "Paper":
        print("Lizard eats Paper. You Loose!!")
    elif word == "Scissors":
        print("Scissors decapitates Lizard. You Win!!")
    elif word == "Rock":
        print("Rock crushes Lizard. You Win!!")
    elif word == "Lizard":
        print("Computer chose Lizard too. It's a tie!!")
    elif word == "Spock":
        print("Spock is poisoned by Lizard. You Loose!!")
    else:
        print("Improper input. Please play again.")
elif comp == 4:
    print("Computer chose Spock\n")
    if word == "Paper":
        print("Paper disproves Spock. You Win!!")
    elif word == "Scissors":
        print("Scissors are smashed by Spock. You Loose!!")
    elif word == "Rock":
        print("Rock is vaporized by Spock. You Loose!!")
    elif word == "Lizard":
        print("Lizard poisons Spock. You Win!!")
    elif word == "Spock":
        print("Computer chose Spock too. It's a tie!!")
    else:
        print("Improper input. Please play again.")
