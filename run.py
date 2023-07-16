# Import relevant libraries and modules
from colorama import Fore
import sys
import time
import pyfiglet


class AdventureGame:
    """
    Creates a class of Player with the required
    variables to play the game
    """

    def __init__(self):
        self.name = ""
        self.town = ""
        self.royal = ""

    def opening(self):
        """
        Gives the user the 'choice' of whether or not to start the game
        """
        start = input(Fore.RED + "Begin game? [Y/N]\n").lower().strip()
        if start == 'y':
            self.name_reverse()
        else:
            print_slowly(Fore.WHITE + "It seems you did not type 'Y'...")
            time.sleep(0.5)
            print_slowly("I'm struggling to understand why you're here if not to play.")  # noqa

            print()
            self.opening()

    # https://www.w3schools.com/python/python_howto_reverse_string.asp
    def name_reverse(self):
        """
        Reverses the player name - this reversed name is the name
        the program will use for the player
        """
        initial_name = input("Pray tell, what be thine name? \n").strip()
        reversed_name = initial_name[::-1]
        self.name = reversed_name.capitalize()
        if len(self.name) == 0:
            print_slowly(Fore.WHITE + "A lack of name is not a name")
            self.name = "Herbert"
            time.sleep(0.5)
            print_slowly("I shall call you Herbert")
        else:
            print_slowly(Fore.WHITE + f"Hmm, {initial_name} ... a weak and poor name, make no mistake.")  # noqa
            time.sleep(0.5)
            print_slowly(f"I shall call you {self.name}, 'tis far better!")
            time.sleep(0.4)
            print_slowly("And I think it sounds kind of Welsh.")

        self.hometown()
        return

    def hometown(self):
        """
        Asks for the name of the player's hometown
        and returns it as the story setting
        """
        print_slowly(Fore.WHITE + f"And, {self.name}, from where do you spring from? ")  # noqa

        self.town = input(Fore.RED + "Which town do ye call home? \n").strip()
        if len(self.town) == 0:
            print_slowly(Fore.WHITE + "If you be too ashamed to tell me, I shall assume it is a terrible place, perhaps Swindon.")  # noqa

            self.town = "Swindon"
            time.sleep(0.5)
            print_slowly("And that den of poverty and sin is the setting for our tale today...")  # noqa

            time.sleep(1)
            print()
        else:
            print_slowly(Fore.WHITE + f"{self.town}! A vile place full of inbred and ugly folk!")  # noqa

            time.sleep(0.5)
            print_slowly("And by coincidence the setting for our tale today...")  # noqa

            print()
        self.prince_princess()
        return

    def prince_princess(self):
        """
        Player chooses whether to rescue a prince or a princess
        """
        print_slowly(f"The rooster crows in the grotty hamlet of {self.town}.")

        time.sleep(0.5)
        print_slowly(f"You, {self.name}, roll from your filthy woven mattress and pull your unwashed rags over your unwashed head. Lice scatter.")  # noqa

        time.sleep(0.5)
        print_slowly("A newspaper falls through your letterbox,")

        print_slowly("you look at the front page,")
        time.sleep(0.5)
        print_slowly("A member of the royal household has been kidnapped!")

        time.sleep(0.5)
        print_slowly("Someone is going to have to rescue him, or her. ")

        print_slowly("Your filthy thumbprint has smeared the details...")

        royal_choice = ""
        while royal_choice != "1" or "2":
            royal_choice = input(Fore.RED + "Is the kidnapped royal a PRINCE(1) or a PRINCESS(2)? \n").strip()  # noqa
            if royal_choice == "1":
                self.royal = "prince"
                print_slowly(Fore.WHITE + 'The newspaper reads: ')

                print_slowly('"The handsome prince, covered in six-packs & pectorals,')  # noqa

                print_slowly("intelligent and witty and nary a pimple on his skin, ")  # noqa

                print_slowly("was just this morning kidnapped from the palace. ")  # noqa

                time.sleep(0.5)
                print_slowly("Whomsoever dost rescue him surely shall be handsomely rewarded")  # noqa

                print_slowly("with a kiss on their haggard face, a bag of coin, ")  # noqa

                print_slowly('or whatever reward the rescuer dost desire."')

                print()
                time.sleep(0.8)
                self.first()
                return
            elif royal_choice == "2":
                self.royal = "princess"
                print_slowly(Fore.WHITE + 'The newspaper reads:')

                print_slowly('"The smouldering princess, veritably covered in shapely curves')  # noqa

                print_slowly("with a sharp and clever wit")

                print_slowly("smooth of skin and the most lovely in the land,")

                print_slowly("was this morning kidnapped from the castle.")

                time.sleep(0.5)
                print_slowly("Whomsoever dost rescue her surely shall be handsomely rewarded")  # noqa

                print_slowly("with a kiss on their spotty cheek, a bag of coin, ")  # noqa

                print_slowly('or whatever reward the rescuer dost desire."')

                print()
                time.sleep(0.8)
                self.first()
                return
            else:
                print_slowly("Your chubby peasantly fingers have missed the relevant keys. ")  # noqa

                time.sleep(0.5)
                print_slowly("Attempt to uncross thine eyes and try again.")

    def first(self):
        """
        First choice - palace or pub
        """
        print_slowly(f"So it is decided that YOU, {self.name}, will rescue the {self.royal}.")  # noqa

        print_slowly("You waddle down the stairs and flop onto the street.")

        print(Fore.RED + "In which direction will you turn?")
        first_choice = ""
        while first_choice != "1" or "2":
            first_choice = input(Fore.RED + "Toward the PALACE(1) or the PUB(2)? \n").strip()  # noqa
            if first_choice == "1":
                self.palace()
            elif first_choice == "2":
                self.pub()
            else:
                print_slowly(Fore.WHITE + "Again your foolishness confounds me!")  # noqa

    def palace(self):
        """
        The initial palace path
        """
        print_slowly(Fore.WHITE + f"Let's face it, if the {self.royal} was at the palace they wouldn't be missing, would they? Cursing your lack of intelligence, you sit down for a while to think. There's a chance the kidnappers might have taken the {self.royal} away in a stagecoach, so the logical thing would be to go to the CROSSROADS and search. But on the other hand you haven't had any ale or mead for what feels like hours, and there's a very slim chance the {self.royal} might have just slipped out for a cheeky gin and soda.")  # noqa

        print(Fore.RED + "Where dost thou wish to turn?")
        palace_choice = ""
        while palace_choice != "1" or "2":
            palace_choice = input(Fore.RED + "Toward the CROSSROADS(1) or the PUB(2)\n").strip()  # noqa
            if palace_choice == "1":
                self.crossroads()
            elif palace_choice == "2":
                self.pub()
            else:
                print_slowly(Fore.WHITE + "The decision is not difficult for folk of sound mind.")  # noqa

    def pub(self):
        """
        The initial pub path
        """
        print_slowly(Fore.WHITE + f"You barrel into the pub and order a flagoon of wine. Followed by another flagoon of wine. The {self.royal} does not seem to be in the pub, so you have another drink. You fall asleep. You awake mid-afternoon feeling sure that you had some kind of mission to fulfil.")  # noqa

        time.sleep(0.5)
        print(Fore.RED + "Where next, friend?")
        pub_choice = ""
        while pub_choice != "1" or "2":
            pub_choice = input(
                Fore.RED + "Will ye go to the PALACE(1), the CROSSROADS(2), or stay here(3)?\n").strip()  # noqa
            if pub_choice == "1":
                self.palace()
            elif pub_choice == "2":
                self.crossroads()
            elif pub_choice == "3":
                self.pub_two()
            else:
                print_slowly(Fore.WHITE + "Try again...")

    def pub_two(self):
        """
        The second Pub choice, leading to Game Over
        """
        print_slowly(Fore.WHITE + "You order a bottle of mead, and then another.")  # noqa

        print_slowly("You play pool. You fall over.")

        time.sleep(0.4)
        print_slowly("You play darts and hit the barmaid with a dart.")

        print_slowly("Eventually everything goes cloudy.")

        time.sleep(0.4)
        print_slowly("You awaken 2 days hence in your own bed, ")

        print_slowly("with your trousers on backwards and socks on your hands.")  # noqa

        print_slowly("Your head throbs. You pick up the newspaper, then drop it")  # noqa

        print_slowly("because you still have socks on your hands.")

        time.sleep(0.4)
        print_slowly("Regardless, you persevere, flopping the page over with your")  # noqa

        print_slowly(f"be-socked hands. The headline says the {self.royal} has been")  # noqa

        print_slowly("rescued by another grimy pauper, who is now being")

        print_slowly("showered with romantic favours and gifts of silver and gold.")  # noqa

        time.sleep(0.5)
        print_slowly(f"You missed your chance {self.name}.")

        time.sleep(0.5)
        print_slowly("You peel back your vomit-stained sheets and go back to bed.")  # noqa

        print(Fore.YELLOW + "GAME OVER.")
        self.game_over()

    def crossroads(self):
        """
        The Crossroads choice, on the correct path to victory
        """
        print_slowly(Fore.WHITE + "Lumbering down the lane, nature calls and you feel the need to relieve yourself. Will you do it in the bushes, or urinate into your own (already filthy) trousers?")  # noqa

        wee_choice = ""
        while wee_choice != "1" or "2":
            wee_choice = input(Fore.RED + "Type [1] for in the BUSHES or [2] for WETTING YOURSELF: \n").strip()  # noqa
            if wee_choice == "1":
                self.bushes()
            elif wee_choice == "2":
                self.carriage()
            else:
                print_slowly(Fore.WHITE + "Thou do not hast time to fool around with a bladder this full")  # noqa

    def bushes(self):
        """
        The wrong choice, leading to a GAME OVER
        """
        print_slowly(Fore.WHITE + f"After doing what you have to do, you run out again toward the crossroads. In the distance the carriage rounds a bend - you're too late! Your rare thought of personal hygiene has allowed the kidnappers of the {self.royal} to escape.")  # noqa

        time.sleep(0.5)
        print_slowly(Fore.WHITE + "You trudge home, vowing never again to pee outside of your own clothing.")  # noqa

        time.sleep(1)
        print(Fore.YELLOW + "GAME OVER.")
        self.game_over()

    def carriage(self):
        """
        Player has a chance to intercept the fleeing carriage
        """
        print_slowly(Fore.WHITE + f"Trousers full of wee, you, {self.name}, round the bend as the stagecoach approaches, the {self.royal} tied up in the back seat. You'll only have one chance to stop the carriage!")  # noqa

        time.sleep(0.5)
        print_slowly("In front of you, you see a rock, a stick and a knife.")

        print_slowly(
            "You have time to throw but one implement at the kidnappers to stop them, but which will you choose...?")  # noqa

        weapon = ""
        while weapon != "1" or "2" or "3":
            weapon = input(Fore.RED + "Will thee toss the ROCK [1], the STICK [2] or the KNIFE [3]? \n").strip()  # noqa
            if weapon == "1":
                self.rock()
            elif weapon == "2":
                self.stick()
            elif weapon == "3":
                self.knife()
            else:
                print_slowly(Fore.WHITE + "The carriage is moving fast, make your choice")  # noqa

    def rock(self):
        """
        The wrong weapon, leading to a Game Over
        """
        print_slowly(Fore.WHITE + f"You clumsily hurl the rock carriageward. It passes between the heads of the kidnappers and strikes the {self.royal} clean between the eyes!")  # noqa

        time.sleep(0.5)
        print_slowly("The carriage barrels into the distance, the comatose royal lolling side to side in the rear.")  # noqa

        print_slowly("A cloud of dust envelopes you as it passes, making you cough and vomit.")  # noqa

        print_slowly(f"{self.name}, with your boss-eyed throwing style, {self.name} you've blown it.")  # noqa

        time.sleep(1)
        print(Fore.YELLOW + "GAME OVER.")
        self.game_over()

    def knife(self):
        """
        The wrong weapon, leading to a Game Over
        """
        print_slowly(Fore.WHITE + "You leap, shrieking and brandishing the knife! But as you pull back the blade to hurl carriageward you embed it in your own bulbous forehead.")  # noqa

        time.sleep(0.5)
        print_slowly(f"You slump to the ground as the kidnappers' carriage bearing the {self.royal} steams past.")  # noqa

        print_slowly("Home you stagger, dagger still stuck in your spotty mush.")  # noqa

        time.sleep(0.5)
        print_slowly("There'll be no rescue today.")

        time.sleep(1)
        print(Fore.YELLOW + "GAME OVER.")
        self.game_over()

    def stick(self):
        """
        The correct weapon, leading to a victory of some sort
        """
        print_slowly(Fore.WHITE + f"The stick spins through the air, bounces and flies between the spokes of the stagecoach's front wheel. The stagecoach swerves violently, throwing the kidnappers into the bushes. As it wobbles to a halt, the {self.royal} steps gingerly from the carriage and sizes you up.")  # noqa

        print_slowly(f"You annouce yourself, 'I am {self.name} from the parish of {self.town}, pleased to rescue you.' The {self.royal} knows that they're going to have to dish out a reward.")  # noqa

        reward = ""
        while reward != "1" or "2":
            reward = input(
                Fore.RED + "Will you ask for a BAG OF GOLDEN COINS [1], or a KISS [2] on the face? \n").strip()  # noqa
            if reward == "1":
                print_slowly(Fore.WHITE + f"""The {self.royal} digs around in their pocket and pulls out a bag of coins. 
                They hand it to you without a word, dust themselves down and start the long walk 
                back toward the palace.""")  # noqa

                time.sleep(0.5)
                print_slowly("You're rich beyond your wildest dreams. Already your head is swimming with ideas on upgrading your hovel and buying a second set of trousers.")  # noqa

                time.sleep(0.5)
                print_slowly("You wander home, smiling happily")
                time.sleep(1)
                print(Fore.GREEN + "THE END")
            elif reward == "2":
                print_slowly(Fore.WHITE + f"You pucker up and lean in. The horrified {self.royal} staggers back, clasping at the air.")  # noqa
                time.sleep(0.5)
                print_slowly(f"The {self.royal} empties their pockets, pulling out two large bags of gold coins.")  # noqa
                reward_two = ""
                while reward_two != "1" or "2":
                    reward_two = input(Fore.RED + "Will ye accept the MONEY [1] or insist on a KISS [2]?\n").strip()  # noqa
                    if reward_two == "1":
                        print_slowly(Fore.WHITE + f"The {self.royal} gladly shoves the bags into your sweaty hands and runs off before you change your mind.")  # noqa

                        time.sleep(0.5)
                        print_slowly("You're rich beyond double what you could dream. Already you're dreaming of a whole new set of clothes, a larger hovel, and maybe a BMW. Although you regret not having a snog, you're happier than you've ever been.")  # noqa

                        time.sleep(1)
                        print(Fore.GREEN + "THE END")
                        quit()
                    elif reward_two == "2":
                        print_slowly(Fore.WHITE + f"The {self.royal}'s face contorts with disgust, but they dutifully lean in to meet your scabby mouth. You touch lips. Before you've even had a chance to really enjoy the kiss they're reeling back, coughing and wiping their face, before turning tail and running toward the palace.")  # noqa

                        time.sleep(0.5)
                        print_slowly("Even though it was short, you enjoyed what was your first kiss (unless you count that time with the homeless dog) and have never been happier.")  # noqa

                        time.sleep(0.5)
                        print_slowly("You float home on a cloud of joy.")

                        time.sleep(1)
                        print(Fore.GREEN + "THE END")
                        quit()
                    else:
                        print_slowly("Do not let your joy get the better of you, steady yourself and choose one of the two options available.")  # noqa

            else:
                print_slowly("On offer: money or possible love. What will ye decide?")  # noqa

    def game_over(self):
        """
        Function to run when player hits a Game Over screen.
        Restarts game
        """
        time.sleep(0.8)
        print("Run the game again to re-play")
        time.sleep(1)
        quit()


def print_slowly(text):
    """
    Function to print text one character at time to the screen
    as if it's being typed out
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.06)
    print()


def main():
    """
    RUN the GAME
    """
    title1 = pyfiglet.figlet_format("Royal")
    title2 = pyfiglet.figlet_format("Rescue")
    print(Fore.BLUE + title1)
    print(Fore.BLUE + title2)

    print_slowly(Fore.WHITE + "Ah, a new player.")

    time.sleep(1)
    game = AdventureGame()
    game.opening()


main()
