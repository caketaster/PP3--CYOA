from colorama import Fore


class Player:
    """
    Creates a class of Player with the required
    variables to play the game
    """
    def __init__(self, name, royal, town):
        self.name = name
        self.town = town
        self.royal = royal


name = ""
town = ""
royal = ""


def opening():
    """
    Gives the user the choice of whether or not to start the game
    """
    start = input(Fore.RED + "Begin game? [Y/N]\n").lower()
    if start.strip() == 'y':
        player = create_player()
        name_reverse()
    else:
        print(Fore.WHITE + "It seems you did not type 'Y'...")
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
    if len(name.strip()) == 0:
        print(Fore.WHITE + "A lack of name is not a name")
        name = "Herbert"
        print("I shall call you Herbert")
    else:
        print(Fore.WHITE + f"Hmm, {initial_name}... a weak and poor name, make no mistake.") # noqa
        print(f"I shall call you {name}, 'tis far better!")
    hometown(name)
    return name


def hometown(name):
    """
    Asks for the name of the player's hometown
    and returns it as the story setting
    """
    print(Fore.RED + f"And, {name}, from where do you spring from? ")
    town = input("Which place do ye call home? \n")
    if len(town.strip()) == 0:
        print(Fore.WHITE + "If you be too ashamed to tell me, I shall assume it is a terrible place, perhaps Swindon.") # noqa
        town = "Swindon"
        print("And that den of poverty and sin is the setting for our tale today...") # noqa
        print("")
    else:
        print(Fore.WHITE + f"{town}! A vile place full of inbred and ugly folk!") # noqa
        print("And by coincidence the setting for our tale today...")
        print("")
    prince_princess(town, name)
    return town


def prince_princess(town, name):
    """
    Player chooses whether to rescue a prince or a princess
    """
    print(f"The rooster crows in the grotty hamlet of {town}.")
    print(f"You, {name}, roll from your filthy woven mattress and pull your unwashed rags over your unwashed head. Lice scatter.") # noqa
    print("A newspaper falls through your letterbox,")
    print("you look at the front page")
    print("A member of the royal household has been kidnapped!")
    print("Someone is going to have to rescue him, or her. ")
    print("Your filthy thumbprint has smeared the details...")
    royal_choice = ""
    while royal_choice.strip() != "1" or "2":
        royal_choice = input(Fore.RED + "Is the kidnapped royal a PRINCE(1) or a PRINCESS(2)? \n") # noqa
        if royal_choice.strip() == "1":
            royal = "prince"
            print(Fore.WHITE + 'The newspaper reads: ')
            print('"The handsome prince, covered in six-packs & pectorals,')
            print("intelligent and witty and not a pimple on his skin, ")
            print("was just this morning kidnapped from the castle. ")
            print("Whomsoever dost rescue him surely shall be handsomely rewarded") # noqa
            print("with a kiss on their haggard face, a bag of silver coin, ")
            print('or whatever reward the rescuer dost desire."')
            first(name, royal)
            return royal
        elif royal_choice.strip() == "2":
            royal = "princess"
            print(Fore.WHITE + 'The newspaper reads:')
            print('"The smouldering princess, veritably covered in shapely curves') # noqa
            print("with a sharp and clever wit")
            print("smooth of skin and the most lovely in the land,")
            print("was this morning kidnapped from the castle.")
            print("Whomsoever dost rescue her surely shall be handsomely rewarded") # noqa
            print("with a kiss on their spotty cheek, a bag of silver coin, ")
            print('or whatever reward the rescuer dost desire."')
            first(name, royal)
            return royal
        else:
            print("Your chubby peasantly fingers have missed the relevant keys. ") # noqa
            print("Attempt to uncross thine eyes and try again.")


def create_player():
    """
    Creates an instance of the Player class
    to store and return the needed variables
    """
    global name, town, royal
    name = name_reverse()
    town = hometown(name)
    royal = prince_princess(town, name)
    player = Player(name, royal, town)
    return player


def first():
    """
    First choice - palace or pub
    """
    print(f"So it is decided that YOU, {name}, will rescue the {royal}.")
    print("You waddle down the stairs and flop onto the street.")
    print(Fore.RED + "In which direction will you turn?")
    first_choice = ""
    while first_choice.strip() != "1" or "2":
        first_choice = input(Fore.RED + "Toward the PALACE(1) or the PUB(2)? \n") # noqa
        if first_choice == "1":
            palace(player)
        elif first_choice == "2":
            pub(player)
        else:
            print(Fore.WHITE + "Again your foolishness confounds me!")
            

