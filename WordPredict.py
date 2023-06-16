"""
1.0
First release
1.1
removed qt library
1.2
Guessing the same letter wont remove points
themes setting
minor code improvments
losing penalty
"""


from random import choice as choose
from os.path import exists
from random import randint
import PySimpleGUI as sg
from os import remove
from json import  dump, load
from sys import exit as close_program

WORDS = ['history', 'station', 'selection', 'stretch', 'kittens', 'birthday', 'territory', 'spring', 'afternoon', 'creator', 'bottle', 'purpose', 'pancake', 'friction', 
'country', 'society', 'observation', 'trains', 'suggestion', 'pencil', 'texture', 'receipt', 'liquid', 'porter', 'statement', 'impulse', 'person', 'business',
'cabbage', 'wilderness', 'partner', 'competition', 'instrument', 'minute', 'holiday', 'mitten', 'morning', 'poison', 'hammer', 'knowledge', 'morning', 'winter',
'fireman', 'sticks', 'treatment', 'weather', 'porter', 'amount', 'chickens', 'toothpaste', 'flavor', 'memory', 'bucket', 'bridge', 'basketball', 'toothbrush', 
'reaction', 'library', 'chance', 'committee', 'degree', 'creature', 'advice', 'country', 'health', 'sneeze', 'wealth', 'stocking', 'person', 'notebook', 'animal', 
'throne', 'appliance', 'cushion', 'arrive', 'attempt', 'employ', 'realize', 'untidy', 'arrange', 'complain', 'multiply', 'rescue', 'compete', 'escape', 'shiver', 
'remind', 'imagine', 'interest', 'develop', 'command', 'applaud', 'divide', 'invent', 'attack', 'compare', 'wander', 'unlock', 'reject', 'charge', 'supply', 'concern', 
'undress', 'inform', 'wonder', 'provide', 'flower', 'suggest', 'wobble', 'influence', 'radiate', 'support', 'reduce', 'increase', 'memorize', 'encourage', 'education',
'person', 'apparatus', 'impulse', 'trouble', 'expert', 'profit', 'opinion', 'canvas', 'destruction', 'stretch', 'existence', 'discussion', 'quality', 'polish', 'manager',
'change', 'punishment', 'expansion', 'belief', 'support', 'fiction', 'reason', 'disgust', 'building', 'cigarette', 'cancer', 'courage', 'sample', 'application', 'writing',
'aspect', 'accident', 'election', 'client', 'science', 'reflection', 'passenger', 'inspector', 'newspaper', 'instance', 'complaint', 'response', 'version', 'teaching', 
'resolution', 'people', 'guitar', 'fortune', 'cousin', 'stranger', 'negotiation', 'celebration', 'funeral', 'control', 'possibility', 'climate', 'president', 'trainer', 
'investment', 'selection', 'abstract', 'accept', 'accelerate', 'access', 'accompany', 'accord', 'account', 'accrue', 'achieve', 'acknowledge', 'acquire', 'address', 
'adhere', 'adjust', 'administer', 'admire', 'advance', 'adventurous', 'advertise', 'advise', 'advocate', 'affair', 'affect', 'afford', 'affiliate', 'affinity', 'affirm',
'afford', 'afloat', 'affront', 'afternoon', 'against', 'agenda', 'airplane', 'alcohol', 'allergic', 'almost', 'alphabet', 'already', 'although', 'always', 'amazing', 
'ambitious', 'amount', 'analyze', 'ancient', 'animal', 'announce', 'annual', 'anonymous', 'answer', 'anxious', 'anybody', 'anyone', 'anything', 'anywhere', 'apartment', 
'apparent', 'appeal', 'appear', 'appetite', 'appoint', 'applause', 'appreciate', 'approach', 'appropriate', 'approve', 'apricot', 'aquatic', 'around', 'arrange', 
'arrest', 'arrive', 'article', 'artificial', 'artist', 'artistic', 'arrogant', 'ashamed', 'ashamed', 'asleep', 'aspect', 'assemble', 'assembly', 'assist', 
'assistant', 'associate', 'assume', 'assure', 'athlete', 'attach', 'attack', 'attempt', 'attend', 'attention', 'attentive', 'attitude', 'attract', 'attractive', 
'attribute', 'author', 'authority', 'automatic', 'automobile', 'autumn', 'available', 'average', 'awkward', 'advertisement', 'understanding', 'communication',
'recommendation', 'administration', 'entertainment', 'responsibility', 'transportation', 'establishment', 'differentiate', 'unaccountable', 'knowledgeable', 
'disillusioned', 'environmental', 'heartbreaking', 'dysfunctional', 'psychological', 'sophisticated', 'lackadaisical', 'materialistic', 'administrative', 
'overconfident', 'comprehensive', 'scintillating', 'competitionsister', 'entertainment', 'conversation', 'distribution', 'significance', 'agricultural', 
'apprehensive', 'approximately', 'gate', 'stove', 'verse', 'cow', 'rule', 'metal', 'heat', 'blade', 'hand', 'walk', 'frog', 'noise', 'toy', 'worm', 'self', 
'oven', 'rest', 'limit', 'dirt', 'smoke', 'seed', 'army', 'boy', 'yard', 'pull', 'meal', 'aunt', 'girls', 'car', 'pail', 'ring', 'scarf', 'form', 'coal', 
'drain', 'deer', 'chalk', 'loss', 'trick', 'touch', 'sack', 'stone', 'end', 'pie', 'mind', 'dad', 'fire', 'step', 'chin', 'grape', 'can', 'rake', 'spoon',
'death', 'queen', 'tent', 'look', 'bone', 'shelf', 'bat', 'beds', 'sock', 'blow', 'wall', 'noise', 'lake', 'ray', 'fear', 'skirt', 'bear', 'crook', 
'cause', 'cover', 'train', 'fuel', 'quill', 'dogs', 'unit', 'scent', 'guide', 'sign', 'slave', 'iron', 'week', 'sofa', 'trade', 'shape', 'land', 
'tray', 'smoke', 'cave', 'boat', 'bell', 'rain', 'bit', 'actor', 'drop', 'smash', 'songs', 'sound', 'coach', 'day', 'juice', 'month', 'verse', 
'thaw', 'glow', 'order', 'mate', 'face', 'last', 'milk', 'live', 'bat', 'found', 'brake', 'film', 'name', 'sip', 'mix', 'count', 'bump', 'kneel', 
'mourn', 'plant', 'join', 'grab', 'rot', 'comb', 'stain', 'store', 'bolt', 'beg', 'glue', 'miss', 'chase', 'list', 'nail', 'stir', 'offer', 'jail',
'long', 'reply', 'head', 'wipe', 'place', 'carve', 'tug', 'allow', 'shrug', 'melt', 'gaze', 'lick', 'fit', 'flow', 'camp', 'smell', 'wail', 'kick',
'hunt', 'trip', 'moan', 'point', 'sense', 'level', 'mind', 'cook', 'twist', 'night', 'doubt', 'hour', 'smoke', 'soup', 'guide', 'limit', 'trick', 
'wine', 'jelly', 'stop', 'drink', 'cloth', 'sky', 'tax', 'food', 'laugh', 'fall', 'slip', 'cork', 'view', 'force', 'form', 'bread', 'order', 'page',
'smile', 'part', 'pain', 'mom', 'oven', 'beer', 'two', 'tale', 'actor', 'paper', 'buyer', 'week', 'tag', 'shy', 'dive', 'act', 'add', 'admit', 
'adopt', 'adopt', 'affix', 'after', 'again', 'age', 'agent', 'agree', 'ahead', 'aim', 'air', 'alarm', 'album', 'alert', 'alien', 'align', 'alive', 
'all', 'allow', 'alone', 'along', 'aloud', 'also', 'alter', 'among', 'amuse', 'and', 'angel', 'anger', 'angle', 'angry', 'ant', 'any', 'apart',
    'apple', 'apply', 'argue', 'arm', 'armed', 'army', 'arrow', 'art', 'atom', 'audio', 'audit', 'avoid', 'awake', 'award', 'aware', 'away', 'awful', 'axe']

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

