"""
Имена файлов

Условие
I wish we had some way to handle it sanely, but I don't think a sane solution to case-insensitivity exists.
Linus Torvalds

На компьютере под управлением операционной системы Linux имеется каталог, содержащий N файлов. Пользователю
требуется скопировать эти файлы на компьютер, работающий под управлением ОС Windows. К сожалению, файловая система
Windows имеет странное свойство. Несмотря на то, что она сохраняет большие и малые буквы в именах файлов, имена,
отличающиеся только регистром букв, считаются одинаковыми. Например, файлы с именами ChangeLog, CHANGELOG и
changelog при копировании на файловую систему Windows попадут в один и тот же файл.
Чтобы избежать потери данных, предлагается при копировании переименовывать файлы по следующим правилам:
Файлы копируются в порядке перечисления в исходном каталоге. Имена файлов считаются одинаковыми, если они совпадают
с точностью до регистра. Если при копировании очередного файла выяснилось, что файл с таким именем уже был
скопирован, то к имени текущего файла добавляется суффикс "1". Если имя, полученное после присоединения суффикса,
также уже встречалось, то перебираются суффиксы "2", "3", ..., "10", "11", ... до тех пор, пока не найдётся
суффикс, дающий уникальное имя. Формат входного файла Входной файл содержит количество имён N , за которым следует
N строк с именами. Имена состоят из латинских букв и цифр и имеют длину от 1 до M символов.
Формат выходного файла Выходной файл должен содержать N строк с модифицированными именами файлов.
"""

# dic = {}
# result = []
# resultLc = []


# with open("input.txt", "r") as file:
#     count = int(file.readline())
#
#     for i in range(count):
#         inputLine = file.readline().strip()
#         inputLower = inputLine.lower()
#         value = dic.get(inputLower)
#         if value is None:
#             if inputLower in resultLc:
#
#                 name = getCleanName(inputLine, 1)
#                 nameLower = name.lower()
#
#                 result.append(name)
#                 resultLc.append(nameLower)
#                 dic[inputLower] = [name]
#             else:
#                 result.append(inputLine)
#                 resultLc.append(inputLower)
#                 dic[inputLower] = [inputLine]
#         else:
#             l = len(value)
#             name = getCleanName(inputLine, l)
#             nameLower = name.lower()
#
#             result.append(name)
#             resultLc.append(nameLower)
#             value.append(inputLine)
#             dic[inputLower] = value
#
# with open("output.txt", "w") as f:
#     f.write("\n".join(result))


dic = {}
result = []
resultLc = []


def getNewName(initialLower, iteration):
    newNameLower = initialLower + str(iteration)
    while newNameLower in resultLc:
        iteration += 1
        newNameLower = initialLower + str(iteration)
    return newNameLower, iteration


def addNewName(inputLower, name, nameLower, namesToDic):
    result.append(name)
    resultLc.append(nameLower)
    dic[inputLower] = namesToDic


with open("input.txt", "r") as file:
    count = int(file.readline())
    for i in range(count):
        input = file.readline().strip()
        inputLower = input.lower()
        value = dic.get(inputLower)
        if value is None:
            if inputLower in resultLc:

                nameLower, iterat = getNewName(inputLower, 1)
                name = input + str(iterat)

                addNewName(inputLower, name, nameLower, [name])
            else:
                addNewName(inputLower, input, inputLower, [input])
        else:
            nameLower, iterat = getNewName(inputLower, len(value))
            name = input + str(iterat)

            value.append(input)
            addNewName(inputLower, name, nameLower, value)

with open("output.txt", "w") as f:
    f.write("\n".join(result))
