from random import choice as choose
from os.path import exists
from random import randint
import PySimpleGUI as sg
from os import remove
from ujson import dump, load
from sys import exit as close_program
WORDS = ['gate', 'history', 'stove', 'station', 'verse', 'selection', 'stretch', 'cow', 'kittens', 'rule', 
'metal', 'heat', 'birthday', 'blade', 'hand', 'walk', 'territory', 'spring', 'afternoon', 'frog', 
'noise', 'creator', 'bottle', 'toy', 'worm', 'self', 'oven', 'rest', 'purpose', 'limit', 'dirt', 
'pancake', 'smoke', 'seed', 'army', 'boy', 'friction', 'yard', 'pull', 'country', 'meal', 
'society', 'aunt', 'girls', 'car', 'observation', 'pail', 'ring', 'scarf', 'trains', 'suggestion', 
'form', 'pencil', 'coal', 'texture', 'drain', 'receipt', 'liquid', 'deer', 'chalk', 'porter', 
'statement', 'impulse', 'person', 'business', 'loss', 'trick', 'touch', 'sack', 'cabbage', 
'wilderness', 'partner', 'competition', 'instrument', 'minute', 'holiday', 'mitten', 
'morning', 'poison', 'stone', 'hammer', 'end', 'pie', 'knowledge', 'mind', 'dad', 'fire', 
'morning', 'winter', 'fireman', 'step', 'sticks', 'chin', 'grape', 'can', 'rake', 'spoon', 
'treatment', 'weather', 'death', 'porter', 'queen', 'tent', 'look', 'bone', 'shelf', 'amount', 
'bat', 'beds', 'sock', 'advertisement', 'blow', 'chickens', 'wall', 'toothpaste', 'flavor', 
'noise', 'lake', 'ray', 'fear', 'memory', 'skirt', 'bucket', 'bridge', 'basketball', 'bear', 
'crook', 'toothbrush', 'cause', 'cover', 'train', 'reaction', 'fuel', 'quill', 'dogs', 'unit', 
'library', 'chance', 'scent', 'guide', 'committee', 'sign', 'degree', 'slave', 'creature', 
'advice', 'iron', 'week', 'sofa', 'trade', 'country', 'health', 'shape', 'sneeze', 'wealth', 
'land', 'tray', 'smoke', 'cave', 'boat', 'stocking', 'person', 'notebook', 'bell', 'rain', 'bit', 
'actor', 'animal', 'drop', 'throne', 'smash', 'songs', 'appliance', 'sound', 'coach', 'day', 
'cushion', 'juice', 'month', 'verse', 'thaw', 'arrive', 'attempt', 'employ', 'glow', 'order', 
'realize', 'mate', 'untidy', 'arrange', 'face', 'complain', 'last', 'milk', 'multiply', 'live', 
'bat', 'rescue', 'found', 'brake', 'film', 'compete', 'name', 'sip', 'mix', 'count', 'escape', 
'bump', 'kneel', 'mourn', 'plant', 'join', 'grab', 'rot', 'comb', 'stain', 'shiver', 'store', 
'bolt', 'beg', 'glue', 'miss', 'remind', 'chase', 'list', 'nail', 'stir', 'offer', 'jail', 
'imagine', 'interest', 'develop', 'command', 'long', 'reply', 'head', 'applaud', 'divide', 
'wipe', 'invent', 'attack', 'place', 'compare', 'carve', 'tug', 'allow', 'wander', 'shrug', 
'melt', 'gaze', 'lick', 'fit', 'unlock', 'flow', 'reject', 'charge', 'supply', 'concern',
'undress', 'inform', 'wonder', 'provide', 'flower', 'suggest', 'camp', 'wobble', 'smell', 
'influence', 'wail', 'kick', 'radiate', 'support', 'reduce', 'increase', 'hunt', 'trip', 'moan', 
'point', 'memorize', 'encourage', 'understanding', 'communication', 'recommendation',
'administration', 'entertainment', 'responsibility', 'transportation', 'establishment', 
'differentiate', 'unaccountable', 'knowledgeable', 'disillusioned', 'environmental', 
'heartbreaking', 'dysfunctional', 'psychological', 'sophisticated', 'lackadaisical', 
'materialistic', 'administrative', 'overconfident', 'comprehensive', 'scintillating',
'education', 'sense', 'person', 'apparatus', 'level', 'mind', 'cook', 'twist', 'impulse',
'night', 'trouble', 'doubt', 'expert', 'profit', 'opinion', 'hour', 'canvas', 'destruction', 
'stretch', 'smoke', 'soup', 'existence', 'discussion', 'guide', 'limit', 'trick', 'wine', 
'jelly', 'quality', 'polish', 'stop', 'drink', 'manager', 'cloth', 'sky', 'change', 
'punishment', 'tax', 'food', 'laugh', 'fall', 'expansion', 'belief', 'support', 'fiction', 
'slip', 'cork', 'view', 'reason', 'force', 'form', 'bread', 'disgust', 'order', 'page', 
'building', 'smile', 'part', 'pain', 'competition'"sister","cigarette","cancer","courage","sample","application","writing",
"aspect","accident","election","client","entertainment","conversation","mom","science","reflection","passenger","inspector","newspaper","instance","complaint",
"distribution","oven","beer","response","version","two","teaching","resolution","tale","actor",
"paper","people","guitar","fortune","cousin","stranger","negotiation","celebration","funeral","control","possibility","buyer","climate","president","trainer",
"investment","significance","week","selection","tag", "shy", "dive","abstract","accept","accelerate","access","accompany","accord","account","accrue","achieve","acknowledge",
"acquire","act","add","address","adhere","adjust","admit","adopt","administer","admire","adopt","advance","adventurous","advertise","advise","advocate","affair","affect","afford",
"affiliate","affinity","affirm","affix","afford","afloat","affront","after","afternoon","again","against","age","agenda","agent","agree","agricultural","ahead","aim","air","airplane",
"alarm","album","alcohol","alert","alien","align","alive","all","allergic","allow","almost","alone","along","aloud","alphabet","already","also","alter","although","always",
"amazing","ambitious","among","amount","amuse","analyze","ancient","and","angel","anger","angle","angry","animal","announce","annual","anonymous","answer","ant","anxious","any",
"anybody","anyone","anything","anywhere","apart","apartment","apparent","appeal","appear","appetite","appoint","applause","apple","apply","appreciate","apprehensive","approach",
"appropriate","approve","approximately","apricot","aquatic","argue","arm","armed","army","around","arrange","arrest","arrive","arrow","art","article","artificial","artist","artistic",
"arrogant","ashamed","ashamed","asleep","aspect","assemble","assembly","assist","assistant","associate","assume","assure","athlete","atom","attach","attack","attempt","attend","attention",
"attentive","attitude","attract","attractive","attribute","audio","audit","author","authority","automatic","automobile","autumn","available","average","avoid","awake","award","aware","away",
"awful","awkward","axe"]

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

