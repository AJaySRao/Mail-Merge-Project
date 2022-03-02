
#for each name in invited_names.txt
with open("D:/python/Mail Merge Project Start/Input/Names/invited_names.txt") as data:
    data = data.readlines()

names = []

for n in data:
    names.append(n.strip())
#print(names)

#Replace the [name] placeholder with the actual name.
for n in names:
    with open("D:/python/Mail Merge Project Start/Input/Letters/starting_letter.txt") as data:
        placeholder = data.read()
        x = placeholder.replace('[name]', n)

#Save the letters in the folder "ReadyToSend".
    with open(f"D:/python/Mail Merge Project Start/Output/ReadyToSend/letter_for_{n}.txt", mode='w') as data:
        data.write(x)



    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp