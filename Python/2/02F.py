"""
Электронная почта

Условие:
В ДВФУ у каждого студента и сотрудника есть персональный адрес электронной почты в домене dvfu.ru.
Требуется написать программу, которая по заданным фамилии, имени и роли пользователя создает адрес его электронной
почты в формате [фамилия].[имя]@[роль].dvfu.ru
Формат входных данных: Входные данные содержат три слова в разных строках.
Формат выходных данных: Выходные данные должны содержать одну строку — электронный адрес в описанном формате.

"""
surname = input()
name = input()
role = input()

print(f"{surname}.{name}@{role}.dvfu.ru")
