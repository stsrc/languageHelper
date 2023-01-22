#!/usr/bin/python3

import json
import glob
import random 

def mark_as_hard(data, english_verb, file_object):
    difficult = data['difficult verbs']
    difficult.append(english_verb)
    file_object.truncate(0)
    file_object.seek(0)
    json.dump(data, file_object, indent = 8, ensure_ascii = False)

def remove_from_hard(data, english_verb, file_object):
    difficult = data['difficult verbs']
    for idx, obj in enumerate(difficult):
        if obj == english_verb:
            difficult.pop(idx)
    file_object.truncate(0)
    file_object.seek(0)
    json.dump(data, file_object, indent = 8, ensure_ascii = False)

def learn_czech_difficult_verbs(data, file_object):
    keys = ["infinitiv", "já", "ty", "on/ona/ono", "my", "vy", "oni/ony/ona"] 
    verbs = data['verbs']
    difficult_verbs = data['difficult verbs']
    if not difficult_verbs:
        print("difficult verbs list is empty, aborting")
        return

    while(1):
        english_verb = random.choice(difficult_verbs)
        czech_verbs = verbs[english_verb]
        key = random.randint(0, len(keys) - 1)
        splited_czech_verbs = czech_verbs.split(', ')
        print_string = english_verb + ", " + keys[key] + ": "
        input_char = input(print_string)
        if (input_char == 'h'):
            print(splited_czech_verbs[0])
            input(print_string)
        print('\n\033[92m' + splited_czech_verbs[key] + '\033[0m')
        input_char = input("\nShow all - a; Remove from difficult - b; Next - any key: ")
        if (input_char == 'a'):
            print('\n')
            print(splited_czech_verbs)
        elif (input_char == 'b'):
            remove_from_hard(data, english_verb, file_object)
        print()
        
def learn_czech_verbs(data, file_object):
    keys = ["infinitiv", "já", "ty", "on/ona/ono", "my", "vy", "oni/ony/ona"] 
    verbs = data['verbs']
    while(1):
        english_verb, czech_verbs = (random.choice(list(verbs.items())))
        key = random.randint(0, len(keys) - 1)
        splited_czech_verbs = czech_verbs.split(', ')
        print_string = english_verb + ", " + keys[key] + ": "
        input_char = input(print_string)
        if (input_char == 'h'):
            print(splited_czech_verbs[0])
            input(print_string)
        print('\n\033[92m' + splited_czech_verbs[key] + '\033[0m')
        input_char = input("\nShow all - a; Mark as difficult - b; Next - any key: ")
        if (input_char == 'a'):
            print('\n')
            print(splited_czech_verbs)
        elif (input_char == 'b'):
            mark_as_hard(data, english_verb, file_object)
        print()

def learn_czech(filename):
    file_object = open(filename, 'r+')
    parsed_json = json.load(file_object)
    print("What would you like to learn?")
    for i in parsed_json:
        print(i + "? y/n: ")
        choice = input().lower()
        if (choice == 'y'):
            if (i == 'verbs'):
                learn_czech_verbs(parsed_json, file_object)
                break
            elif (i == 'difficult verbs'):
                learn_czech_difficult_verbs(parsed_json, file_object)
                break


def learn_english(filename):
    print(filename)

def main():
    print("Which language would you like to learn?")
    files = glob.glob("*.json")
    print(files[0] + "? y/n: " ) # TODO: print only filename
#    choice = input().lower()
    choice = 'y'
    if (choice == 'y'):
        learn_czech(files[0])
    else:
        learn_english(files[1])


if __name__ == "__main__":
    main()
