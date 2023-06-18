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
1.3
sounds
icons
fixed penalty bug
modifed level system
"""


from random import choice as choose
from os.path import exists
from playsound import playsound
from random import randint
import PySimpleGUI as sg
from os import remove
from os.path import exists
from json import  dump, load
from sys import exit as close_program
import gc

SPEAKER_ICON = b"iVBORw0KGgoAAAANSUhEUgAAAA0AAAAOCAYAAAD0f5bSAAABAElEQVQokY2SO04DMRRFz5s2ElISUriYCsICRtBMAz0sA3YAqwg7SJYRemjSgCIahICAkFK4mJCRIqZ+NOOR52MJN5av3/H1+8hkOsdfN1cXAKiqkxQQABEBIPIuFGAynTcBf69BVVBsBqztTyuwBqXJmNgMxAlru9XYDIMAgJRf0cXyXRbLjyr4+vK8FevnpABpcqRpMq4cb2d3QadaTv8Fo4enz5oQAt++bLeTe6ALfH79xvVUXlaWLC8UwOzvid3s9PT4AIBmcSibHGV54Q5iNztG/Z6EHCmL5gsA3D+uGPV7ZHkRdGxOBGcnh2R50XL0B6AFdYHZ9ldiM6zS+AP+PHyWOxSTEQAAAABJRU5ErkJggg=="
SAVE_ICON = b"iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAAAsUlEQVRIie2WrQ/CMBBH3xEcCkEyXzeN518HDRY3NAKBQh9mS0o3klLaHiF7rqIfv767tKKq9CjA4XQhht3WvYzDeZv1SgBa1wAgIgAsolbPyJI+WW5a1wzrCsBwk9UT1thQ8W7RxGESsdXsoWCQUNRrRJ+EBMC4P0N+J2Ep7Ks01d07Qqf1He6PnU6dpBSzw+yMEpZ2aZ9wdvgtf/mnsd1Qzt0VgNv98dG7mOBawCDhE0JcNSfHRvXqAAAAAElFTkSuQmCC"
GEAR_ICON = b"iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAYAAAByDd+UAAABAUlEQVRIid2WMQ+CMBSEvxo3WTAhOsvG7O5f11lXndTVKBEHda4DVC3hUWIMFW8ij2vLvWt7KK01JZiCEuoSJL5V7zkm+Tr6aXYDIBoGZQWSUhdq52lf4WZ/1ACzYSBxXN415WnwoFCttwcA0ss9VzqNK4mL1a52Imnc+1rgw0PzkExGZjdaXhhlLgU1PN/nsPAuicfWi6ZfTNERw6sYZ3XMn4cNIN04ld5LaF3h/y/49LDBefs0Jy34u0ujME+Lci52/qZRp/MVqEx8C51NCzVfbmtz8Nv4ncQ3npmcdHmcZjcF8PxHEnarFw8BiMIB8FIahQPr/Ji6BIn/1iHAg8IHOnFuSExQE8cAAAAASUVORK5CYII="
ICON = b"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"

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

SOUNDS = {"click":"WordPredict/sfx/click.wav", 
        "guess_correct":"WordPredict/sfx/guess_correct.wav", 
        "guess_wrong":"WordPredict/sfx/guess_wrong.wav", 
        "levelup":"WordPredict/sfx/levelup.wav", 
        "word_done":"WordPredict/sfx/word_done.wav", 
        "word_fail":"WordPredict/sfx/word_fail.wav"}



VERSION = 1.3
NAME = "WordPredict"
SAVE_FILE = f"{NAME} Save.json"
CREDITS = """Developer - blabla_lab
GUI Library - PySimpleGUI
Icons       - Lucid V1.2 on itch.io
Sounds      - Nathan Gibson
"""


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
            "SOUNDS": SOUNDS,
        }
        dump(save_dictionary, f, indent=1)

def play_sound(sound):
    if SOUNDS_ENABLED:
        playsound(SOUNDS[sound],block=False)


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
sg.set_options(font=FONT, element_padding=(5,5), auto_size_text=True, auto_size_buttons=True, icon=ICON)

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
    if points < 0: raise KeyError("Points must be equal or greater than 0")
    for i in save_dictionary["custom_words"]:
        WORDS.append(i)
    points_required_for_level = save_dictionary["points_required_for_level"]
    SOUNDS = save_dictionary["SOUNDS"]
except (KeyError, FileNotFoundError) as e:
    sg.popup_error(f"deleting save file...\n\nmore info:\n{e} was not found")
    remove(SAVE_FILE)
    close_program("bad save file")
print("Loaded save file")


# sg.theme("LightGrey3")
# PySimpleGUI Theme.
# Generated using Themera v1.0.0., v 2.0.0
sg.theme_add_new(
    'Dark', 
    {
        'BACKGROUND': 'black', 
        'TEXT': '#a4daff', 
        'INPUT': '#c8c8c8', 
        'TEXT_INPUT': 'black', 
        'SCROLL': '#a4daff', 
        'BUTTON': ('black', '#a4daff'), 
        'PROGRESS': ('#13406c', '#a4daff'), 
        'BORDER': 0, 
        'SLIDER_DEPTH': 0, 
        'PROGRESS_DEPTH': 0, 
    })



sg.theme_add_new('default', 
    {'BACKGROUND': '#f1f1f1',
    'TEXT': 'black',
    'INPUT': '#c8c8c8',
    'TEXT_INPUT': '#171413',
    'SCROLL': '#a0a0a0',
    'BUTTON': ('black', '#a4daff'),
    'PROGRESS': ('black', '#a0a0a0'),
    'BORDER': 0,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0})
sg.theme('default')
print("Applied theme")




#sound checks

def run_sound_check():
    for i in list(SOUNDS.keys()):
        sg.popup_quick_message(f"playing: {i}", image=SPEAKER_ICON, keep_on_top=True)
        playsound(SOUNDS[i])

while True:
    SOUNDS_ENABLED = True
    Not_found_sounds = []
    for i in (SOUNDS.values()):
        if not exists(i):
            Not_found_sounds.append(i)
            SOUNDS_ENABLED = False
            break
    if SOUNDS_ENABLED is False:
        user_input = sg.popup("Sounds have been disabled\nReason:\nThese sounds were not found:\n{}\nPlease reinstall the program\nor make sure the sfx folder is \nin the same path as the program".format('\n'.join(Not_found_sounds)), 
                 title="Error",
                 custom_text=("Continue without sounds", "Advanced Options"),
                 keep_on_top=True,
                 image=SPEAKER_ICON)
        if user_input == "Advanced Options":
            sound_manager_layout = [
                [sg.Image(SPEAKER_ICON),sg.Text("Sounds Enabled: {0}".format(SOUNDS_ENABLED))],
                [sg.T("Sounds List:")],
            ]
            for i in list(SOUNDS.keys()):
                sound_manager_layout.append([sg.T(i), sg.In(SOUNDS[i], key=i), sg.FileBrowse()])
            sound_manager_layout.append([sg.OK(), sg.B("Continue without sounds")])
            sound_manager = sg.Window("Sounds", sound_manager_layout, icon=SPEAKER_ICON)
            sme,smv = sound_manager.read(close=True)
            if sme == "OK":
                for i in list(SOUNDS.keys()):
                    SOUNDS[i] = smv[i]
                SOUNDS_ENABLED = True
                if sg.popup_yes_no("Changed sounds directory\nrun a test?", title="Sounds") == "Yes":
                    run_sound_check()
            else:
                SOUNDS_ENABLED = False
                sg.popup_quick_message("Failed to change sounds directory")
            break
        else:break
    else:break

gc.collect()

# end of sound checks





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
        # event, values = window.read(1500, timeout_key="-TIMEOUT-")
        event, values = window.read()
        play_sound("click")

        
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
                [sg.T("Themes"), sg.Listbox(["default", "Dark default"], default_values=sg.theme(), select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, key="-THEME-")],
                [sg.B("Test sound")],
                [sg.B("Add new word"), sg.B("Credits"), sg.B("view words"), sg.B("Delete save")], 
                [sg.OK(), sg.T("the game will restart to apply changes!")]
            ]
            settings_window = sg.Window("Settings", settings_layout)
            while True:
                se, sv = settings_window.read()
                play_sound("click")
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

                elif se == "Test sound":
                    sg.popup_ok("Click ok to start", title="test sound", image=SPEAKER_ICON)
                    run_sound_check()
                elif se == "Credits":
                    sg.popup_no_buttons(f"{NAME} {VERSION}\n\nCredits:\n{CREDITS}\n\nOther:\nWords in the game:{len(WORDS)}", title="Credits")
                    play_sound("click")
                elif se == "view words":
                    sg.popup_scrolled(", ".join(WORDS), title="words base")
                    play_sound("click")
                elif se == "Delete save":
                    confirm = sg.popup_get_text("ARE YOU SURE YOU WANT TO DELETE YOUR SAVE FILE\nALL OF YOUR PROGRESS WILL BE LOST!\nTO CONFIRM TYPE THIS SENTENCE:\nI AM SURE THAT I WANT TO DELETE MY SAVE FILE\n", title="Confirm")
                    if confirm == "I AM SURE THAT I WANT TO DELETE MY SAVE FILE":
                        play_sound("click")
                        remove(SAVE_FILE)
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

                        sg.popup_ok("DELETED SAVE FILE\n\nrestart game to apply changes")
                        play_sound("click")
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
                # guess wrong
                play_sound("guess_wrong")
                tries -= 1
                bad_letters.append(guess)
                window.find_element("t").update(f"Tries:{tries}")
                if tries == 0:
                    points -= 1
                    play_sound("word_fail")
                    sg.popup_ok(f"You lose\nthe word was:{word}")
                    tries = user_tries
                    window.close()
                    break
            

            continue

        for i in range(0, len(word_in_a_list_form)): # it just loops for every letter in the word and check if the guess = the index it reached
            if str(word_in_a_list_form[i]) == str(guess):
                # guess correct
                play_sound("guess_correct")
                guess_word[i] = guess
                if i >= len(word_in_a_list_form):  #if it finished scanning the whole thing
                    break

                


        if guess_word == word_in_a_list_form:
            window.close()
            play_sound("word_done")
            points += 1
            if points >= points_required_for_level:
                sg.popup_quick_message(f"Level up, Your now on level {level}", title="level up")
                play_sound("levelup")
                level += 1
                points_required_for_level +=  2 * level
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
