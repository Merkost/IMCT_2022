"""
Groupby group

Условие:
Необходимо написать программу, которая группирует студентов по их группам. Формат входного файла В первой
строке входного файла дано число n — количество студентов. Далее следует n строк, в каждой из которых записаны
группа и имя студента. Группа и имя студента разделены символом табуляции. Формат выходного файла Выходной файл
должен содержать список студентов, сгруппированный по группам. Для каждой группы необходимо вывести имя группы,
а затем все имена студентов, которые принадлежат этой группе в алфавитном порядке, каждое в новой строке. Сами
группы следуют также в алфавитном порядке.
"""

dict = {}

with open("input.txt", "r") as file:
    count = int(file.readline())
    for i in range(count):
        line = file.readline().split("\t")
        existedList = dict.get(line[0])
        if existedList is None:
            existedList = []
        existedList.insert(0, line[1].rstrip())
        dict[line[0]] = existedList

with open("output.txt", "w") as f:
    for i in dict.keys():
        if i != list(dict.keys())[0]: f.write('\n')
        f.write(f"{i}\n")
        f.writelines("\n".join(dict.get(i)))

print(dict)
