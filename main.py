from openpyxl import load_workbook
from config import SHEET_NAME, LANGUAGES, OUTPUT_DIRECTORY
from genarator import ARBGenerator

# Крч суть какая, идешь в файл config.py и прописываешь нужные языки, колонки и так далее
# Потом здесь прописываешь название файла с таблицей и запускаешь
# Перед применением скорее всего надо pip install openpyxl

WB = load_workbook('../Локализация без функций (2).xlsx')

sheet = WB[SHEET_NAME]

for lang in LANGUAGES:
    generator = ARBGenerator(lang=lang, sheet=sheet)
    lang_lines = generator.generate_lines()

    text = ''.join(lang_lines)

    f = open(f'{OUTPUT_DIRECTORY}/app_{lang.two_letter_code}.arb', 'w', encoding='utf-8')
    f.write(text)
