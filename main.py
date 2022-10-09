#!/usr/bin/python3

import json
import glob
import random 

def learn_czech_verbs(data):
    keys = {"infinitiv", "já", "ty", "on/ona/ono", "my", "vy", "oni/ony/ona"} 
    verbs = data['verbs']
    while(1):
        english_verb, czech_verbs = (random.choice(list(verbs.items())))
        key = random.choice(list(keys))
        input(english_verb + ", " + key + ": ")
        print(czech_verbs[key])

def learn_czech(filename):
    file_object = open(filename)
    parsed_json = json.load(file_object)
    print("What would you like to learn?")
    for i in parsed_json:
        print(i + "? y/n: ")
#        choice = input().lower()
        choice = 'y'
        if (choice == 'y'):
            if (i == 'verbs'):
                learn_czech_verbs(parsed_json)
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
