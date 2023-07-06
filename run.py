# def Player():
#     def __init__(self, name, hometown):
#         self.name = name
#         self.hometown = hometown


name = ""
town = ""
royal = ""


def opening():
    """
    Gives the user the choice of whether or not to start the game
    """
    start = input("Begin game? [Y/N]").lower()
    if start == 'y':
        name_reverse()
        hometown()
    else:
        print("It seems you did not type 'Y'...")
        print("I'm struggling to understand why you're here if not to play.")


# https://www.w3schools.com/python/python_howto_reverse_string.asp
def name_reverse():
    """
    Reverses the player name - this reversed name is the name
    the program will use for the player
    """
    global name
    initial_name = input("Pray tell, what be thine name? \n")
    reversed_name = initial_name[::-1]
    name = reversed_name.capitalize()
    print(f"Hmm, {initial_name}... a weak and poor name, make no mistake.")
    print(f"I shall call you {name}, 'tis far better!")
    return name

# time - words to 'type out', & time spaces between some lines

# do i need this self.name here?


def hometown():
    """
    Asks for the name of the player's hometown
    and returns it as the story setting
    """
    global name
    print(f"And, {name}, from where do you spring from? ")
    town = input("Which place do ye call home? \n")
    print(f"{town}! A vile place full of inbred and ugly folk!")
    print("And by coincidence the setting for our tale today...")
    return town


def prince_princess():
    """
    Player chooses whether to rescue a prince or a princess
    """
    global royal
    print(f"The rooster crows in the grotty hamlet of {town}.")
    print(f"You, {name}, roll from your filthy woven mattress")
    print("and pull your unwashed rags over your unwashed head. Lice scatter.")
    print("A newspaper falls through your letterbox,")
    print("you look at the front page")
    print("A member of the royal household has been kidnapped!")
    print("Someone is going to have to rescue him, or her. ")
    royal_choice = input("Your filthy thumbprint has smeared the details...")
    print("is the kidnapped royal a PRINCE(1) or a PRINCESS(2)? \n")
    if royal_choice == "1":
        royal = "prince"
        print('The newspaper reads: ')
        print('"The handsome prince, covered in six-packs & pectorals,')
        print("intelligent and witty and not a pimple on his skin, ")
        print("was just this morning kidnapped from the castle. ")
        print("Whomsoever dost rescue him surely shall be handsomely rewarded")
        print("with a kiss on their haggard face, a bag of silver coin, ")
        print('or whatever reward the rescuer dost desire."')
        return royal
    elif royal == "2":
        royal = "princess"
        print('The newspaper reads:')
        print('"The smouldering princess, veritably covered in shapely curves')
        print("with a sharp and clever wit")
        print("smooth of skin and the most lovely in the land,")
        print("was this morning kidnapped from the castle.")
        print("Whomsoever dost rescue her surely shall be handsomely rewarded")
        print("with a kiss on their spotty cheek, a bag of silver coin, ")
        print('or whatever reward the rescuer dost desire."')
        return royal
    else:
        print("Your chubby peasantly fingers have missed the relevant keys. ")
        print("Attempt to uncross thine eyes and try again.")
        royal_choice = input("Hit either 1 for a PRINCE or 2 for a PRINCESS\n")


def first():
    """
    First choice - palace or pub
    """
    print(f"So it is decided that YOU, {name}, will rescue the {royal}.")
    print("You waddle down the stairs and flop onto the street.")
    print("In which direction will you turn?")
    first_choice = input("Toward the PALACE(1) or the PUB(2)? \n")
    if first_choice == "1":
        palace()
    elif first_choice == "2":
        pub()
    else:
        print("Again your foolishness confounds me!")
        first_choice = input("Type 1 for PALACE, 2 for PUB: \n")


def palace():
    """
    The initial palace path
    """
    print("Where dost thou wish to turn?")
    palace_choice = input("Toward the CROSSROADS(1) or the PUB(2)\n")
    if palace_choice == "1":
        crossroads()
    elif palace_choice == "2":
        pub()
    else:
        palace_choice = input("")


def pub():
    """
    The initial pub path
    """
    print("Where next, friend?")
    pub_choice = input("The PALACE(1), CROSSROADS(2), or stay here(3)?\n")
    if pub_choice == "1":
        palace()
    elif pub_choice == "2":
        crossroads()
    elif pub_choice == "3":
        pub_two()
    else:
        pub_choice = input("")


def pub_two():
    """
    The second Pub choice, leading to Game Over
    """
    print("You order a bottle of mead, and then another.")
    print("You order a bottle of mead, and then another.")
    print("You play pool. You fall over.")
    print("You play darts and hit the barmaid with a dart.")
    print("Eventually everything goes cloudy.")
    print("You awaken 2 days hence in your own bed, ")
    print("with your trousers on backwards and socks on your hands.")
    print("Your head throbs. You pick up the newspaper, then drop it")
    print("because you still have socks on your hands.")
    print("Regardless, you persevere, flopping the page over with your")
    print(f"be-socked hands. The headline says the {royal} has been")
    print("rescued by another grimy pauper, who is now being")
    print("showered with romantic favours and gifts of silver and gold.")
    print("You missed your chance buddy.")
    print("You peel back your vomit-stained sheets and go back to bed.")
    print("GAME OVER.")


def crossroads():
    """
    The Crossroads choice, on the correct path to victory
    """


opening()
prince_princess()
first()

# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
