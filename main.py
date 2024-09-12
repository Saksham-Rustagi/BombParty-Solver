import time

import keyboard
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

full_words = set()
letters = [1 for i in range(26)]
letters[25] = 0
letters[23] = 0

def getDictionary(dictionary_file):
    with open (dictionary_file) as f:
        for word in f:
            full_words.add(word.strip())
    with open("enable.txt") as f:
        for word in f:
            if not word in full_words:
                full_words.add(word.strip().upper())
    with open("moby.txt") as f:
        for word in f:
            if not word in full_words:
                full_words.add(word.strip().upper())
    print("dictionary got")

def find_words(con):
    found_words = set()
    for word in full_words:
        if con in word:
            found_words.add(word)
    return found_words

def sorts(found):
    maxPoints = 0
    for e in found:
        break
    bestWord = e
    for word in found:
        temp = 0
        for c in word:
            if letters[ord(c)-ord('A')] == 1:
                temp += 1
        if temp > maxPoints:
            maxPoints = temp
            bestWord = word
        #elif temp == maxPoints and len(word) < len(bestWord):
        #    bestWord = temp

    for c in bestWord:
        letters[ord(c)-ord('A')] = 0

    test = False
    for x in letters:
        if x == 1:
            test = True
    if not test:
        for x in range(26):
            letters[x] = 1
        letters[25] = 0
        letters[23] = 0

    return bestWord

def short_sort(found):
    short_word = "AAAAAAAAAAAAAAAAAAAA"
    for word in found:
        if len(word) < len(short_word):
            short_word = word

    full_words.remove(short_word)
    return short_word

def long_sort(found):
    short_word = ""
    for word in found:
        if len(word) > len(short_word):
            short_word = word

    full_words.remove(short_word)
    return short_word

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    getDictionary("dict.txt")
    while True:
        ans = input("What letters to contain")
        found = find_words(ans.upper())
        best = sorts(found)
        print(best)
        keyboard.press('alt')
        keyboard.press('tab')
        time.sleep(0.1)
        keyboard.release('alt')
        keyboard.release('tab')
        time.sleep(0.1)
        keyboard.write(best.lower(), 0.1)
        keyboard.press_and_release('enter')
        time.sleep(0.1)
        keyboard.press('alt')
        keyboard.press('tab')
        time.sleep(0.1)
        keyboard.release('alt')
        keyboard.release('tab')




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
