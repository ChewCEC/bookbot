foo = open("books/frankenstein.txt","r").read()
# print(foo)
VALID = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def count_letters (txt: str) -> dict:
    letter_list = {}
    for letter in txt:
        letter = letter.lower()
        if letter in VALID:
            if (letter not in letter_list):
                letter_list[letter] = 1
            else:
                letter_list[letter] += 1
    return letter_list

def create_report(dic: dict) -> str:
    repo = ""
    for key,val in dic.items():
        repo+=f"The {key} character was found {val} times\n"
        
    return repo.rstrip()

print(create_report(count_letters(foo)))