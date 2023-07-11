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
1.4
Old save files will now be compatible with new versions
Theme setting uses a dropdown
More Themes
Few more words
Settings now uses a icon
Minor code optimizations
Better error messages
Win popup will not ask user to play again
window now saves location
Minor other changes
1.5
Modes
Tutorial
Debugger
    |_ Its usualy disabled, to enable it change the variable debug to True
        or go to settings > delete save > type: ENABLE DEBUG
New Icon
Fixed and Improved compatibility system
Improved credits menu
App license is now included in the app itself
Bug fixes
"""



from random import choice as choose
from random import randint as random_int
from playsound import playsound
import Word_library as wl
import PySimpleGUI as sg
from os import remove
from os.path import exists
from json import  dump, load
from sys import exit as close_program


ICON = b"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"
LICENSE = """MIT License

Copyright (c) 2023 blabla_lab

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

WORDS = wl.WORDS
MODE_COUNTRY_WORDS = wl.COUNTRIES
HARD_WORDS = wl.HARD_WORDS

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

SOUNDS = {"click":"WordPredict/sfx/click.wav", 
        "guess_correct":"WordPredict/sfx/guess_correct.wav", 
        "guess_wrong":"WordPredict/sfx/guess_wrong.wav", 
        "levelup":"WordPredict/sfx/levelup.wav", 
        "word_done":"WordPredict/sfx/word_done.wav", 
        "word_fail":"WordPredict/sfx/word_fail.wav"}


# debug related stuff
DEBUG_DOC = """DEBUG DOCUMENTATION
basically you can type a python command and it will run it

custom commands:
!help - view this page
!vars - view the variables and functions, and their value
!delete save - deletes save file
"""

DEBUG_VARS_DOC = {
    # short decription for variables in the app
    "DEBUG_USE_CUSTOM_WORD": "set a custom word for the next game",
    "DEBUG_DOC": "DEBUG DOCUMENTATION", 
    "points_required_for_level": "points required for the next level",
    "custom_words": "custom words to add to the words base",
    "SOUNDS_ENABLED": "enable sounds",
    "SOUNDS": "a dictionary with the name of the sound and the path to it",
    "theme": "theme of the app",
    "version": "version of the app",
    "name": "name of the app",
    "save_file": "name of the save file",
    "CREDITS": "credits",
    "gradual_difficulty": "enable gradual difficulty",
    "gradual_difficulty_word_length": "length of the word for gradual difficulty increases with level",
    "show_first_letter": "show first letter",
    "show_last_letter": "show last letter",
    "level": "your level in game",
    "points": "your points in game, gained by guessing words",
    "tries": "tries left",
    "save_file": "name of the save file",
    "save_dictionary": "contents of the save file",
    "auto_font_size_factor": "The game title in window and the word shown are automatically scaled. increasing the number makes the font smaller",
    "DEBUG_FUNCTION" : "a one line code to run every timeout(1.5 seconds)\nHow to: DEBUG_FUNCTION = ['COMMAND', GLOBALS, LOCALS]",
    "FONT" : "defualt font",
    "WORDS" : "list of words to guess",
    "LETTERS" : "list of letters",
    "RECOMMENDED_THEMES" : "list of themes for the settings menu dropdown",
    "DEBUG_MAINTAIN_WINDOW_POSITION" : "maintain window position, when game restarts",
    "DEBUG_ALWAYS_MAXIMIZED" : "window always maximized",
    "DEBUG_VARS_DOC" : "documentation for vars in ths vars picker, your not supposed to see this from here instead you should choose a variable and check its description",
    "DEBUG_SAVE" : "If False the game will never save",
    "DEBUG_AUTO_FONT_SIZE" : "If False the word to guess and title will never be scaled depending on window size",
    "MODES" : "list of modes for the settings menu dropdown",
    "mode" : "the current mode",
}


