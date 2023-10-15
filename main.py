import random
# print multiline instruction
# performstring concatenation of string
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")
user_paper=0
user_rock=0
user_scissors=0
while True:
     
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
     
    # take the input from user
     
    choice=int(input("Enter your choice :"))
     
     # OR is the short-circuit operator
    # if any one of the condition is true
    # then it return True value
     
    # looping until user enter invalid input
    while choice > 3 or choice <1:
      choice=int(input('Enter a valid choice please ☺'))
         
        # initialize value of choice_name variable
    # corresponding to the choice value
    if choice == 1:
        choice_name= 'Rock'
        user_rock+=1
    elif choice == 2:
        choice_name= 'Paper'
        user_paper+=1
    else:
        choice_name= 'Scissors'
        user_scissors+=1
         
        # print user choice
    print('User choice is \n',choice_name)
    print('Now its Computers Turn....')
     
    # Computer chooses randomly any number
    # among 1 , 2 and 3. Using randint method
    # of random module
    print("________________",user_rock)
    print("________________",user_paper)
    print("________________",user_scissors)
    if user_paper==0 and user_rock==0 and user_scissors==0:
        comp_choice = random.randint(1,3)
    else:
        if user_rock>user_paper and user_paper==user_scissors:
            comp_choice=2
        if user_paper>user_rock>user_scissors:
            comp_choice=2
        elif user_paper<user_rock>user_scissors:
            comp_choice=2
        elif user_paper>user_rock<user_scissors:
            comp_choice=1
        elif user_paper<user_rock<user_scissors:
            comp_choice=1
        elif user_paper==user_rock==user_scissors:
            comp_choice = random.randint(1,3)
        elif user_paper==user_rock>user_scissors:
            comp_choice=2
        elif user_rock<user_paper<user_scissors:
            comp_choice=1
        elif user_paper>user_rock==user_scissors:
            comp_choice=3
        elif user_paper==user_rock<user_scissors:
            comp_choice=1

        
         
     # initialize value of comp_choice_name
    # variable corresponding to the choice value
    if comp_choice == 1:
        comp_choice_name = 'rocK'
    elif comp_choice == 2:
        comp_choice_name = 'papeR'
    elif comp_choice==3:
        comp_choice_name = 'scissoR'
    else:
        raise Exception("Sorry! but there was a BUG!")
    print("Computer choice is \n", comp_choice_name)
    print(choice_name,'Vs',comp_choice_name)
    # we need to check of a draw
    if choice == comp_choice:
        print('Its a Draw',end="")
        result="DRAW"
    # condition for winning      
    if (choice==1 and comp_choice==2):
        print('paper wins =>',end="")
        result='papeR'
    elif (choice==2 and comp_choice==1):
        print('paper wins =>',end="")
        result='Paper'
         
       
    if (choice==1 and comp_choice==3):
        print('Rock wins =>\n',end= "")
        result='Rock'
    elif (choice==3 and comp_choice==1):
        print('Rock wins =>\n',end= "")
        result='rocK'
         
    if (choice==2 and comp_choice==3):
        print('Scissors wins =>',end="")
        result='scissoR'
    elif (choice==3 and comp_choice==2):
        print('Scissors wins =>',end="")
        result='Scissors'
     # Printing either user or computer wins or draw
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    if result == comp_choice_name:
        print("<== Computer wins ==>")
        #raise Exception("Sorry! but there was a BUG!")
# after coming out of the while loop
# we print thanks for playing
print("thanks for playing")
