# import time
# import random
#
# print("Время проверить твою ловкость и скорость и понять, кто самый быстрый стрелок на западе! Когда увидишь 'СТРЕЛЯЙ', у тебя будет 0.3 секунды чтобы нажать Enter. Но если ты нажмёшь Enter раньше, то ты проиграл.")
#
# input("Нажми Enter что бы начать...")
# print("время пострелять")
# time.sleep(random.randint(1, 5)) # случайно ожидание
#
# start = time.time()
# input("бум бум тут нельзя взрываться")
# end = time.time()
# delta = end - start
# print(f"{delta} сек")
# if delta < 0.01: # фальштарт
#     print("фальштарт придурок")
#
# elif delta < 0.3:
#     print("ты топ")
# else:
#     print("ты бот")