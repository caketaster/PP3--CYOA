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
        hometown(name)
    else:
        print("It seems you did not type 'Y'...")
        print("I'm struggling to understand why you're here if not to play.")
        opening()


# https://www.w3schools.com/python/python_howto_reverse_string.asp
def name_reverse():
    """
    Reverses the player name - this reversed name is the name
    the program will use for the player
    """
    initial_name = input("Pray tell, what be thine name? \n")
    reversed_name = initial_name[::-1]
    name = reversed_name.capitalize()
    print(f"Hmm, {initial_name}... a weak and poor name, make no mistake.")
    print(f"I shall call you {name}, 'tis far better!")
    hometown(name)
    return name


def hometown(name):
    """
    Asks for the name of the player's hometown
    and returns it as the story setting
    """
    print(f"And, {name}, from where do you spring from? ")
    town = input("Which place do ye call home? \n")
    print(f"{town}! A vile place full of inbred and ugly folk!")
    print("And by coincidence the setting for our tale today...")
    prince_princess(town, name)
    return town


def prince_princess(town, name):
    """
    Player chooses whether to rescue a prince or a princess
    """
    print(f"The rooster crows in the grotty hamlet of {town}.")
    print(f"You, {name}, roll from your filthy woven mattress and pull your unwashed rags over your unwashed head. Lice scatter.")
    print("A newspaper falls through your letterbox,")
    print("you look at the front page")
    print("A member of the royal household has been kidnapped!")
    print("Someone is going to have to rescue him, or her. ")
    print("Your filthy thumbprint has smeared the details...")
    royal_choice = input("Is the kidnapped royal a PRINCE(1) or a PRINCESS(2)? \n")
    if royal_choice == "1":
        royal = "prince"
        print('The newspaper reads: ')
        print('"The handsome prince, covered in six-packs & pectorals,')
        print("intelligent and witty and not a pimple on his skin, ")
        print("was just this morning kidnapped from the castle. ")
        print("Whomsoever dost rescue him surely shall be handsomely rewarded")
        print("with a kiss on their haggard face, a bag of silver coin, ")
        print('or whatever reward the rescuer dost desire."')
        first(name, royal)
        return royal
    elif royal_choice == "2":
        royal = "princess"
        print('The newspaper reads:')
        print('"The smouldering princess, veritably covered in shapely curves')
        print("with a sharp and clever wit")
        print("smooth of skin and the most lovely in the land,")
        print("was this morning kidnapped from the castle.")
        print("Whomsoever dost rescue her surely shall be handsomely rewarded")
        print("with a kiss on their spotty cheek, a bag of silver coin, ")
        print('or whatever reward the rescuer dost desire."')
        first(name, royal)
        return royal
    else:
        print("Your chubby peasantly fingers have missed the relevant keys. ")
        print("Attempt to uncross thine eyes and try again.")
        royal_choice = input("Is the kidnapped royal a PRINCE(1) or a PRINCESS(2)? \n")
        


def first(name, royal):
    """
    First choice - palace or pub
    """
    print(f"So it is decided that YOU, {name}, will rescue the {royal}.")
    print("You waddle down the stairs and flop onto the street.")
    print("In which direction will you turn?")
    first_choice = input("Toward the PALACE(1) or the PUB(2)? \n")
    if first_choice == "1":
        palace(royal)
    elif first_choice == "2":
        pub(royal)
    else:
        print("Again your foolishness confounds me!")
        first_choice = input("Type 1 for PALACE, 2 for PUB: \n")


def palace(royal):
    """
    The initial palace path
    """
    print(f"Let’s face it, if the {royal} was at the palace they wouldn’t be missing, would they? Cursing your lack of intelligence, you sit down for a while to think. There’s a chance the kidnappers might have taken the {royal} away in a stagecoach, so the logical thing would be to go to the CROSSROADS and search. But on the other hand you haven’t had any ale or mead for what feels like hours, and there’s a very slim chance the {royal} might have just slipped out for a cheeky gin and soda.")
    print("Where dost thou wish to turn?")
    palace_choice = input("Toward the CROSSROADS(1) or the PUB(2)\n")
    if palace_choice == "1":
        crossroads()
    elif palace_choice == "2":
        pub(royal)
    else:
        palace_choice = input("")


