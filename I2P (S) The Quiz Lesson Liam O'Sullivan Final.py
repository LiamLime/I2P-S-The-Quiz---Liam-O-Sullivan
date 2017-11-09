global score
score = 0 #this is to keep track of the score
def scorend(): #this function is the printing out of the final score for the user
    if score<11:
        print "You got ",score," out of 18 you get an F"
    if 14>score>11:
        print "You got ",score," out of 18 you get a C"
    if 16>score>14:
        print "You got ",score," out of 18 you get a B"
    if 17>score>15:
        print "You got ",score," out of 18 you get a B+"
    if 18>score>17:
        print "You got ",score," out of 18 you get a A-"
    if score==18:
        print "You got ",score," out of 18 you get a A"
def game(): # this is the whole function of the actual game
    global score
    while True:  #using while statements for the questions, this is the starting question if you want to play or not
        print """   ___________.__              ________          .__
    \__    ___/|  |__    ____   \_____  \   __ __ |__|________
      |    |   |  |  \ _/ __ \   /  / \  \ |  |  \|  |\___   /
      |    |   |   Y  \\  ___/  /   \_/.  \|  |  /|  | /    /
      |____|   |___|  / \___  > \_____\ \_/|____/ |__|/_____/
                    \/      \/         \__>              """
        startquiz = raw_input("""This is a multiple choice quiz. It has a bunch of fun facts, just put True or False and at the end of the 18 questions, you will get your score!
    Do you want to take the quiz? (yes or no)""")
        if startquiz.lower() == "yes":
            print "Alright! Lets go to the first question"
            break
        elif startquiz.lower() == "no":
            print "Aw man :("
            exit()
        else:
            print "please say yes or no"
    while True: #for every question it is a while loop
        firstq = raw_input("True or false :Bananas are curved because they grow towards the sun")
        if firstq.lower() == "true": #put .lower() so that it is easy to read for the code at "true" or "false"
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif firstq.lower() == "false":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        secondq = raw_input("True or false : There is a species of spider called the Hobo Spider")
        if secondq.lower() == "true":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif secondq.lower() == "false":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        thirdq = raw_input("True or false : beans, corn and peppers don't make you fart")#false
        if thirdq.lower() == "false":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif thirdq.lower()== "true":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        fourthq = raw_input("True or false : Billy goats urinate on their own heads to smell more attractive to females")#true
        if fourthq.lower() == "true":
            print "Correct! Nice one lets move to the next question!"
            score =+1
            break
        elif fourthq.lower()== "false":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        fithq = raw_input("True or false : An eagle can kill a young deer and fly away with it ")#true
        if fithq.lower() == "true":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif fithq.lower()== "false":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        sixthq = raw_input("True or false : Regular water has a higher boiling point than Human saliva")#false
        if sixthq.lower() == "false":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif sixthq.lower()== "true":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        seventhq = raw_input("True or false : During your lifetime you will produce enough saliva to fill two swimming pools ")#true
        if seventhq.lower() == "true":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif seventhq.lower()== "false":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        eighthq = raw_input("True or false : More people died in 2015 by shark attacks than taking a selfie")#false
        if eighthq.lower() == "false":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif eighthq.lower()== "true":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        ninthq = raw_input("True or false : A lions roar can be heard from 7 miles away")#false, it is only 5 miles away
        if ninthq.lower() == "false":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif ninthq.lower()== "true":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        tenthq = raw_input("True or false : Recycling one glass jar saves enough energy to watch tv for 3 hours")#true
        if tenthq.lower() == "true":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif tenthq.lower()== "false":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        eleventhq = raw_input("True or false : A small child could swim through the veins of a blue whale")#true
        if eleventhq.lower() == "true":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif eleventhq.lower()== "false":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        twelthq = raw_input("True or false : The Twitter bird is named Larry")#true
        if twelthq.lower() == "true":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif twelthq.lower()== "false":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        thirteenthq = raw_input("True or false : If you consistently fart for 6 years and 9 months, enough gas is produced to create the energy of an atomic bomb")#true
        if thirteenthq.lower() == "true":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif thirteenthq.lower()== "false":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        fourteenthq = raw_input("True or false : The average person walks the equivalent of twice around the world in a lifetime ")#true
        if fourteenthq.lower() == "true":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif fourteenthq.lower()== "false":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        fifteenthq = raw_input("True or false : There are more than 75,000 toilet related injuries in the United States every year")#false its 40,000
        if fifteenthq.lower() == "false":
            print "Correct! It is actually 40,000. Nice one lets move to the next question!"
            score += 1
            break
        elif fifteenthq.lower()== "true":
            print "Wrong! It is actually 40,000. Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        sixteenthq = raw_input("True of false : Samuel L.Jackson requested to have a purple light saver in StarWars in order for him to accept the part as Mace Windu")#true
        if sixteenthq.lower() == "true":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif sixteenthq.lower()== "false":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        seventeenthq = raw_input("True or false : A crocodile can poke its tongue out")#false
        if seventeenthq.lower() == "false":
            print "Correct! Nice one lets move to the next question!"
            score += 1
            break
        elif seventeenthq.lower()== "true":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

    while True:
        eighteenthq = raw_input("True or false : 95% of people text things they could never say in person ")#true
        if eighteenthq.lower() == "true":
            print "Correct! Nice one lets move to the next question!"
            score +=1
            break
        elif eighteenthq.lower()== "false":
            print "Wrong! Lets move to the next question!"
            break
        else:
            print "please say 'true' or 'false' "

game() #calling the game function to work
scorend() #calling the scorend function to work

tryagain = raw_input("Do you want to try again!") #this is the try again function to see if the user wants to play again
while True:
    if tryagain.lower()=="yes":
        game()
    elif tryagain.lower() == "no":
        print "OK bye"
        exit()
    else:
        print"please say yes or no"


f = open("score.txt", "w") #my attempt at making a text file
f.write(score)
f.close()

f=open("score.txt", "r") #attempting to read the score.txt file
if f.mode == 'r':
    contents =f.read()