DEBUG = False  # to enable debugger go to settings > delete save > and type ENABLE DEBUG 
DEBUG_USE_CUSTOM_WORD = None
auto_font_size_factor = 20
DEBUG_FUNCTION = None
DEBUG_MAINTAIN_WINDOW_POSITION = True
DEBUG_AUTO_FONT_SIZE = True
DEBUG_ALWAYS_MAXIMIZED = False
DEBUG_SAVE = True



VERSION = 1.5
NAME = "WordPredict"
SAVE_FILE = f"{NAME} Save.json"
CREDITS = """Developer - blabla_lab
GUI Library - PySimpleGUI
Sounds      - Nathan Gibson
"""




#! DEFAULT VALUES
global gradual_difficulty,gradual_difficulty_word_length,show_first_letter,show_last_letter,level,points,points_required_for_level
gradual_difficulty = True
gradual_difficulty_word_length = 3
show_first_letter = True 
show_last_letter = True
show_random_letter = True
level = 1
points = 0
user_tries = 6
tries=user_tries
points_required_for_level = 3
custom_words = []
SOUNDS_ENABLED = True
theme = "WordPredict"
mode = "Classic"
#! END DEFAULT VALUES


HOW_TO_PLAY = f"""How to play:
A word is randomly choosen from a list stored inside this program
To guess a word click the letter below the displayed word.
You can only guess the word letter by letter.
You have {tries} tries to guess the word.
Every time you guess a wrong guess one try is lost.
If the tries are 0 you lose a point.
If you guess the word correctly you gain a point."""



# mode name : [mode description, should gradual diffculty be on?, words list, tries]
MODES = {"Classic" : ["The Classic word predict mode,\nGuess the randomly choosen word", True, WORDS, user_tries], 
         "Countries" : ["Guess the randomly choosen country!\nNOT all countries are in the database", False, MODE_COUNTRY_WORDS, user_tries],
         "Hardcore" : ["Guess the randomly choosen hard word with only 2 tries!", False, HARD_WORDS, 2],
         } 





def popup_list(_list, title="choose", default = None):
    e,v = sg.Window(title, [[sg.T(title)], [sg.Listbox(_list, size=(50, 10), key="-LIST-", default_values=default)], [sg.OK()]]).read(close=True)
    if not e == "OK": return False
    else:return "".join(v["-LIST-"])
    

