import random    # random.shuffle(array)


def scoring(cards): # подсчёт очков в наборе карт
	result = 0
	for card in cards:
		if card in ["6", "7", "8", "9", "10"]:
			result += int(card)
		elif card == "J":
			result += 2
		elif card == "Q":
			result += 3
		elif card == "K":
			result += 4
		elif card == "A":
			result += 11
	return result


def main():
	cards = ["6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9",
			"10", "10", "10", "10", "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K",
			"A", "A", "A", "A"]
	random.shuffle(cards) # перемешиваем карты

	player_cards = []
	dealer_cards = []
	# сдаём по одной карте игроку и дилеру
	player_cards.append(cards[0])
	dealer_cards.append(cards[1])
	number = 2

	print("Если вы хотите получить ещё одну карту, введите ЕЩЁ. Если хотите остановиться, введите СТОП")
	print("Ваши карты:", end=' ')
	for card in player_cards:
		print(card, end=' ')
	print()
	score = scoring(player_cards)
	print("Ваши очки:", score)
		
	command = input().lower()
	while (command == "ещё") or (command == "еще"):
		player_cards.append(cards[number])
		number += 1
		print("Ваши карты:", end=' ')
		for card in player_cards:
			print(card, end=' ')
		print()
		score = scoring(player_cards)
		print("Ваши очки:", score)
		
		if score == 21:
			print()
			print("Поздравляем! Вы выиграли!")
			return
		elif score > 21:
			print()
			print("Упс... Вы проиграли:(")
			return
		command = input().lower()
	# дилер набирает карты себе:
	while scoring(dealer_cards) < 17:
		dealer_cards.append(cards[number])
		number += 1
	# вскрываемся:
	print("Ваши карты:", end=' ')
	for card in player_cards:
		print(card, end=' ')
	print()
	print("Ваши очки:", scoring(player_cards))
	
	print("Карты дилера:", end=' ')
	for card in dealer_cards:
		print(card, end=' ')
	print()
	print("Очки дилера:", scoring(dealer_cards))
	if (scoring(dealer_cards) < scoring(player_cards)) or (scoring(dealer_cards) > 21):
		print("Поздравляем! Вы выиграли!")
		return
	else:
		print("Упс... Вы проиграли:(")
		return
		
		

print("Привет! Это игра 21. Если вы не умеете играть в эту игру, введите команду Справка.")
print("Если вы хотите сыграть, введите команду Играть.")
print("Для выхода введите команду Выход.")
command = input().lower()
if command == "выход":
	print("До новых встреч!")
elif command == "справка":
	rules = open("rules_21.txt", "r")
	print(rules.read())
	rules.close()
	print("Если вы хотите сыграть, введите команду Играть.")
	print("Для выхода введите команду Выход.")
	command = input().lower()
while command == "играть":
	main()
	print()
	print("Если вы хотите сыграть ещё, то введите команду Играть")
	print("Если вы хотите выйти, то введите команду Выход")
	command = input().lower()
		
