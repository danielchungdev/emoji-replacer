from logging.config import listen
from pynput.keyboard import Key, Listener
import pyautogui

replacements = {
    "skull": "penis",
    "eyes": "asdfom"
}

macro_starter = ":"
macro_ender = ":"
typed_keys = []
listening = False

def on_press(key):
    global typed_keys
    global listening

    key_str = str(key).replace('\'', '')

    if listening: 
        if key_str.isalpha() and key_str != macro_ender:
            typed_keys.append(key_str)
        if key_str == macro_ender:
            print("end")
            candidate_keyword = ""
            candidate_keyword = candidate_keyword.join(typed_keys)

            if candidate_keyword != "":
                if candidate_keyword in replacements.keys():
                    print(candidate_keyword)
                    pyautogui.press('backspace', presses=len(candidate_keyword) + 2)
                    pyautogui.typewrite(replacements[candidate_keyword])
                    listening = False
    elif key_str == macro_starter and listening == False:
        print("start")
        typed_keys = []
        listening = True


def main():
    print("Now listening...")
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()