def palace(player):
    """
    The initial palace path
    """
    print(Fore.WHITE + f"Let’s face it, if the {royal} was at the palace they wouldn’t be missing, would they? Cursing your lack of intelligence, you sit down for a while to think. There’s a chance the kidnappers might have taken the {royal} away in a stagecoach, so the logical thing would be to go to the CROSSROADS and search. But on the other hand you haven’t had any ale or mead for what feels like hours, and there’s a very slim chance the {royal} might have just slipped out for a cheeky gin and soda.") # noqa
    print(Fore.RED + "Where dost thou wish to turn?")
    palace_choice = ""
    while palace_choice.strip() != "1" or "2":
        palace_choice = input(Fore.RED + "Toward the CROSSROADS(1) or the PUB(2)\n") # noqa
        if palace_choice == "1":
            crossroads(player)
        elif palace_choice == "2":
            pub(player)
        else:
            print(Fore.WHITE + "The decision is not difficult for folk of sound mind.") # noqa
        

def pub(player):
    """
    The initial pub path
    """
    print(Fore.WHITE + f"You barrel into the pub and order a flagoon of wine. Followed by another flagoon of wine. The {royal} does not seem to be in the pub, so you have another drink. You fall asleep. You awake mid-afternoon feeling sure that you had some kind of mission to fulfil.") # noqa
    print(Fore.RED + "Where next, friend?")
    pub_choice = ""
    while pub_choice != "1" or "2":
        pub_choice = input(Fore.RED + "Will ye go to the PALACE(1), the CROSSROADS(2), or stay here(3)?\n") # noqa
        if pub_choice.strip() == "1":
            palace(royal)
        elif pub_choice.strip() == "2":
            crossroads()
        elif pub_choice.strip() == "3":
            pub_two(royal)
        else:
            print(Fore.WHITE + "Try again...")


def pub_two(player):
    """
    The second Pub choice, leading to Game Over
    """
    print(Fore.WHITE + "You order a bottle of mead, and then another.")
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
    print(Fore.YELLOW + "GAME OVER.")
    game_over()


def crossroads(player):
    """
    The Crossroads choice, on the correct path to victory
    """
    print(Fore.WHITE + "Lumbering down the lane, nature calls and you feel the need to relieve yourself. Will you do it in the bushes, or urinate into your own (already filthy) trousers?") # noqa
    wee_choice = ""
    while wee_choice.strip() != "1" or "2":
        wee_choice = input(Fore.RED + "Type [1] for in the BUSHES or [2] for WETTING YOURSELF: \n") # noqa
        if wee_choice.strip() == "1":
            bushes(royal)
        elif wee_choice.strip() == "2":
            carriage(name, royal)
        else:
            print(Fore.WHITE + "Thou do not hast time to fool around with a bladder this full") # noqa


def bushes(player):
    """
    The wrong choice, leading to a GAME OVER
    """
    print(Fore.WHITE + f"After doing what you have to do, you run out again toward the crossroads. In the distance the carriage rounds a bend - you're too late! Your rare thought of personal hygiene has allowed the kidnappers of the {royal} to escape.") # noqa
    print(Fore.WHITE + "You trudge home, vowing never again to pee outside of your own clothing.") # noqa
    print(Fore.YELLOW + "GAME OVER.")
    game_over()


def carriage(player):
    """
    Player has a chance to intercept the fleeing carriage
    """
    print(Fore.WHITE + f"Trousers full of wee, you, {name}, round the bend as the stagecoach approaches, the {royal} tied up in the back seat. You'll only have one chance to stop the carriage!") # noqa
    print("In front of you, you see a rock, a stick and a knife.")
    print("You decide to throw one implement at the kidnappers to stop them, but which will you choose...?") # noqa
    weapon = ""
    while weapon != "1" or "2" or "3":
        weapon = input(Fore.RED + "Will thee toss the rock [1], the stick [2] or the knife [3]? \n") # noqa
        if weapon.strip() == "1":
            rock(royal, name)
        elif weapon.strip() == "2":
            stick()
        elif weapon.strip() == "3":
            knife(royal)
        else:
            print(Fore.WHITE + "The carriage is moving fast, make your choice")


def rock(player):
    """
    The wrong weapon, leading to a Game Over
    """
    print(Fore.WHITE + f"You clumsily hurl the rock carriageward. It passes between the heads of the kidnappers and strikes the {royal} clean between the eyes!") # noqa
    print("The carriage barrels into the distance, the comatose royal lolling side to side in the rear.") # noqa
    print("A cloud of dust envelopes you as it passes, making you cough and vomit.") # noqa
    print(f"{name}, with your boss-eyed throwing style, you've blown it.")
    print(Fore.YELLOW + "GAME OVER.")
    game_over()


