from random import *
from replit import clear

logo = '''
 _
| |
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \\
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/    '''


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["shinchan", "tom", "jerry", "phineas", "ferb"]

# word_list = [
#     'abruptly',
#     'absurd',
#     'abyss',
#     'affix',
#     'askew',
#     'avenue',
#     'awkward',
#     'axiom',
#     'azure',
#     'bagpipes',
#     'bandwagon',
#     'banjo',
#     'bayou',
#     'beekeeper',
#     'bikini',
#     'blitz',
#     'blizzard',
#     'boggle',
#     'bookworm',
#     'boxcar',
#     'boxful',
#     'buckaroo',
#     'buffalo',
#     'buffoon',
#     'buxom',
#     'buzzard',
#     'buzzing',
#     'buzzwords',
#     'caliph',
#     'cobweb',
#     'cockiness',
#     'croquet',
#     'crypt',
#     'curacao',
#     'cycle',
#     'daiquiri',
#     'dirndl',
#     'disavow',
#     'dizzying',
#     'duplex',
#     'dwarves',
#     'embezzle',
#     'equip',
#     'espionage',
#     'euouae',
#     'exodus',
#     'faking',
#     'fishhook',
#     'fixable',
#     'fjord',
#     'flapjack',
#     'flopping',
#     'fluffiness',
#     'flyby',
#     'foxglove',
#     'frazzled',
#     'frizzled',
#     'fuchsia',
#     'funny',
#     'gabby',
#     'galaxy',
#     'galvanize',
#     'gazebo',
#     'giaour',
#     'gizmo',
#     'glowworm',
#     'glyph',
#     'gnarly',
#     'gnostic',
#     'gossip',
#     'grogginess',
#     'haiku',
#     'haphazard',
#     'hyphen',
#     'iatrogenic',
#     'icebox',
#     'injury',
#     'ivory',
#     'ivy',
#     'jackpot',
#     'jaundice',
#     'jawbreaker',
#     'jaywalk',
#     'jazziest',
#     'jazzy',
#     'jelly',
#     'jigsaw',
#     'jinx',
#     'jiujitsu',
#     'jockey',
#     'jogging',
#     'joking',
#     'jovial',
#     'joyful',
#     'juicy',
#     'jukebox',
#     'jumbo',
#     'kayak',
#     'kazoo',
#     'keyhole',
#     'khaki',
#     'kilobyte',
#     'kiosk',
#     'kitsch',
#     'kiwifruit',
#     'klutz',
#     'knapsack',
#     'larynx',
#     'lengths',
#     'lucky',
#     'luxury',
#     'lymph',
#     'marquis',
#     'matrix',
#     'megahertz',
#     'microwave',
#     'mnemonic',
#     'mystify',
#     'naphtha',
#     'nightclub',
#     'nowadays',
#     'numbskull',
#     'nymph',
#     'onyx',
#     'ovary',
#     'oxidize',
#     'oxygen',
#     'pajama',
#     'peekaboo',
#     'phlegm',
#     'pixel',
#     'pizazz',
#     'pneumonia',
#     'polka',
#     'pshaw',
#     'psyche',
#     'puppy',
#     'puzzling',
#     'quartz',
#     'queue',
#     'quips',
#     'quixotic',
#     'quiz',
#     'quizzes',
#     'quorum',
#     'razzmatazz',
#     'rhubarb',
#     'rhythm',
#     'rickshaw',
#     'schnapps',
#     'scratch',
#     'shiv',
#     'snazzy',
#     'sphinx',
#     'spritz',
#     'squawk',
#     'staff',
#     'strength',
#     'strengths',
#     'stretch',
#     'stronghold',
#     'stymied',
#     'subway',
#     'swivel',
#     'syndrome',
#     'thriftless',
#     'thumbscrew',
#     'topaz',
#     'transcript',
#     'transgress',
#     'transplant',
#     'triphthong',
#     'twelfth',
#     'twelfths',
#     'unknown',
#     'unworthy',
#     'unzip',
#     'uptown',
#     'vaporize',
#     'vixen',
#     'vodka',
#     'voodoo',
#     'vortex',
#     'voyeurism',
#     'walkway',
#     'waltz',
#     'wave',
#     'wavy',
#     'waxy',
#     'wellspring',
#     'wheezy',
#     'whiskey',
#     'whizzing',
#     'whomever',
#     'wimpy',
#     'witchcraft',
#     'wizard',
#     'woozy',
#     'wristwatch',
#     'wyvern',
#     'xylophone',
#     'yachtsman',
#     'yippee',
#     'yoked',
#     'youthful',
#     'yummy',
#     'zephyr',
#     'zigzag',
#     'zigzagging',
#     'zilch',
#     'zipper',
#     'zodiac',
#     'zombie',
# ]


print(logo)
chosen_word = choice(word_list)
blank_list = ["_"]*len(chosen_word)
print(f"The solution is {chosen_word}")
game_continues = True
lives = 6
while game_continues:
    guess = input("Guess a letter: ").lower()
    clear()
    print(logo)
    if guess in blank_list:
        print(f"You've already guessed {guess}")
    else:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                blank_list[position] = guess
    print(" ".join(blank_list))
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_continues = False
            print("You lose :(")
    if "_" not in blank_list:
        print("You won ;)")
        game_continues = False
    print(stages[lives])