VERSION = 1.2
NAME = "WordPredict"
SAVE_FILE = f"{NAME} Save.json"
CREDITS = """Developer - blabla_lab
GUI Library - PySimpleGUI"""


# settings
global gradual_difficulty,gradual_difficulty_word_length,show_first_letter,show_last_letter,level,points,points_required_for_level
gradual_difficulty = True
gradual_difficulty_word_length = 3
show_first_letter = True 
show_last_letter = True
level = 1
points = 0
user_tries = 6
tries=user_tries
points_required_for_level = 3
custom_words = []



def auto_font_size():
    window.find_element("WORD").update(font=("LCD Solid", window.size[1] // 20 ))
    window.find_element("Title").update(font=(FONT[0], window.size[1] // 20 ))


def save():
    with open(SAVE_FILE, "w") as f:
        save_dictionary = {
            "gradual_difficulty": gradual_difficulty,
            "gradual_difficulty_word_length": gradual_difficulty_word_length,
            "show_first_letter": show_first_letter,
            "show_last_letter": show_last_letter,
            "level": level,
            "points": points,
            "tries": user_tries,
            "custom_words": custom_words,
            "points_required_for_level": points_required_for_level,
        }
        dump(save_dictionary, f, indent=1)



def load_save():
    with open(SAVE_FILE, "r") as f:
        return load(f)
    


if not exists(SAVE_FILE):
    with open(SAVE_FILE, "w"):
        pass
    save()

sg.theme_border_width(3)
sg.theme("dark2")

FONT = (None, 18)  
sg.set_options(font=FONT, element_padding=(10,10), auto_size_text=True, auto_size_buttons=True)
sg.set_options(font=FONT, element_padding=(5,5), auto_size_text=True, auto_size_buttons=True)

# sg.theme('SystemDefault')

#load save
try:
    save_dictionary = load_save()
    user_tries=save_dictionary["tries"]
    gradual_difficulty = save_dictionary["gradual_difficulty"]
    gradual_difficulty_word_length = save_dictionary["gradual_difficulty_word_length"]
    show_first_letter = save_dictionary["show_first_letter"]
    show_last_letter = save_dictionary["show_last_letter"]
    level = save_dictionary["level"]
    points = save_dictionary["points"]
    for i in save_dictionary["custom_words"]:
        WORDS.append(i)
    points_required_for_level = save_dictionary["points_required_for_level"]
except (KeyError, FileNotFoundError) as e:
    sg.popup_error(f"deleting save file...\n\nmore info:\n{e}")
    remove(SAVE_FILE)
    close_program("bad save file")
print("Loaded save file")


# sg.theme("LightGrey3")
# Custom flat PySimpleGUI Theme.
# Generated using Themera v1.0.0.
import PySimpleGUI as sg  # Please change 'sg' to your liking.
flat_themedict = {'BACKGROUND': '#f1f1f1',
    'TEXT': 'black',
    'INPUT': '#c8c8c8',
    'TEXT_INPUT': '#171413',
    'SCROLL': '#a0a0a0',
    'BUTTON': ('black', '#a4daff'),
    'PROGRESS': ('black', '#a0a0a0'),
    'BORDER': 0,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0}

sg.theme_add_new('default', flat_themedict)
sg.theme('default')
print("Applied theme")


while True:
    print("On while loop")
    tries=user_tries
    bad_letters = []
    word = choose(WORDS)

    if gradual_difficulty:
        while True:
            print(f"Making up a word...\n\nword:{word}, {type(word)}\ngdwl:{gradual_difficulty_word_length}")
            word = choose(WORDS)
            if not len(word) > gradual_difficulty_word_length:
                break

    word_in_a_list_form = list(word)
    guess_word = []
    for i in word_in_a_list_form:
        guess_word.append("_")
    
    if show_first_letter is True: 
        guess_word[0] = word_in_a_list_form[0]
    if show_last_letter is True:
        guess_word[-1] = word_in_a_list_form[-1]

    layout = [  [sg.T(f"{NAME}!", justification="c", expand_x=True, key="Title")],
                [sg.T(f"Level:{level}", font=(FONT[0], FONT[1], "bold"), expand_x=True, expand_y=True),sg.T(f"Tries:{tries}", font=(FONT[0], FONT[1], "bold"), expand_x=True, expand_y=True, k="t")],
                [sg.ProgressBar(points_required_for_level, orientation="h", k="-PR-", expand_x=True, expand_y=True), sg.T(f"Points:{points}", font=(FONT[0], FONT[1], "bold"), expand_x=True, expand_y=True)],
                [sg.T(" ".join(guess_word), key="WORD", relief=sg.RELIEF_SUNKEN, justification="c", expand_x=True, font=("LCD Solid", 18, "bold"), tooltip="the word you need to guess its missing letters")],
                [sg.T("Guess a letter:", expand_x=True)],
                [sg.B(i, expand_x=True, pad=(1,1), expand_y = True) for i in LETTERS[0:14]],
                [sg.B(i, expand_x=True, pad=(1,1), expand_y = True) for i in LETTERS[14:]],
                [sg.B("Settings", expand_x=True)]]

    window = sg.Window(NAME, layout, resizable=True).finalize()

    window.set_min_size((534, 346))

    window.find_element("-PR-").update(points, points_required_for_level)

    auto_font_size()

    exit_loop = False

    while not exit_loop:
        print("On nested loop")
        event, values = window.read(1500, timeout_key="-TIMEOUT-")
        
        if event == sg.WIN_CLOSED:
            window.close()
            close_program()
        elif event == "Settings":
            settings_layout = [
                [sg.T("Settings")],
                [sg.Checkbox("gradual difficulty", key="gd", default=gradual_difficulty, 
                              tooltip="this mode will give you words\nbased on your level, for example\nlevel 1 will give you words ranging\nfrom 3-4 letters of length"), 
                              sg.T(f"Gradual diffculty max word length:{gradual_difficulty_word_length}",
                                    tooltip="this tells you the number of letters long words can come, based on level")],
                
                [sg.Checkbox("show first letter", key="sf", default=show_first_letter)],
                [sg.Checkbox("show last letter", key="sl", default=show_last_letter)],
                [sg.T("Tries:"), sg.In(user_tries, key="tries")],
                [sg.T("Themes"), sg.Listbox(["default", "Dark2", "Black", "SystemDefault", "RAnDOm"], default_values=sg.theme(), select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, key="-THEME-")],
                [sg.B("Add new word"), sg.B("Credits"), sg.B("view words"), sg.B("Delete save")], 
                [sg.OK(), sg.T("the game will restart to apply changes!")]
            ]
            settings_window = sg.Window("Settings", settings_layout)
            while True:
                se, sv = settings_window.read()
                invalid = False
                if se == sg.WIN_CLOSED: 
                    sg.popup_quick_message("Didnt save settings")
                    break
                elif se == "Add new word":
                    user_custom_word = sg.popup_get_text("Type a word you want to\nadd to the word base:", title="add", background_color="Dark Gray")
                    if user_custom_word is None or user_custom_word.strip() == "":
                        continue
                    for i in list(user_custom_word):
                        print(i)
                        if not i in LETTERS or user_custom_word in WORDS:
                            invalid = True
                            sg.popup_ok("your word contained something thats not a letter.\nor your word already exists in the words base.", title="error")
                            break
                    if invalid:
                        continue

                    WORDS.append(user_custom_word)


                elif se == "OK":
                    gradual_difficulty = sv["gd"]
                    show_first_letter = sv["sf"]
                    show_last_letter = sv["sl"]
                    user_tries = int(sv["tries"])
                    sg.theme("".join(sv["-THEME-"]))
                    sg.theme_border_width(0)
                    save()
                    window.close()

                    exit_loop=True
                    break
                
                elif se == "Credits":
                    sg.popup_no_buttons(f"{NAME} {VERSION}\n\nCredits:\n{CREDITS}\n\nOther:\nWords in the game:{len(WORDS)}", title="Credits")
                elif se == "view words":
                    sg.popup_scrolled(",".join(WORDS), title="words base")
                elif se == "Delete save":
                    confirm = sg.popup_get_text("ARE YOU SURE YOU WANT TO DELETE YOUR SAVE FILE\nALL OF YOUR PROGRESS WILL BE LOST!\nTO CONFIRM TYPE THIS SENTENCE:\nI AM SURE THAT I WANT TO DELETE MY SAVE FILE\n", title="Confirm")
                    if confirm == "I AM SURE THAT I WANT TO DELETE MY SAVE FILE":
                        remove(SAVE_FILE)
                        sg.popup_ok("DELETED SAVE FILE\n\nrestart game to apply changes")
            settings_window.close()
            continue
               
        elif event == "-TIMEOUT-":
            save()
            auto_font_size()
            continue


        #* the checking section *#


        guess = event
      
        
        
        #* this checks if the user guessed correctly

        # check if guess is wrong
        if not guess in word_in_a_list_form:
            if guess not in bad_letters:
                # sg.popup_quick_message("Wrong.", auto_close_duration=0.5, non_blocking=False)
                tries -= 1
                points -= 1
                bad_letters.append(guess)
                window.find_element("t").update(f"Tries:{tries}")
                if tries == 0:
                    sg.popup_ok(f"You lose\nthe word was:{word}")
                    tries = user_tries
                    window.close()
                    break
            

            continue

        for i in range(0, len(word_in_a_list_form)): # it just loops for every letter in the word and check if the guess = the index it reached
            if str(word_in_a_list_form[i]) == str(guess):
                guess_word[i] = guess
                if i >= len(word_in_a_list_form):  #if it finished scanning the whole thing
                    break

                


        if guess_word == word_in_a_list_form:
            window.close()

            points += 1
            if points >= points_required_for_level:
                level += 1
                points_required_for_level += randint(3,8) + level
                gradual_difficulty_word_length += 1
            
            save()
            
            u = sg.popup_yes_no(f"You won!\nThe word was {word}.\nDo you want to play again?", title="WON!")
            if u == "Yes":
                exit_loop = True
                break
            else:
                close_program("user didnt want to play again")

        window.find_element("WORD").update(" ".join(guess_word))

        print(guess, guess_word)
