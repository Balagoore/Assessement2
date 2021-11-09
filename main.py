#Создайте класс `Text`, описывающий константный (неизменяемый) многострочный текстовый блок. Храните строки текста в
#списке. Что должен уметь делать класс:

#- Создать текстовый блок по одной строке (возможно, с символами перевода строки);
#- Получить количество строк в блоке;
#- Получить строку по номеру;
#- Получить количество слов заданной строки;
#- Получить слово по его номеру из заданной строки.

#На его основе создайте класс `EditableText`, который позволяет изменять имеющийся текст. Функционал класса
#- Заменить строку п её номеру;
#- Заменить слово по его номеру в заданной строке;
#- Найти позицию слова во всём тексте;
#- Получить весь текстовый блок одной строкой.


class Text:
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return f' is {self.text} '

    def countlines(self):
        self.text = open(self)
        self.text_gen = _make_gen(text.countlines())
        return sum(text.count(b'\n') for buf in self.text_gen)
    def textsplit(self):
        textsplit = text.split('\n', n)[m]

        print
    def __len__(self):
        r = len(self.text.split())
        print(self.text(r))
    def stringfind(self):
        print(string find for index)

class EditableText(Text):