def auto_font_size():
    try:
        window.find_element("WORD").update(font=("LCD Solid", window.size[1] // auto_font_size_factor ))
        window.find_element("Title").update(font=(FONT[0], window.size[1] // auto_font_size_factor ))

    except Exception: return False


def save():
    global save_dictionary
    with open(SAVE_FILE, "w") as f:
        save_dictionary = { 
            "gradual_difficulty": gradual_difficulty,
            "gradual_difficulty_word_length": gradual_difficulty_word_length,
            "show_first_letter": show_first_letter,
            "show_last_letter": show_last_letter,
            "show_random_letter": show_random_letter,
            "level": level,
            "points": points,
            "tries": user_tries,
            "custom_words": custom_words,
            "points_required_for_level": points_required_for_level,
            "SOUNDS_ENABLED":SOUNDS_ENABLED,
            "SOUNDS": SOUNDS,
            "theme": theme,
            "mode" : mode,
        }
        dump(save_dictionary, f, indent=1)

def play_sound(sound):
    if SOUNDS_ENABLED:
        playsound(SOUNDS[sound],block=False)


def get_save():
    with open(SAVE_FILE, "r") as f:
        return load(f)
    
def load_from_save(item):
    load_dictionary = get_save()
    try:x = load_dictionary[item]
    except KeyError as e: 
        not_found_keys.append(str(e).replace("'", "")) # for some reason without using replace they are appended like this: "'SOUNDS'"
        return False
    else:return x


    
def choose_word(choose_from):
    '''picks a random word from choose_from

    Args:
        choose_from (list): list to pick the words from
    '''
    
    if gradual_difficulty:
        i = 0
        while True:
            i += 1
            print(f"Making up a word...{i}, gd:{gradual_difficulty}\ngdwl:{gradual_difficulty_word_length}")
            x = choose(choose_from)

            # if the game tried too much to find a word then its a probably error with gd.
            if i > len(choose_from) * 2:
                sg.popup_error("The game have been trying too much to find a word\nthis is probably happening because this mode isn't compatible\nwith gradual difficulty setting")
                close_program(f"ERROR: TRYING TO FIND A WORD FOR TOO LONG\n\nLOOP COUNT:{i}\nMAX AMOUNT OF LOOPS:{len(choose_from) * 2}")

            if len(x) <= gradual_difficulty_word_length:
                del i
                return x
    else: 
        return choose(choose_from)


sg.theme_border_width(3)

FONT = (None, 18)  
sg.set_options(font=FONT, element_padding=(5,5), auto_size_text=True, auto_size_buttons=True, icon=ICON)
sg.theme('TealMono')




if not exists(SAVE_FILE):
    x = sg.popup_yes_no("This is the first time you have played the game.\nDo you know how to play this game?", title="First play") 
    if x == "Yes": pass
    elif x == "No": 
        sg.popup(HOW_TO_PLAY, title="How to play")
    else: close_program()
    with open(SAVE_FILE, "w"):
        pass
    save()

    






#! load save
#! COMPATIBLITY
# Variable name in strings as a key, for the value it should be its default value
SAVE_KEYS =  {
"gradual_difficulty_word_length":3, 
"level":1, 
"tries":6 ,
"points":0, 
"points_required_for_level":3,
"show_first_letter":True,
"show_last_letter":True,
"show_random_letter":True,
"gradual_difficulty":True,
"SOUNDS_ENABLED":True,
"custom_words":[],
"SOUNDS":{"click": "WordPredict/sfx/click.wav","guess_correct": "WordPredict/sfx/guess_correct.wav","guess_wrong": "WordPredict/sfx/guess_wrong.wav","levelup": "WordPredict/sfx/levelup.wav","word_done": "WordPredict/sfx/word_done.wav","word_fail": "WordPredict/sfx/word_fail.wav"},
"theme":"'WordPredict'",
"mode":"Classic"
}


not_found_keys = []
#! variables to load
user_tries=load_from_save("tries")
gradual_difficulty = load_from_save("gradual_difficulty")
gradual_difficulty_word_length = load_from_save("gradual_difficulty_word_length")
show_first_letter = load_from_save("show_first_letter")
show_last_letter = load_from_save("show_last_letter")
show_random_letter = load_from_save("show_random_letter")
level = load_from_save("level")
points = load_from_save("points")
points_required_for_level = load_from_save("points_required_for_level")
SOUNDS_ENABLED = load_from_save("SOUNDS_ENABLED")
SOUNDS = load_from_save("SOUNDS")
theme = load_from_save("theme")
mode = load_from_save("mode")

#! if there any issues with loading save
if not_found_keys != []: # if there some missig keys , make them with theri defuakts as values
    if sg.popup_ok("there {2} {0} missing key{3}\nand {4} {2}:\n-{1}\n\nPress Ok to fix {5}".format(
        len(not_found_keys), 
        "\n-".join(not_found_keys), 
        "is" if len(not_found_keys) == 1 else "are", 
        "" if len(not_found_keys)==1 else "s",
        "it" if len(not_found_keys) == 1 else "they",
        "it" if len(not_found_keys)==1 else "them" )) != "OK":close_program("BAD SAVE")   
    
    for i in not_found_keys: 
        sg.one_line_progress_meter(f"fixing: {i}", not_found_keys.index(i) + 1, len(not_found_keys))
        for x in SAVE_KEYS:
            if x == i:
                print(f"{i} == {x}")
                exec(f"{i} = {SAVE_KEYS[x]}", globals(), locals())
                break

            else: print(f"{i} != {x}")
    sg.one_line_progress_meter_cancel()


print("Loaded save file")
#! end of load save






# sg.theme("LightGrey3")
# PySimpleGUI Theme.
# Generated using Themera v1.0.0., v 2.0.0
sg.theme_add_new('WordPredict', 
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


sg.theme_add_new(
    'WordPredictDarkGreen', 
    {
        'BACKGROUND': 'black', 
        'TEXT': '#ffffff', 
        'INPUT': '#c8c8c8', 
        'TEXT_INPUT': 'black', 
        'SCROLL': '#36ff83', 
        'BUTTON': ('black', '#36ff83'), 
        'PROGRESS': ('#36ff83', '#005320'), 
        'BORDER': 0, 
        'SLIDER_DEPTH': 0, 
        'PROGRESS_DEPTH': 0, 
    })


sg.theme_add_new("WordPredictDarkRed",  {'BACKGROUND': '#111111',
    'TEXT': 'white',
    'INPUT': '#888888',
    'TEXT_INPUT': 'black',
    'SCROLL': '#a0a0a0',
    'BUTTON': ('white', '#ff4444'),
    'PROGRESS': ('#ff4444', '#420000'),
    'BORDER': 0,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0})


sg.theme_add_new("WordPredictDark",  {'BACKGROUND': '#111111',
    'TEXT': 'white',
    'INPUT': '#888888',
    'TEXT_INPUT': 'white',
    'SCROLL': '#a0a0a0',
    'BUTTON': ('white', '#42b4ff'),
    'PROGRESS': ('#42b4ff', '#222222'),
    'BORDER': 0,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0})

sg.theme_add_new(
    'WordPredictGreen', 
    {
        'BACKGROUND': '#f1f1f1', 
        'TEXT': '#000000', 
        'INPUT': '#c8c8c8', 
        'TEXT_INPUT': 'black', 
        'SCROLL': '#36ff83', 
        'BUTTON': ('black', '#36ff83'), 
        'PROGRESS': ('#36ff83', '#b3ffd0'), 
        'BORDER': 0, 
        'SLIDER_DEPTH': 0, 
        'PROGRESS_DEPTH': 0, 
    })


sg.theme_add_new("WordPredictRed",  {'BACKGROUND': '#f1f1f1',
    'TEXT': '#000000',
    'INPUT': '#c8c8c8',
    'TEXT_INPUT': 'black',
    'SCROLL': '#a0a0a0',
    'BUTTON': ('white', '#ff4444'),
    'PROGRESS': ('#ff4444', '#ff9d9d'),
    'BORDER': 0,
    'SLIDER_DEPTH': 0,
    'PROGRESS_DEPTH': 0})




RECOMMENDED_THEMES = ["WordPredict", "WordPredictDark", "WordPredictDarkRed", "WordPredictDarkGreen", "WordPredictGreen", "WordPredictRed"]
sg.theme(theme)
print("Applied theme")






#sound checks
def run_sound_check():
    for i in list(SOUNDS.keys()):
        sg.popup_quick_message(f"playing: {i}", keep_on_top=True)
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
                 keep_on_top=True,)
        if user_input == "Advanced Options":
            sound_manager_layout = [
                [sg.Text("Sounds Enabled: {0}".format(SOUNDS_ENABLED))],
                [sg.T("Sounds List:")],
            ]
            for i in list(SOUNDS.keys()):
                sound_manager_layout.append([sg.T(i, expand_x=True), sg.In(SOUNDS[i], key=i), sg.FileBrowse(), sg.T("Valid path" if exists(SOUNDS[i]) else "Invalid Path", text_color = "Black" if exists(SOUNDS[i]) else "Red")])
            sound_manager_layout.append([sg.OK(), sg.B("Continue without sounds")])
            sound_manager = sg.Window("Sounds", sound_manager_layout)
            sme,smv = sound_manager.read(close=True)
            if sme == "OK":
                for i in list(SOUNDS.keys()):
                    SOUNDS[i] = smv[i]
                SOUNDS_ENABLED = True
                if sg.popup_yes_no("Changed sounds directory\nrun a test?", title="Sounds") == "Yes":
                    run_sound_check()
            elif sme == "Refresh Paths":
                continue
            else:
                SOUNDS_ENABLED = False
                sg.popup_quick_message("Failed to change sounds directory")
            break
        else:break
    else:break
del Not_found_sounds


# end of sound checks


window_position = None

while True:
    #* game loop

    tries=user_tries
    bad_letters = []


    if type(DEBUG_USE_CUSTOM_WORD) is str and DEBUG is True:
        word = DEBUG_USE_CUSTOM_WORD
        DEBUG_USE_CUSTOM_WORD = None
    else:
        # modes section
        mode_gradual_difficulty = MODES[mode][1]
        mode_words_list = MODES[mode][2]
        mode_tries = MODES[mode][3]

        gradual_difficulty = mode_gradual_difficulty
        tries = mode_tries
        word = choose_word(mode_words_list)
        




    word_in_a_list_form = list(word)
    guess_word = []
    for i in word_in_a_list_form:
        guess_word.append("_")
    
    if show_first_letter is True: 
        guess_word[0] = word_in_a_list_form[0]
    if show_last_letter is True:
        guess_word[-1] = word_in_a_list_form[-1]
    if show_random_letter is True:
        if len(word_in_a_list_form) != 3:
            while True:
                s = random_int(1, len(word_in_a_list_form)-1) # random letter to reveal
                print(f"----\nguess_word:{guess_word}\nguess_word[s]:{guess_word[s]}\ns:{s}\nlen of word_in_a_list_form:{len(word_in_a_list_form)}\n")
                if guess_word[s] == "_":
                    guess_word[s] = word_in_a_list_form[s]
                    break
            



    layout = [  [sg.T(f"{NAME}!", justification="c", expand_x=True, key="Title", enable_events=True)],
                [sg.T(f"Level:{level}", font=(FONT[0], FONT[1], "bold"), expand_x=True, expand_y=True),sg.T(f"Tries:{tries}", font=(FONT[0], FONT[1], "bold"), expand_x=True, expand_y=True, k="tries")],
                [sg.ProgressBar(points_required_for_level, orientation="h", k="-PR-", expand_x=True, expand_y=True), sg.T(f"Points:{points}", font=(FONT[0], FONT[1], "bold"), expand_x=True, expand_y=True)],
                [sg.T(" ".join(guess_word), key="WORD", relief=sg.RELIEF_SUNKEN, justification="c", expand_x=True, font=("LCD Solid", 18, "bold"), tooltip="the word you need to guess its missing letters")],
                [sg.T("Guess a letter:", expand_x=True)],
                [sg.B(i, expand_x=True, pad=(1,1), expand_y = True) for i in LETTERS[0:14]],
                [sg.B(i, expand_x=True, pad=(1,1), expand_y = True) for i in LETTERS[14:]],
                [sg.B("Settings", expand_x=True)],]
    

    window = sg.Window(NAME, layout, resizable=True, finalize=True)
    
    window.set_min_size((534, 346))

    if DEBUG_ALWAYS_MAXIMIZED: window.maximize()

    if DEBUG_MAINTAIN_WINDOW_POSITION:
        if window_position is None:
            window.move_to_center()
        else:
            window.move(window_position[0], window_position[1])

    window.find_element("-PR-").update(points, points_required_for_level)
   
    auto_font_size()

    exit_loop = False

    while not exit_loop:
        event, values = window.read(1500, timeout_key="-TIMEOUT-")
        # event, values = window.read()
        print(f"event:{event}\nvalues:{values}")


        if event == "-TIMEOUT-":
            # visual warning
            if tries < 3: window["tries"].update(text_color = "Red")
            else: window["tries"].update(text_color = None)
            auto_font_size()
            if DEBUG is True:
                if DEBUG_FUNCTION is not None:

                    exec(DEBUG_FUNCTION[0], DEBUG_FUNCTION[1], DEBUG_FUNCTION[2]) 
                    # print(f"DEBUG_FUNCTION:{DEBUG_FUNCTION}")
            continue

            

        
        


        play_sound("click")
        save()
        auto_font_size() # there is an error that happens when you close a window, it s not important as the program is already done when the error comes

        
        if event == sg.WIN_CLOSED:
            window.close()
            close_program()


        elif event == "Title" and DEBUG is True:
            #* debugger
            command = sg.popup_get_text("PLEASE BECAREFUL WITH TYPING A COMMAND\nAS YOU CAN DAMAGE YOUR SYSTEM\n\nEnter a Command OR type '!help' for help:", title="debug")
            play_sound("click")
            # special commands
            if command == None or command.strip() == "" or command == "OK": continue
            elif command == "!help":sg.popup_scrolled(DEBUG_DOC, title="help")
            elif command == "!delete save": 
                if sg.popup_yes_no("Are you sure you want to delete the save file?", title="delete save") == "Yes": 
                    remove(SAVE_FILE)
                    sg.popup_quick_message("deleted", non_blocking=False)
                    close_program(0)
            elif command == "!vars":
                var = popup_list(sorted([v for v in globals().keys() if not v.startswith('_')]), title="variable picker")
                try:
                    sg.popup_scrolled(f"name: {var}\nvalue: {globals()[var]}\ndescription: {'undocumented' if var not in DEBUG_VARS_DOC.keys() else DEBUG_VARS_DOC[var]} ", title=f"value of {var}")
                except KeyError: pass
                del var

            else:         
                try:exec(command, globals())
                except Exception as e:sg.popup_error(f"error\n{e}")
                else:sg.popup_quick_message("command executed")
            
                


            


        elif event == "Settings":
            settings_layout = [
                [sg.T("Settings")],
                [sg.Checkbox("Gradual difficulty", key="gd", default=gradual_difficulty, 
                              tooltip="this mode will give you words\nbased on your level, for example\nlevel 1 will give you words ranging\nfrom 3-4 letters of length"), 
                              sg.T(f"Gradual diffculty max word length:{gradual_difficulty_word_length}",
                                    tooltip="this tells you the number of letters long words can come, based on level")],
                
                [sg.Checkbox("Show first letter", key="sf", default=show_first_letter)],
                [sg.Checkbox("Show last letter", key="sl", default=show_last_letter)],
                [sg.Checkbox("Show random letter", key="sr", default=show_random_letter)],
                [sg.Checkbox("Sounds", k="sounds", default=SOUNDS_ENABLED), sg.B("Test sound")],
                [sg.T("Tries:"), sg.In(user_tries, key="tries", disabled=True if mode == "Hardcore" else False)],
                [sg.T("Themes"), sg.DropDown(RECOMMENDED_THEMES, default_value=sg.theme(), key="-THEME-", readonly=True)],
                [sg.T(f"Game mode: {mode}", expand_x=True, key = "mode"), sg.B("Change mode")],
                [sg.B("Add new word"), sg.B("Credits"), sg.B("View words"), sg.B("Delete save")], 
                [sg.OK(), sg.T("the game will restart to apply changes!")]
            ]
            settings_window = sg.Window("Settings", settings_layout)
            while True:
                se, sv = settings_window.read()
                print(se, sv)
                invalid = False
                play_sound("click")
                if se == sg.WIN_CLOSED: 
                    sg.popup_quick_message("Didnt save settings")
                    break
                if se == "Add new word":
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

                    WORDS.append(user_custom_word.lower())
                
                elif se == "Change mode":
                    l=[
                        [sg.T("Game modes:")],
                        [sg.Drop(list(MODES.keys()), readonly=True, key="-MODE-", default_value=mode, enable_events=True, expand_x=True)],
                        [sg.T("Description:")],
                        [sg.T(" ", key="-DESC-")],
                        [sg.OK()]
                    ]
                    w = sg.Window("Change mode", l).finalize()

                    w["-DESC-"].update(MODES[mode][0])
                    while True:
                        e,v = w.read()
                        if e == sg.WIN_CLOSED:
                            break
                        elif e == "-MODE-":
                            w["-DESC-"].update(MODES[v["-MODE-"]][0])
                        elif e == "OK":
                            mode = v["-MODE-"]
                            print(mode)
                            sg.popup_quick_message("mode changed")
                            break
                    
                    settings_window["mode"].update(f"Game mode: {mode}")

                    w.close()
                    del w,l,e,v   


                        

                elif se == "OK":
                    try:
                        gradual_difficulty = sv["gd"]
                        show_first_letter = sv["sf"]
                        show_last_letter = sv["sl"]
                        show_random_letter = sv["sr"]
                        SOUNDS_ENABLED = bool(sv["sounds"])
                        user_tries = int(sv["tries"])
                        theme = "".join(sv["-THEME-"])
                        sg.theme(theme)
                        save()
                    except (ValueError, TypeError) as e:
                        sg.popup_error(f"error saving data\nYou probably typed something wrong\n{e}")
                    
                    window.close()
                    exit_loop=True
                    break


                elif se == "Test sound":
                    sg.popup_ok("Click ok to start", title="test sound")
                    run_sound_check()
                elif se == "Credits":
                    x = sg.popup(CREDITS, title="credits", custom_text=("License", "How to play"))
                    play_sound("click")
                    if x == "License":
                        sg.popup_scrolled(LICENSE, title="license")
                        play_sound("click")
                    elif x == "How to play":
                        sg.popup_scrolled(HOW_TO_PLAY, title="how to play")
                elif se == "View words":
                    sg.popup_scrolled(", ".join(WORDS), title="words base")
                    play_sound("click")

                elif se == "Delete save":
                    confirm = sg.popup_get_text("ARE YOU SURE YOU WANT TO DELETE YOUR SAVE FILE\nALL OF YOUR PROGRESS WILL BE LOST!\nTO CONFIRM TYPE THIS SENTENCE:\nI AM SURE THAT I WANT TO DELETE MY SAVE FILE\n", title="Confirm")
                    play_sound("click")
                    if confirm == "I AM SURE THAT I WANT TO DELETE MY SAVE FILE":
                        remove(SAVE_FILE)
                        sg.popup_ok("DELETED SAVE FILE\n\ngame will close to apply changes")
                        play_sound("click")
                        close_program()
                    elif confirm == "ENABLE DEBUG":
                        DEBUG = True
                        sg.popup_quick_message("DEBUGGER ENABLED")


            settings_window.close()
            continue

               


        #* the checking section *#


        guess = event
        if guess not in LETTERS: continue
      
        
        
        #* this checks if the user guessed correctly

        # check if guess is wrong
        if not guess in word_in_a_list_form:
            if guess not in bad_letters:
                # guess wrong
                play_sound("guess_wrong")
                tries -= 1
                bad_letters.append(guess)
                window.find_element("tries").update(f"Tries:{tries}")
                if tries == 0: # the player lost
                    points -= 1
                    play_sound("word_fail")
                    sg.popup_ok(f"You lose\nthe word was:{word}")
                    sg.popup_quick_message("-1 point", auto_close_duration=1)
                    tries = user_tries
                    if DEBUG_MAINTAIN_WINDOW_POSITION:window_position = window.current_location(more_accurate=True)
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
            if DEBUG_MAINTAIN_WINDOW_POSITION:window_position = window.current_location(more_accurate=True)
            window.close()
            play_sound("word_done")
            points += 1
            sg.popup_quick_message("+1 point", auto_close_duration=1)
            if points >= points_required_for_level:
                sg.popup_quick_message(f"Level up, Your now on level {level}", title="level up")
                play_sound("levelup")
                level += 1
                points_required_for_level +=  points_required_for_level
                gradual_difficulty_word_length += 1
            
            save()

            u = sg.popup_quick_message(f"You won!\nThe word was {word}.", title="WON!", non_blocking=False, auto_close_duration=1.6)

            exit_loop = True
            break

        window.find_element("WORD").update(" ".join(guess_word))

        print(guess, guess_word)
