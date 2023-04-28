import os

notes = []
sair = False
while not sair:
    resp = input ('Fazer anotação ? (s/n)' )
    if resp.lower() == "s":
        text = input("Anotação: ")
        notes.append(text)
    print('\n'+"Anotações".center(30, "="))
    #layout do post-it
    for note in notes:
        text_size = len(note)
        note_size = text_size+6
        print('-'*note_size)
        print(note.center(note_size))
        print("-"*note_size)
    r =input ("Sair? (s/n)")
    if r.lower() == "s":
        sair = True
    os.system('cls' if os.name == "nt" else 'clear')