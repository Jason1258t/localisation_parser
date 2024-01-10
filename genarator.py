from config import *


class ARBGenerator:
    def __init__(self, lang: Language, sheet):
        self.lang = lang
        self.sheet = sheet

    def generate_lines(self) -> list[str]:
        lines = ['{\n']

        for i in range(1, LIST_LENGTH + 1):
            new_line = self.__build_line__(i, self.lang)
            lines.append(new_line)

        lines.append('\n}')

        return lines

    @staticmethod
    def __clean_specialize_symbols__(string: str) -> str:
        index1 = string.rfind('"')
        if index1 != -1:
            string = string[:index1]
        index2 = string.rfind('"')
        if index2 != -1:
            string = string[index2 + 1:]

        string = string.replace(r'\ n', r'\n')
        string = string.replace(r'\ N', r'\n')
        string = string.replace(r'\ ', r'')

        return string.strip()

    def __build_line__(self, index: int, language: Language) -> str:
        var_name = self.sheet.cell(row=index, column=VARIABLE_NAMES_COLUMN).value
        phrase: str = self.sheet.cell(row=index, column=language.column).value
        if language.two_letter_code != 'ru':
            phrase = self.__clean_specialize_symbols__(phrase)

        # print(f'"{convertToDartFormatName(names)}": "{phrase}",')
        line = f'"{var_name}": "{phrase}",\n'
        if index == LIST_LENGTH:
            line = line[:-2]

        return line