VERSION = 1.0
NAME = "WordPredict"
SAVE_FILE = f"{NAME} Save.json"
CREDITS = """Developer - blabla_lab (H.A)
GUI Library - PySimpleGUI & PySimpleGUIQt"""

sgq = sg

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
    window.find_element("WORD").update(font=("LCD Solid", window.size[1] // 23 ))
    window.find_element("Title").update(font=(FONT[0], window.size[1] // 23 ))


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
sgq.theme("dark2")

FONT = (None, 18)  
sg.set_options(font=FONT, element_padding=(10,10), auto_size_text=True, auto_size_buttons=True)
sgq.set_options(font=FONT, element_padding=(5,5), auto_size_text=True, auto_size_buttons=True)

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

sgq.theme("LightGrey3")
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

sg.theme_add_new('flat', flat_themedict)
sg.theme('flat')


while True:

        

    tries=user_tries
    bad_letters = []

    if gradual_difficulty:
        while True:
            word = choose(WORDS)
            if not len(word) > gradual_difficulty_word_length:
                break
    else:
        word = choose(WORDS)

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
                [sg.B("Settings", expand_x=True), sg.B("Shop")]]

    window = sg.Window(NAME, layout, resizable=True).finalize()

    window.set_min_size((534, 346))

    window.find_element("-PR-").update(points, points_required_for_level)

    auto_font_size()

    exit_loop = False

    while not exit_loop:
        event, values = window.read(1500, timeout_key="-TIMEOUT-")
        
        if event == sg.WIN_CLOSED:
            window.close()
            close_program()
        elif event == "Settings":
            settings_layout = [
                [sgq.T("Settings")],
                [sgq.Checkbox("gradual difficulty", key="gd", default=gradual_difficulty, 
                              tooltip="this mode will give you words\nbased on your level, for example\nlevel 1 will give you words ranging\nfrom 3-4 letters of length"), 
                              sgq.T(f"Gradual diffculty max word length:{gradual_difficulty_word_length}",
                                    tooltip="this tells you the number of letters long words can come, based on level")],
                
                [sgq.Checkbox("show first letter", key="sf", default=show_first_letter)],
                [sgq.Checkbox("show last letter", key="sl", default=show_last_letter)],
                [sgq.T("Tries:"), sgq.In(user_tries, key="tries")],
                [sgq.B("Add new word"), sgq.B("Credits"), sgq.B("view words"), sgq.B("Delete save")], 
                [sgq.OK(), sgq.T("the game will restart to apply changes!")]
            ]
            settings_window = sgq.Window("Settings", settings_layout)
            while True:
                se, sv = settings_window.read()
                invalid = False
                if se == sgq.WIN_CLOSED: 
                    sgq.popup_quick_message("Didnt save settings")
                    break
                elif se == "Add new word":
                    user_custom_word = sg.popup_get_text("Type a word you want to\nadd to the word base:", title="add", background_color="Dark Gray")
                    if user_custom_word is None or user_custom_word.strip() == "":
                        continue
                    for i in list(user_custom_word):
                        print(i)
                        if not i in LETTERS or user_custom_word in WORDS:
                            invalid = True
                            sgq.popup_ok("your word contained something thats not a letter.\nor your word already exists in the words base.", title="error")
                            break
                    if invalid:
                        continue

                    WORDS.append(user_custom_word)


                elif se == "OK":
                    gradual_difficulty = sv["gd"]
                    show_first_letter = sv["sf"]
                    show_last_letter = sv["sl"]
                    user_tries = int(sv["tries"])
                    save()

                    exit_loop=True
                    break
                
                elif se == "Credits":
                    sgq.popup_no_buttons(f"{NAME} {VERSION}\n\nCredits:\n{CREDITS}\n\nOther:\nWords in the game's dictionary:{len(WORDS)}", title="Credits")
                elif se == "view words":
                    sgq.popup_scrolled(WORDS, title="words base")
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
        elif event == "Shop":
            shop_layout = [
                [sg.T("Shop")],

            ]


        #* the checking section *#


        guess = event
      
        
        
        #* this checks if the user guessed correctly

        # check if guess is wrong
        if not guess in word_in_a_list_form:
            if guess not in bad_letters:
                # sgq.popup_quick_message("Wrong.", auto_close_duration=0.5, non_blocking=False)
                tries -= 1
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