def pub(royal):
    """
    The initial pub path
    """
    print(f"You barrel into the pub and order a flagoon of wine. Followed by another flagoon of wine. The {royal} does not seem to be in the pub, so you have another drink. You fall asleep. You awake mid-afternoon feeling sure that you had some kind of mission to fulfil.")
    print("Where next, friend?")
    pub_choice = input("The PALACE(1), CROSSROADS(2), or stay here(3)?\n")
    if pub_choice == "1":
        palace(royal)
    elif pub_choice == "2":
        crossroads()
    elif pub_choice == "3":
        pub_two(royal)
    else:
        pub_choice = input("")


def pub_two():
    """
    The second Pub choice, leading to Game Over
    """
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
    print("Lumbering down the lane, nature calls and you feel the need to relieve yourself. Will you do it in the bushes, or urinate into your own (already filthy) trousers?")
    wee_choice = input("Type [1] for in the BUSHES or [2] for WETTING YOURSELF: \n")
    if wee_choice == "1":
        bushes(royal)
    elif wee_choice == "2":
        carriage(name, royal)


def bushes(royal):
    """
    The wrong choice, leading to a GAME OVER
    """
    print(f"After doing what you have to do, you run out again toward the crossroads. In the distance the carriage rounds a bend - you're too late! Your rare thought of personal hygiene has allowed the kidnappers of the {royal} to escape.")
    print("You trudge home, vowing never again to pee outside of your own clothing.")
    print("GAME OVER.")


def carriage(name, royal):
    """
    Player has a chance to intercept the fleeing carriage
    """
    print(f"Trousers full of wee, you, {name}, round the bend as the carriage approaches, the {royal} tied up in the back seat. You'll only have one chance to stop the carriage!")
    print("In front of you, you see a rock, a stick and a knife.")
    print("You decide to throw one implement at the kidnappers to stop them, but which will you choose...?")
    weapon = input("Will thee toss the rock [1], the stick [2] or the knife [3]?")
    if weapon == "1":
        rock(royal, name)
    elif weapon == "2":
        stick()
    elif weapon == "3":
        knife(royal)


def rock(royal, name):
    """
    The wrong weapon, leading to a Game Over
    """
    print(f"You clumsily hurl the rock carriageward. It passes between the heads of the kidnappers and strikes the {royal} clean between the eyes!")
    print("The carriage barrels into the distance, the comatose royal lolling side to side in the rear.")
    print("A cloud of dust envelopes you as it passes, making you cough and vomit.")
    print(f"{name}, with your boss-eyed throwing style, you've blown it.")
    print("GAME OVER.")


def knife(royal):
    """
    The wrong weapon, leading to a Game Over
    """
    print("You leap, shrieking and brandishing the knife! But as you pull back the blade to hurl carriageward you embed it in your own bulbous forehead.")
    print(f"You slump to the ground as the kidnappers' carriage bearing the {royal} steams past.")
    print("Home you stagger, dagger still stuck in your spotty head.")
    print("There'll be no rescue today.")
    print("GAME OVER.")


def stick():
    """
    The correct weapon, leading to a victory of some sort
    """



opening()



# Write your code to expect a terminal of 80 characters wide and 24 rows high



# QUESTIONS:
# Do I need to keep my lines under 80 chars? Or can I just allow them to wrap?
# How do I end the game (using break) at Game Over points?
# Variables (name, royal, hometown) are not *always* carrying over into new functions. What am I doing wrong? Something to do with local vs. global scope
# Can I use classes here..? Seems to be working without them but the code is quite basic as is. Is it enough?
# If you don't type 1 or 2 I want the question to be re-asked, but it just breaks out (e.g. prince_princess function)


# TO DO:
# Deploy early (screenshot the method)
# Make the words 'type' in real time (do later - it slows down testing)
# Pauses between certain lines