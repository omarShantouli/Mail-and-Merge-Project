base = []
with open("../input/Letters/starting_letter.txt") as file:
    base = file.read()

names = []
with open("../input/Names/invited_names.txt") as file:
    names = file.read()
for name in names.split('\n'):
    with open(f"../output/ReadyToSend/{name}", mode= "w") as file:
        x = base.replace("[name]", name)
        file.write(x)
