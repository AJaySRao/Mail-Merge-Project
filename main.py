#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as document:
    data = document.readlines()

with open("./Input/Letters/starting_letter.txt") as document:
    placeholder = document.read()
#Replace the [name] placeholder with the actual name.
for n in data:
    name = n.strip()
    letter = placeholder.replace('[name]', name)

#Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/A_letter_for_{name}.txt", mode='w') as document:
        document.write(letter)

