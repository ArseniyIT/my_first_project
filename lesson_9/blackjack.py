#
# import random
# logo = """
# .------.            _     _            _    _            _
# |A_  _ |.          | |   | |          | |  (_)          | |
# |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
# | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
# |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
# `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
#       |  \/ K|                            _/ |
#       `------'                           |__/
# """
#
# print(logo)
#
# is_game = "y"
# while is_game == "y":
#
#     cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
#     hand_player = [random.choice(cards)]
#     hand_computer = [random.choice(cards)]
#     score_player = 0
#     score_computer = 0
#     get_card = "y"
#     while get_card == "y":
#         hand_player.append(random.choice(cards))
#
#         # если туз и > 21
#         if sum(hand_player) > 21 and 11 in hand_player:
#             for i in range(0, len(hand_player)):
#                 if hand_player[i] == 11:
#                     hand_player[i] = 1
#
#         score_player = sum(hand_player)
#         print(f"Твoя рука: {hand_player}, Очков у тебя: {score_player}")
#         print("Первая карта диллера:", hand_computer[0])
#         if score_player > 21:
#             get_card = "n"
#         else:
#             get_card = input("y - зять карту, n - остановиться -->")
#
#         while sum(hand_computer) < 17:
#             hand_computer.append(random.choice(cards))
#
#             # если туз и > 21
#             if sum(hand_computer) > 21 and 11 in hand_computer:
#                 for i in range(0, len(hand_computer)):
#                     if hand_computer[i] == 11:
#                         hand_computer[i] = 1
#
#         score_computer = sum(hand_computer)
#         print('-'*12)
#         print(f"Твоя итоговая рука: {hand_player}, Очков: {score_player}")
#         print(f"Итоговая рука диллера: {hand_computer}, Очков: {score_computer}")
#
#         if score_computer > 21 and score_player > 21:
#             print("Перебор у обоих. Ничья")
#         elif score_player > 21:
#             print("Ты преебрал, проигрышь.")
#         elif score_computer > 21:
#             print("У диллера перебор, ты выиграл.")
#         elif score_player > score_computer:
#             print("Победа")
#         elif score_player < score_computer:
#             print("Проиграл.")
#         else:
#             print("Ничья")
#
#         is_game = input("Еще разочек? y - да, n - нет: ")