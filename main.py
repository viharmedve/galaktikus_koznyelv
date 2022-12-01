print("Galaktikus Köznyelv")
print("(A)bc, (F)ordító vagy (Q)uiz? ")
kerdes = input()
kerdes = kerdes.upper()
if kerdes == "A":
    print("ᔑ     ʖ     ᓵ     ↸     ᒷ     ⎓    ⊣     ⍑     ╎     ⋮     ꖌ      ꖎ     ᒲ     リ    𝙹     !¡    ᑑ     ∷     ᓭ     ℸ     ⚍     ⍊     ∴      ̇/     ||      ⨅ ")
    print("A     B     C     D     E     F     G     H     I     J     K     L     M     N     O     P     Q     R     S     T     U     V     W      X      Y      Z ")
if kerdes == "F":
    print("Gépeld be a fordítandó szöveget: ")
    szoveg = input("")
    szoveg = szoveg.upper()
    if "Á" in szoveg:
        szoveg = (szoveg.replace("Á", "A"))
    if "É" in szoveg:
        szoveg = (szoveg.replace("É", "E"))
    if "Ő" in szoveg:
        szoveg = (szoveg.replace("Ő", "O"))
    if "Ö" in szoveg:
        szoveg = (szoveg.replace("Ö", "O"))
    if "Ó" in szoveg:
        szoveg = (szoveg.replace("Ó", "O"))
    if "Ű" in szoveg:
        szoveg = (szoveg.replace("Ű", "U"))
    if "Ü" in szoveg:
        szoveg = (szoveg.replace("Ü", "U"))
    if "Ú" in szoveg:
        szoveg = (szoveg.replace("Ú", "U"))
    if "A" in szoveg:
        szoveg = (szoveg.replace("A", "ᔑ"))
    if "B" in szoveg:
        szoveg = (szoveg.replace("B", "ʖ"))
    if "C" in szoveg:
        szoveg = (szoveg.replace("C", "ᓵ"))
    if "D" in szoveg:
        szoveg = (szoveg.replace("D", "↸"))
    if "E" in szoveg:
        szoveg = (szoveg.replace("E", "ᒷ"))
    if "F" in szoveg:
        szoveg = (szoveg.replace("F", "⎓"))
    if "G" in szoveg:
        szoveg = (szoveg.replace("G", "⊣"))
    if "H" in szoveg:
        szoveg = (szoveg.replace("H", "⍑"))
    if "I" in szoveg:
        szoveg = (szoveg.replace("I", "╎"))
    if "J" in szoveg:
        szoveg = (szoveg.replace("J", "⋮"))
    if "K" in szoveg:
        szoveg = (szoveg.replace("K", "ꖌ"))
    if "L" in szoveg:
        szoveg = (szoveg.replace("L", "ꖎ"))
    if "M" in szoveg:
        szoveg = (szoveg.replace("M", "ᒲ"))
    if "N" in szoveg:
        szoveg = (szoveg.replace("N", "リ"))
    if "O" in szoveg:
        szoveg = (szoveg.replace("O", "𝙹"))
    if "P" in szoveg:
        szoveg = (szoveg.replace("P", "!¡"))
    if "Q" in szoveg:
        szoveg = (szoveg.replace("Q", "ᑑ"))
    if "R" in szoveg:
        szoveg = (szoveg.replace("R", "∷"))
    if "S" in szoveg:
        szoveg = (szoveg.replace("S", "ᓭ"))
    if "T" in szoveg:
        szoveg = (szoveg.replace("T", "ℸ"))
    if "U" in szoveg:
        szoveg = (szoveg.replace("U", "⚍"))
    if "V" in szoveg:
        szoveg = (szoveg.replace("V", "⍊"))
    if "W" in szoveg:
        szoveg = (szoveg.replace("W", "∴"))
    if "X" in szoveg:
        szoveg = (szoveg.replace("X", " ̇/"))
    if "Y" in szoveg:
        szoveg = (szoveg.replace("Y", "||"))
    if "Z" in szoveg:
        szoveg = (szoveg.replace("Z", "⨅"))
    print("A begépelt szöveg galaktikus köznyelven: ")
    print(szoveg)
if kerdes == "Q":
    print("Quiz: ")
    import random
    for x in range(1):
        randomszam = (random.randint(0, 25))
        #print(randomszam)
    galaktikussorszam = ["ᔑ", "ʖ", "ᓵ", "↸", "ᒷ", "⎓", "⊣", "⍑", "╎", "⋮", "ꖌ", "ꖎ", "ᒲ", "リ", "𝙹", "!¡", "ᑑ", "∷", "ᓭ", "ℸ", "⚍", "⍊", "∴", " ̇/", "||", "⨅"]
    abcsorszam = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    print(galaktikussorszam[randomszam])
    valasz = input("Melyik betű ez az angol ABC-ben? ")
    valasz = valasz.upper()
    if "A" in valasz:
        valasz = (valasz.replace("A", "0"))
    if "B" in valasz:
        valasz = (valasz.replace("B", "1"))
    if "C" in valasz:
        valasz = (valasz.replace("C", "2"))
    if "D" in valasz:
        valasz = (valasz.replace("D", "3"))
    if "E" in valasz:
        valasz = (valasz.replace("E", "4"))
    if "F" in valasz:
        valasz = (valasz.replace("F", "5"))
    if "G" in valasz:
        valasz = (valasz.replace("G", "6"))
    if "H" in valasz:
        valasz = (valasz.replace("H", "7"))
    if "I" in valasz:
        valasz = (valasz.replace("I", "8"))
    if "J" in valasz:
        valasz = (valasz.replace("J", "9"))
    if "K" in valasz:
        valasz = (valasz.replace("K", "10"))
    if "L" in valasz:
        valasz = (valasz.replace("L", "11"))
    if "M" in valasz:
        valasz = (valasz.replace("M", "12"))
    if "N" in valasz:
        valasz = (valasz.replace("N", "13"))
    if "O" in valasz:
        valasz = (valasz.replace("O", "14"))
    if "P" in valasz:
        valasz = (valasz.replace("P", "15"))
    if "Q" in valasz:
        valasz = (valasz.replace("Q", "16"))
    if "R" in valasz:
        valasz = (valasz.replace("R", "17"))
    if "S" in valasz:
        valasz = (valasz.replace("S", "18"))
    if "T" in valasz:
        valasz = (valasz.replace("T", "19"))
    if "U" in valasz:
        valasz = (valasz.replace("U", "20"))
    if "V" in valasz:
        valasz = (valasz.replace("V", "21"))
    if "W" in valasz:
        valasz = (valasz.replace("W", "22"))
    if "X" in valasz:
        valasz = (valasz.replace("X", " ̇23"))
    if "Y" in valasz:
        valasz = (valasz.replace("Y", "24"))
    if "Z" in valasz:
        valasz = (valasz.replace("Z", "25"))
    if int(valasz) == randomszam:
        print("Helyes válasz")
    else:
        print("Helytelen válasz")
        print("A helyes válasz: " + abcsorszam[randomszam])
