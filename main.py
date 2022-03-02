
#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as data:
    data = data.readlines()

names = []

for n in data:
    names.append(n.strip())
#print(names)

#Replace the [name] placeholder with the actual name.
for n in names:
    with open("./Input/Letters/starting_letter.txt") as data:
        placeholder = data.read()
        x = placeholder.replace('[name]', n)

#Save the letters in the folder "ReadyToSend".
    with open(f"./Output/ReadyToSend/letter_for_{n}.txt", mode='w') as data:
        data.write(x)
