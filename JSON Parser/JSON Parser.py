import os
import re

def isValidJSON(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
        if (text.count("{") == text.count("}")) and len(text) > 0:
            return True
        else:
            return False
        

def step1():
    for root, dirs, files in os.walk("."):
        if root == ".\\tests\\step1":
            for filename in files:
                filepath = root + "\\" + filename
                if isValidJSON(filepath):
                    print(filename + " is a valid JSON Object")
                else:
                    print(filename + " is not a valid JSON Object")

def parseJSON(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
        items = []
        word = ""
        split = text.split(":")
        for item in split:
            for entry in item.split(","):
                for c in entry:    
                    if not c.isalnum():
                        if word == "":
                            word = entry.replace(c, "")
                        else:
                            word = word.replace(c, "")
                if word:
                    items.append(word)
                word = ""
        return items

def step2():
    for root, dirs, files in os.walk("."):
        if root == ".\\tests\\step2":
            for filename in files:
                filepath = root + "\\" + filename
                print("ITEMS ARE " + str(parseJSON(filepath)))

#I wrote parseJSON in a way that it ended up working for step 3 as well :D
def step3():
    for root, dirs, files in os.walk("."):
        if root == ".\\tests\\step3":
            for filename in files:
                filepath = root + "\\" + filename
                print("ITEMS ARE " + str(parseJSON(filepath)))

def parseJSONstep4(filepath):
    allowed = set("{", "}", "[", "]")
    with open(filepath, 'r') as f:
        text = f.read()
        items = []
        word = ""
        split = text.split(":")
        for item in split:
            for entry in item.split(","):
                for c in entry:    
                    if not c.isalnum() and c not in allowed:
                        if word == "":
                            word = entry.replace(c, "")
                        else:
                            word = word.replace(c, "")
                if word:
                    items.append(word)
                word = ""
        return items

def step4():
    for root, dirs, files in os.walk("."):
        if root == ".\\tests\\step4":
            for filename in files:
                filepath = root + "\\" + filename
                print("ITEMS ARE " + str(parseJSON(filepath)))

step1()