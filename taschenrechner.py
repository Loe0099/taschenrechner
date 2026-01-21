while True:
	eingabe = input("Gib die erste Zahl der Berechnung ein! ")

	if eingabe.lower() == "beenden":
		print("Das Programm wurde erfolgreich verlassen!")
		exit()

	try:
		zahl1 = float(eingabe)
		break
	except ValueError:
		print("Deine erste Eingabe ist keine Zahl! Mache bitte eine neue Angabe!")
		print("Wenn du das Programm verlassen möchtest, gebe einfach 'Beenden' ein.")
while True:
	eingabe = input("Gib die erste Zahl der Berechnung ein! ")

	if eingabe.lower() == "beenden":
		print("Das Programm wurde erfolgreich verlassen!")
		exit()

	try:
		zahl2 = float(eingabe)
		break
	except ValueError:
		print("Deine zweite Eingabe ist keine Zahl! Mache bitte eine neue Angabe!")
		print("Wenn du das Programm verlassen möchtest, gebe einfach 'Beenden' ein.")
while True:
	rechenzeichen = str(input("Gib das Rechenzeichen ein (+ - * /) : "))
	if rechenzeichen in ("+","-","*","/"):
		break
	elif rechenzeichen.lower() == "beenden":
		print("Das Programm wurde erfolgreich verlassen!")
		exit()
	else:
		print("Deine Eingabe wurde nicht als Rechenzeichen identifiziert. Mache bitte eine neue Angabe!")
		print("Wenn du das Programm verlassen möchtest, gebe einfach 'Beenden' ein.")

if zahl1 == int(zahl1) and zahl2 == int(zahl2):
	zahl1 = int(zahl1)
	zahl2 = int(zahl2)

if rechenzeichen == "+":
	ergebnis = zahl1 + zahl2
if rechenzeichen == "-":
	ergebnis = zahl1 - zahl2
if rechenzeichen == "*":
	ergebnis = zahl1 * zahl2
if rechenzeichen == "/":
	ergebnis = zahl1 / zahl2

print("Das Ergebnis der Berechnung", zahl1, rechenzeichen, zahl2, "=", ergebnis)