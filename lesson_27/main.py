# first_lesson = input("введите время начало уроков: ")
# len_lesson = int(input("введите длительность уроков: "))
# break_lesson = int(input("введите длительсность перемены: "))
# lesson_count = int(input("введите кол-во уроков: "))
# hours, minutes = first_lesson.split(":")
# hours, minutes = int(hours), int(minutes)
# time = hours*60 + minutes
# for i in range(lesson_count+1):
#     print(f"{i+1} урок: ", end="")
#     print(f"{str(hours).rjust(2, '0')}:{str(minutes).rjust(2, '0')} - ", end="")
#     time +=  len_lesson
#     hours = time // 60
#     minutes = time % 60
#     print(f"{str(hours).rjust(2, '0')}:{str(minutes).rjust(2, '0')}")
# time += 10
# hours = time // 60
# minutes = time % 60


col_zomb = int(input("сколько зомби к началу расчета: "))
wozm_zaraz = int(input("сколько может заразить один зомби: "))
day = int(input("на который день делаем расчет: "))
print(f"1 день: {col_zomb}")
for i in range(2, day + 1):
    col_zomb = col_zomb * wozm_zaraz + col_zomb
    print(f"{i} день: {col_zomb}")