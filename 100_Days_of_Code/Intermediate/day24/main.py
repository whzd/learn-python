#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
def _load_file(filepath):
    with open(filepath, mode="r") as file:
        return file.read()


def _save_letter(filepath, letter, person):
    with open(f"{filepath}/letter_for_{person}.txt", mode="w") as file:
        file.write(letter)


def get_invited_guests():
    names = _load_file("./Input/Names/invited_names.txt")
    return names.split("\n")


def create_letter(person):
    letter_base = _load_file("./Input/Letters/starting_letter.txt")
    letter = letter_base.replace("[name]", person)
    _save_letter("./Output/ReadyToSend", letter, person)


def run():
    people = get_invited_guests()
    for person in people:
        create_letter(person)


if __name__ == "__main__":
    run()
