import random

RESET = "\033[0m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
WHITE = "\033[97m"

words = [
    "about", "above", "after", "agree", "alive", "allow", "along", "amount", "apple", "apply",
    "arena", "arise", "audio", "avoid", "baker", "basic", "began", "begin", "below", "bread",
    "break", "bring", "brown", "build", "bunch", "buyer", "cable", "carry", "catch", "cause",
    "chain", "chair", "chart", "chief", "child", "civil", "claim", "class", "clean", "clear",
    "click", "clock", "close", "cloud", "coach", "coast", "color", "comma", "count", "cover",
    "crane", "crazy", "crime", "crowd", "cycle", "dance", "dealt", "death", "debut", "depth",
    "dream", "drink", "drive", "early", "earth", "eight", "enemy", "enjoy", "enter", "equal",
    "error", "event", "every", "exact", "exist", "extra", "faith", "false", "fault", "fiber",
    "field", "final", "first", "fixed", "flame", "floor", "fluid", "focus", "force", "forge",
    "forte", "frame", "front", "fruit", "funny", "genre", "given", "glass", "glory", "goose",
    "grade", "grain", "grand", "grant", "great", "green", "group", "growl", "guest", "guide",
    "happy", "heart", "heavy", "hello", "hence", "house", "human", "ideal", "image", "index",
    "input", "issue", "joint", "judge", "knack", "knife", "known", "large", "later", "laugh",
    "layer", "learn", "legal", "level", "light", "limit", "local", "lucky", "magic", "major",
    "maker", "meter", "might", "minor", "model", "money", "month", "moral", "motor", "mount",
    "mouse", "mouth", "movie", "music", "nasty", "never", "night", "noise", "north", "novel",
    "ocean", "offer", "other", "ought", "owner", "paper", "party", "peace", "phase", "phone",
    "place", "plain", "plane", "plant", "plate", "point", "power", "press", "price", "pride",
    "prime", "print", "prize", "proof", "proud", "queen", "quick", "quiet", "radio", "raise",
    "range", "rapid", "rather", "ready", "refer", "right", "river", "robot", "rough", "round",
    "route", "royal", "rural", "salad", "scale", "scene", "scope", "score", "sense", "serve",
    "setup", "share", "sheep", "sheet", "shift", "shine", "shirt", "shock", "shoot", "short",
    "shown", "sight", "since", "skill", "sleep", "small", "smile", "sound", "south", "space",
    "speak", "speed", "spend", "split", "sport", "staff", "stage", "stand", "start", "state",
    "steam", "steel", "stick", "still", "stock", "stone", "store", "story", "strip", "study",
    "sugar", "super", "sweet", "table", "taste", "teach", "thank", "theme", "there", "thick",
    "thing", "think", "third", "three", "throw", "tight", "title", "today", "total", "touch",
    "towel", "tower", "track", "trade", "train", "trial", "trick", "truth", "twice", "under",
    "union", "unity", "until", "upper", "urban", "usual", "value", "video", "visit", "vital",
    "voice", "waste", "watch", "water", "while", "white", "whole", "woman", "world", "worry",
    "worse", "worth", "would", "write", "wrong", "yacht", "yield", "young", "youth", "zebra"
]


def get_feedback(user_inp, random_word):
    feedback = [''] * 5
    used = [False] * 5
    for i in range(len(user_inp)):
        if user_inp[i] == random_word[i]:
            feedback[i] = 'Y'
            used[i] = True
    for i in range(len(user_inp)):
        if feedback[i] == '':
            for j in range(len(user_inp)):
                if not used[j] and user_inp[i] == random_word[j]:
                    feedback[i] = '?'
                    used[j] = True
                    break
            else:
                feedback[i] = 'X'
    return feedback

def print_colored_feedback(user_inp, feedback):
    colored_letters = []
    for i in range(len(feedback)):
        if feedback[i] == 'Y':
            colored_letters.append(GREEN + user_inp[i].upper() + RESET)
        elif feedback[i] == '?':
            colored_letters.append(YELLOW + user_inp[i].upper() + RESET)
        else:
            colored_letters.append(WHITE + user_inp[i].upper() + RESET)
    print('\t'.join(colored_letters) + '\n')

random_word = random.choice(words)

maxim = 6
attempts = 0
won = False
welcome_string = '''
Hello, Welcome to Wordle on the Terminal. You have 6 tries to guess a 5 letter word.
Once you guess, Green colour indicates the letter is at the right place,
Yellow indicates that the letter is present in the word but not at the right place,
White indicates that the letter is not present in the word. Good luck!
'''
print(welcome_string)

while True:
    user_inp = input(f"Attempt - {attempts + 1}/{maxim} Enter a 5-letter word: ").lower()
    if len(user_inp) != 5 or not user_inp.isalpha():
        print("Please enter a valid 5-letter word.\n")
        continue

    feedback = get_feedback(user_inp, random_word)
    print_colored_feedback(user_inp, feedback)

    if user_inp == random_word:
        print("Congratulations! You've guessed the word correctly!")
        won = True
        break

    attempts += 1
    if attempts > 5:
        break

if not won:
    print(f"Game over! The correct word was '{random_word.upper()}'. Better luck next time!")
