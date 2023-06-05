# 1. Пользователь вводит с клавиатуры номер дня недели (1-7).
# Необходимо вывести на экран названия дня недели.
# Например, если 1, то на экране надпись понедельник, 2 — вторник и т.д.

try:
    user_select = int(input("Enter the number of the day of the week here:"))

    if user_select == 1:
        print("Monday")
    elif user_select == 2:
        print("Tuesday")
    elif user_select == 3:
        print("Wednesday")
    elif user_select == 4:
        print("Thursday")
    elif user_select == 5:
        print("Friday")
    elif user_select == 6:
        print("Saturday")
    elif user_select == 7:
        print("Sunday")
    else:
        print("Incorrect numer")

except Exception as error:
    print(f"Exception occurred: {error}")

# except BaseException as error:
#     print(f"Exception occurred: {error}")




# 2. Пользователь вводит два числа. Определить, равны ли эти числа и если нет, вывести их на экран в порядке возрастания






# 3. Пользователь вводит два числа и матем действие: + - * или /
# В зависимости от введенного матем действия вывести результат