def knife(player):
    """
    The wrong weapon, leading to a Game Over
    """
    print(Fore.WHITE + "You leap, shrieking and brandishing the knife! But as you pull back the blade to hurl carriageward you embed it in your own bulbous forehead.") # noqa
    print(f"You slump to the ground as the kidnappers' carriage bearing the {royal} steams past.") # noqa
    print("Home you stagger, dagger still stuck in your spotty head.")
    print("There'll be no rescue today.")
    print(Fore.YELLOW + "GAME OVER.")
    game_over()


def stick():
    """
    The correct weapon, leading to a victory of some sort
    """
    print(f"The stick spins through the air, bounces and flies between the spokes of the stagecoach's front wheel. The stagecoach swerves violently, throwing the kidnappers into the bushes. As it wobbles to a halt, the {royal} steps gingerly from the carriage and sizes you up.") # noqa
    print(f"You annouce yourself, 'I am {name} from the parish of {town}, pleased to rescue you.' The {royal} knows that they're going to have to dish out a reward.") # noqa
    reward = ""
    while reward != "1" or "2":
        reward = input(Fore.RED + "Will you ask for a bag or golden coins [1], or a kiss [2] on the face?") # noqa
        if reward.strip() == "1":
            print(f"The {royal} digs around in their pocket and pulls out a bag of coins. They hand it to you without a word, dust themselves down and start the long walk back toward the palace.") # noqa
            print("You're rich beyond your wildest dreams. Already your head is swimming with ideas on upgrading your hovel and buying a second set of trousers.") # noqa
            print("You wander home, smiling happily")
            print(Fore.GREEN + "THE END")
        elif reward.strip() == "2":
            print(f"You pucker up and lean in. The horrified {royal} staggers back, clasping at the air.") # noqa
            print(f"The {royal} empties their pockets, pulling out two large bags of gold coins.") # noqa
            reward_two = ""
            while reward_two != "1" or "2":
                reward_two = input(Fore.RED + "Will ye accept the money [1] or insist on a kiss [2]?") # noqa
                if reward_two == "1":
                    print(f"The {royal} gladly shoves the bags into your sweaty hands and runs off before you change your mind.") # noqa
                    print("You're rich beyond double what you could dream. Already you're dreaming of a whole new set of clothes, a larger hovel, and maybe a BMW. Although you regret not having a snog, you're happier than you've ever been.") # noqa
                    print(Fore.GREEN + "THE END")
                    quit()
                elif reward_two == "2":
                    print(f"The {royal}'s face contorts with disgust, but they dutifully lean in to meet your scabby mouth. You touch lips. Before you've even had a chance to really enjoy the kiss they're reeling back, coughing and wiping their face, before turning tail and running toward the palace.") # noqa
                    print("Even though it was short, you enjoyed what was your first kiss (unless you count that time with the homeless dog) and have never been happier.") # noqa
                    print("You float home on a cloud of joy.")
                    print(Fore.GREEN + "THE END")
                    quit()
                else:
                    print("Do not let your joy get the better of you, steady yourself and choose one of the two options available.") # noqa
        else:
            print("On offer: money or possible love. What will ye decide?")


def game_over():
    """
    Function to run when player hits a Game Over screen.
    Restarts game
    """
    print("Run the game again to re-play")
    quit()


opening()


# Write your code to expect a terminal of 80 characters wide and 24 rows high

# QUESTIONS:
# Variables (name, royal, hometown) are not *always* carrying over into new functions. What am I doing wrong? Something to do with local vs. global scope - use classes!!


# TO DO:
# Deploy early (screenshot the method)
# Make the words 'type' in real time (do later - it slows down testing)
# Pauses between certain lines
# You can make what the user enters more clear to vs the story text  and use red/yellow for correct incorrect messaging.
    # Colorama is really easy to install and then use with string based messages which you have in your program.
    # You’ll have to pip install colorama then freeze your requirements.txt again but it’s worth it.
    # Here’s an article about color in python, jump to the colorama bit:
    # https://www.geeksforgeeks.org/print-colors-python-terminal/
# Use fancy fonts for welcome and good bye
    # Here’s an article about fancy fonts in python: https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/
    # You basically install pyfiglet and it can make your letters bubbly and stand out more.
# ASCII art
    # Search for ascii art generator from image and you will get lots of results on how to convert images to ascii art. It might help you add some graphic components potentially. I’d save any ascii_art into an ascii_art.py file and import them as needed so they don’t mess up your main run.py file.

    # https://convertcase.net/ascii-art-generator/ works pretty well for gray scale,

    # this one works for color images: https://www.meridianoutpost.com/resources/etools/calculators/downloader-ascii-art.php 


# while loop OR separate function for questions so that you can re-ask questions  OK
# .strip() for choices   OK
 # noqa at the end of long lines  OK


#  pp2 - remove 'onclick' from html buttons - should work. Try then send to Malia