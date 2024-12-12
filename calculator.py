''' 
Aufgabe:
Rechnen mit match case
setze ein match case ein
'''


''' 
zahl1 - eine Zahl
zahl2 - eine Zahl
operator - ein Operator (+,-,*,/)  -> optional %
return - Ergibnis der Berechnung
'''
def calc(zahl1,zahl2,operator):
    #pass      ## pass -> Funktion macht noch nichts
    match operator:
        case '+':
            return zahl1 + zahl2
        case '-':
            return zahl1 - zahl2
        case '*':
            return zahl1 * zahl2
        case '/':
            if zahl2==0:
                return 'Fehler: ivision durch 0 ist nicht erlaubt!'
            return zahl1 / zahl2
        case _:
            return 'Ungültiger Operator!'







#result = calc(10,0,'/')
#print(result)# 50