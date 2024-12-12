import calculator

print(__name__)


'''  
Benutzereingabe (input)
- erste Zahl: 4
- Operator: +
- zweite Zahl: 2
Ergebnis:6 
-weiter (y/n?)

Optional:
    Eingabe prüfen: z.B. mit try/except
'''
def main():
    print("Willkommen zum einfachen Taschenrechner!")
    while True:
        try:
            print("\nNeue Berechnung:")
            zahl1 = float(input("Gib die erste Zahl ein: "))
            operator = input("Gib den Operator ein (+, -, *, /, %): ")
            zahl2 = float(input("Gib die zweite Zahl ein: "))
            
            ergebnis = calculator.calc(zahl1, zahl2, operator)
            print(f"Ergebnis: {ergebnis}")
        except ValueError:
            print("Fehler: Bitte gib eine gültige Zahl ein!")
        except ZeroDivisionError:
            print("Fehler: Division durch Null ist nicht erlaubt!")

        # Frage den Benutzer, ob er eine weitere Berechnung durchführen möchte
        weiter = input("\nMöchtest du eine weitere Berechnung durchführen? (y/n): ").strip().lower()
        if weiter != 'y':
            print("Vielen Dank für die Nutzung des Taschenrechners. Auf Wiedersehen!")
            break


# Programmstart
# Prüfen ob main in dieser Datei aufgerufen wird
if __name__=='__main__': 
    main()