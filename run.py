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
        Gives the user the choice of whether or not to start the game
        """
        start = input(Fore.RED + "Begin game? [Y/N]\n").lower()
        if start.strip() == 'y':
            self.create_player()
            self.name_reverse()
        else:
            s = Fore.WHITE + "It seems you did not type 'Y'... "
            for character in s:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            time.sleep(0.5)
            s = "I'm struggling to understand why you're here if not to play."
            for character in s:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            print()
            print()
            self.opening()

    # https://www.w3schools.com/python/python_howto_reverse_string.asp
    def name_reverse(self):
        """
        Reverses the player name - this reversed name is the name
        the program will use for the player
        """
        initial_name = input("Pray tell, what be thine name? \n")
        reversed_name = initial_name[::-1]
        self.name = reversed_name.capitalize()
        if len(self.name.strip()) == 0:
            s = Fore.WHITE + "A lack of name is not a name"
            for character in s:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            print()
            self.name = "Herbert"
            time.sleep(0.5)
            s1 = "I shall call you Herbert"
            for character in s1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            print()
        else:
            s2 = Fore.WHITE + f"Hmm, {initial_name}... a weak and poor name, make no mistake." # noqa
            for character in s2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            print()
            time.sleep(0.5)
            s = f"I shall call you {self.name}, 'tis far better!"
            for character in s:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            print()
        self.hometown()
        return

    def hometown(self):
        """
        Asks for the name of the player's hometown
        and returns it as the story setting
        """
        s1 = Fore.RED + f"And, {self.name}, from where do you spring from? "
        for character in s1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        self.town = input("Which place do ye call home? \n")
        if len(self.town.strip()) == 0:
            s2 = Fore.WHITE + "If you be too ashamed to tell me, I shall assume it is a terrible place, perhaps Swindon." # noqa
            for character in s2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            print()
            self.town = "Swindon"
            time.sleep(0.5)
            s3 = "And that den of poverty and sin is the setting for our tale today..."  # noqa
            for character in s3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            print()
            time.sleep(1)
            print()
        else:
            s4 = Fore.WHITE + f"{self.town}! A vile place full of inbred and ugly folk!"  # noqa
            for character in s4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            print()
            time.sleep(0.5)
            s5 = "And by coincidence the setting for our tale today..."
            for character in s5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(0.06)
            print()
            print()
        self.prince_princess()
        return

    def prince_princess(self):
        """
        Player chooses whether to rescue a prince or a princess
        """
        s1 = f"The rooster crows in the grotty hamlet of {self.town}."
        for character in s1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.5)
        s2 = f"You, {self.name}, roll from your filthy woven mattress and pull your unwashed rags over your unwashed head. Lice scatter." # noqa
        for character in s2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.5)
        s3 = "A newspaper falls through your letterbox,"
        for character in s3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s4 = "you look at the front page,"
        for character in s4:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s5 = "A member of the royal household has been kidnapped!"
        for character in s5:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.5)
        s6 = "Someone is going to have to rescue him, or her. "
        for character in s6:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s7 = "Your filthy thumbprint has smeared the details..."
        for character in s7:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        royal_choice = ""
        while royal_choice.strip() != "1" or "2":
            royal_choice = input(Fore.RED + "Is the kidnapped royal a PRINCE(1) or a PRINCESS(2)? \n") # noqa
            if royal_choice.strip() == "1":
                self.royal = "prince"
                s = Fore.WHITE + 'The newspaper reads: '
                for character in s:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                s10 = '"The handsome prince, covered in six-packs & pectorals,'
                for character in s10:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                s11 = "intelligent and witty and nary a pimple on his skin, "
                for character in s11:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                s2 = "was just this morning kidnapped from the palace. "
                for character in s2:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                time.sleep(0.5)
                s3 = "Whomsoever dost rescue him surely shall be handsomely rewarded" # noqa
                for character in s3:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                s4 = "with a kiss on their haggard face, a bag of coin, "
                for character in s4:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                s5 = 'or whatever reward the rescuer dost desire."'
                for character in s5:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                print()
                time.sleep(0.8)
                self.first()
                return
            elif royal_choice.strip() == "2":
                self.royal = "princess"
                s = Fore.WHITE + 'The newspaper reads:'
                for character in s:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                s1 = '"The smouldering princess, veritably covered in shapely curves'  # noqa
                for character in s1:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                s2 = "with a sharp and clever wit"
                for character in s2:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                s3 = "smooth of skin and the most lovely in the land,"
                for character in s3:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                s4 = "was this morning kidnapped from the castle."
                for character in s4:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                time.sleep(0.5)
                s5 = "Whomsoever dost rescue her surely shall be handsomely rewarded"  # noqa
                for character in s5:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                s6 = "with a kiss on their spotty cheek, a bag of coin, "
                for character in s6:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                s7 = 'or whatever reward the rescuer dost desire."'
                for character in s7:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                print()
                time.sleep(0.8)
                self.first()
                return
            else:
                s8 = "Your chubby peasantly fingers have missed the relevant keys. "  # noqa
                for character in s8:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                time.sleep(0.5)
                s9 = "Attempt to uncross thine eyes and try again."
                for character in s9:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()

    def create_player(self):
        """
        Creates an instance of the Player class
        to store and return the needed variables
        """
        self.name = self.name_reverse()
        self.town = self.hometown()
        self.royal = self.prince_princess()

    def first(self):
        """
        First choice - palace or pub
        """
        s = f"So it is decided that YOU, {self.name}, will rescue the {self.royal}." # noqa
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s1 = "You waddle down the stairs and flop onto the street."
        for character in s1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        print(Fore.RED + "In which direction will you turn?")
        first_choice = ""
        while first_choice.strip() != "1" or "2":
            first_choice = input(Fore.RED + "Toward the PALACE(1) or the PUB(2)? \n")  # noqa
            if first_choice == "1":
                self.palace()
            elif first_choice == "2":
                self.pub()
            else:
                s3 = Fore.WHITE + "Again your foolishness confounds me!"
                for character in s3:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()

    def palace(self):
        """
        The initial palace path
        """
        s = Fore.WHITE + f"Let's face it, if the {self.royal} was at the palace they wouldn't be missing, would they? Cursing your lack of intelligence, you sit down for a while to think. There's a chance the kidnappers might have taken the {self.royal} away in a stagecoach, so the logical thing would be to go to the CROSSROADS and search. But on the other hand you haven't had any ale or mead for what feels like hours, and there's a very slim chance the {self.royal} might have just slipped out for a cheeky gin and soda." # noqa
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        print(Fore.RED + "Where dost thou wish to turn?")
        palace_choice = ""
        while palace_choice.strip() != "1" or "2":
            palace_choice = input(Fore.RED + "Toward the CROSSROADS(1) or the PUB(2)\n")  # noqa
            if palace_choice.strip() == "1":
                self.crossroads()
            elif palace_choice.strip() == "2":
                self.pub()
            else:
                s1 = Fore.WHITE + "The decision is not difficult for folk of sound mind."  # noqa
                for character in s1:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()

    def pub(self):
        """
        The initial pub path
        """
        s = Fore.WHITE + f"You barrel into the pub and order a flagoon of wine. Followed by another flagoon of wine. The {self.royal} does not seem to be in the pub, so you have another drink. You fall asleep. You awake mid-afternoon feeling sure that you had some kind of mission to fulfil." # noqa
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.5)
        print(Fore.RED + "Where next, friend?")
        pub_choice = ""
        while pub_choice != "1" or "2":
            pub_choice = input(Fore.RED + "Will ye go to the PALACE(1), the CROSSROADS(2), or stay here(3)?\n") # noqa
            if pub_choice.strip() == "1":
                self.palace()
            elif pub_choice.strip() == "2":
                self.crossroads()
            elif pub_choice.strip() == "3":
                self.pub_two()
            else:
                s = Fore.WHITE + "Try again..."
                for character in s:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()

    def pub_two(self):
        """
        The second Pub choice, leading to Game Over
        """
        s = Fore.WHITE + "You order a bottle of mead, and then another."
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s1 = "You play pool. You fall over."
        for character in s1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.4)
        s2 = "You play darts and hit the barmaid with a dart."
        for character in s2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s3 = "Eventually everything goes cloudy."
        for character in s3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.4)
        s4 = "You awaken 2 days hence in your own bed, "
        for character in s4:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s5 = "with your trousers on backwards and socks on your hands."
        for character in s5:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s6 = "Your head throbs. You pick up the newspaper, then drop it"
        for character in s6:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s7 = "because you still have socks on your hands."
        for character in s7:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.4)
        s8 = "Regardless, you persevere, flopping the page over with your"
        for character in s8:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s9 = f"be-socked hands. The headline says the {self.royal} has been"
        for character in s9:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s10 = "rescued by another grimy pauper, who is now being"
        for character in s10:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s11 = "showered with romantic favours and gifts of silver and gold."
        for character in s11:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.5)
        s12 = f"You missed your chance {self.name}."
        for character in s12:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.5)
        s13 = "You peel back your vomit-stained sheets and go back to bed."
        for character in s13:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        print(Fore.YELLOW + "GAME OVER.")
        self.game_over()

    def crossroads(self):
        """
        The Crossroads choice, on the correct path to victory
        """
        s = Fore.WHITE + "Lumbering down the lane, nature calls and you feel the need to relieve yourself. Will you do it in the bushes, or urinate into your own (already filthy) trousers?" # noqa
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        wee_choice = ""
        while wee_choice.strip() != "1" or "2":
            wee_choice = input(Fore.RED + "Type [1] for in the BUSHES or [2] for WETTING YOURSELF: \n") # noqa
            if wee_choice.strip() == "1":
                self.bushes()
            elif wee_choice.strip() == "2":
                self.carriage()
            else:
                s1 = Fore.WHITE + "Thou do not hast time to fool around with a bladder this full" # noqa
                for character in s1:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()

    def bushes(self):
        """
        The wrong choice, leading to a GAME OVER
        """
        s = Fore.WHITE + f"After doing what you have to do, you run out again toward the crossroads. In the distance the carriage rounds a bend - you're too late! Your rare thought of personal hygiene has allowed the kidnappers of the {self.royal} to escape." # noqa
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.5)
        s1 = Fore.WHITE + "You trudge home, vowing never again to pee outside of your own clothing." # noqa
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(1)
        print(Fore.YELLOW + "GAME OVER.")
        self.game_over()

    def carriage(self):
        """
        Player has a chance to intercept the fleeing carriage
        """
        s = Fore.WHITE + f"Trousers full of wee, you, {self.name}, round the bend as the stagecoach approaches, the {self.royal} tied up in the back seat. You'll only have one chance to stop the carriage!" # noqa
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.5)
        s1 = "In front of you, you see a rock, a stick and a knife."
        for character in s1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s2 = "You have time to throw but one implement at the kidnappers to stop them, but which will you choose...?" # noqa
        for character in s2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        weapon = ""
        while weapon != "1" or "2" or "3":
            weapon = input(Fore.RED + "Will thee toss the ROCK [1], the STICK [2] or the KNIFE [3]? \n") # noqa
            if weapon.strip() == "1":
                self.rock()
            elif weapon.strip() == "2":
                self.stick()
            elif weapon.strip() == "3":
                self.knife()
            else:
                s5 = Fore.WHITE + "The carriage is moving fast, make your choice" # noqa
                for character in s5:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()

    def rock(self):
        """
        The wrong weapon, leading to a Game Over
        """
        s = Fore.WHITE + f"You clumsily hurl the rock carriageward. It passes between the heads of the kidnappers and strikes the {self.royal} clean between the eyes!" # noqa
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.5)
        s1 = "The carriage barrels into the distance, the comatose royal lolling side to side in the rear." # noqa
        for character in s1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s2 = "A cloud of dust envelopes you as it passes, making you cough and vomit."  # noqa
        for character in s2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s3 = f"{self.name}, with your boss-eyed throwing style, {self.name} you've blown it." # noqa
        for character in s3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(1)
        print(Fore.YELLOW + "GAME OVER.")
        self.game_over()

    def knife(self):
        """
        The wrong weapon, leading to a Game Over
        """
        s = Fore.WHITE + "You leap, shrieking and brandishing the knife! But as you pull back the blade to hurl carriageward you embed it in your own bulbous forehead." # noqa
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.5)
        s1 = f"You slump to the ground as the kidnappers' carriage bearing the {self.royal} steams past." # noqa
        for character in s1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s2 = "Home you stagger, dagger still stuck in your spotty mush."
        for character in s2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(0.5)
        s3 = "There'll be no rescue today."
        for character in s3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        time.sleep(1)
        print(Fore.YELLOW + "GAME OVER.")
        self.game_over()

    def stick(self):
        """
        The correct weapon, leading to a victory of some sort
        """
        s = Fore.WHITE + f"The stick spins through the air, bounces and flies between the spokes of the stagecoach's front wheel. The stagecoach swerves violently, throwing the kidnappers into the bushes. As it wobbles to a halt, the {self.royal} steps gingerly from the carriage and sizes you up." # noqa
        for character in s:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        s1 = f"You annouce yourself, 'I am {self.name} from the parish of {self.town}, pleased to rescue you.' The {self.royal} knows that they're going to have to dish out a reward." # noqa
        for character in s1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.06)
        print()
        reward = ""
        while reward != "1" or "2":
            reward = input(Fore.RED + "Will you ask for a BAG OF GOLDEN COINS [1], or a KISS [2] on the face? \n") # noqa
            if reward.strip() == "1":
                s3 = f"The {self.royal} digs around in their pocket and pulls out a bag of coins. They hand it to you without a word, dust themselves down and start the long walk back toward the palace." # noqa
                for character in s3:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                time.sleep(0.5)
                s4 = "You're rich beyond your wildest dreams. Already your head is swimming with ideas on upgrading your hovel and buying a second set of trousers." # noqa
                for character in s4:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                time.sleep(0.5)
                s5 = "You wander home, smiling happily"
                for character in s5:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                time.sleep(1)
                print(Fore.GREEN + "THE END")
            elif reward.strip() == "2":
                s6 = f"You pucker up and lean in. The horrified {self.royal} staggers back, clasping at the air." # noqa
                for character in s6:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                time.sleep(0.5)
                s7 = f"The {self.royal} empties their pockets, pulling out two large bags of gold coins." # noqa
                for character in s7:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()
                reward_two = ""
                while reward_two != "1" or "2":
                    reward_two = input(Fore.RED + "Will ye accept the MONEY [1] or insist on a KISS [2]?\n") # noqa
                    if reward_two.strip() == "1":
                        s8 = f"The {self.royal} gladly shoves the bags into your sweaty hands and runs off before you change your mind." # noqa
                        for character in s8:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.06)
                        print()
                        time.sleep(0.5)
                        s9 = "You're rich beyond double what you could dream. Already you're dreaming of a whole new set of clothes, a larger hovel, and maybe a BMW. Although you regret not having a snog, you're happier than you've ever been." # noqa
                        for character in s9:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.06)
                        print()
                        time.sleep(1)
                        print(Fore.GREEN + "THE END")
                        quit()
                    elif reward_two.strip() == "2":
                        s10 = f"The {self.royal}'s face contorts with disgust, but they dutifully lean in to meet your scabby mouth. You touch lips. Before you've even had a chance to really enjoy the kiss they're reeling back, coughing and wiping their face, before turning tail and running toward the palace." # noqa
                        for character in s10:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.06)
                        print()
                        time.sleep(0.5)
                        s11 = "Even though it was short, you enjoyed what was your first kiss (unless you count that time with the homeless dog) and have never been happier." # noqa
                        for character in s11:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.06)
                        print()
                        time.sleep(0.5)
                        s12 = "You float home on a cloud of joy."
                        for character in s12:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.06)
                        print()
                        time.sleep(1)
                        print(Fore.GREEN + "THE END")
                        quit()
                    else:
                        s13 = "Do not let your joy get the better of you, steady yourself and choose one of the two options available." # noqa
                        for character in s13:
                            sys.stdout.write(character)
                            sys.stdout.flush()
                            time.sleep(0.06)
                        print()
            else:
                s14 = "On offer: money or possible love. What will ye decide?"
                for character in s14:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(0.06)
                print()

    def game_over(self):
        """
        Function to run when player hits a Game Over screen.
        Restarts game
        """
        time.sleep(0.8)
        print("Run the game again to re-play")
        time.sleep(1)
        quit()


def main():
    """
    RUN the GAME
    """
    game = AdventureGame()
    game.opening()


title1 = pyfiglet.figlet_format("Royal")
title2 = pyfiglet.figlet_format("Rescue")
print(Fore.BLUE + title1)
print(Fore.BLUE + title2)

s = Fore.WHITE + "Ah, a new player."
for character in s:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.07)
print()
time.sleep(1)
main()
