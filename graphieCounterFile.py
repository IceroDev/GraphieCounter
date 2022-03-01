str_ipt = None
filename = None
calig =[".","?","!","...",";",":",",","(","[",'"',"/","{","'"]

def setFile():
    global filename
    filename = input("Entrez votre fichier texte (.txt) (stop pour fermer) ~ ")
    return filename
while(setFile() != 'stop'):
    count = 0
    str_ipt = open(filename,"r", encoding="utf-8").readlines()
    file = "".join(str_ipt).replace("\n", " ")
    mots = file.split(" ")
    count = count+len(mots)

    lettres_str = []

    for characters in file:
        lettres_str.append(characters)

    for lettre in lettres_str:
        if(lettre in calig):
            count = count + 1
    print("Votre texte comporte {} graphies".format(count))
