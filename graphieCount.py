str_ipt = None
while(str_ipt != "stop"):
    count = 0
    str_ipt = input("Entrez votre texte (stop pour fermer) ~ ")
    mots = str_ipt.split(" ")
    count = count+len(mots)
    lettres_str = []
    for characters in str_ipt:
        lettres_str.append(characters)
    calig =[".","?","!","...",";",":",",","(","[",'"',"/","{"]
    for lettre in lettres_str:
        if(lettre == "'"):
            count = count + 1
        if(lettre in calig):
            count = count + 1
    print("Votre texte comporte {} graphies".format(count))
