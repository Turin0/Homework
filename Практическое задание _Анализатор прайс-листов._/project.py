import csv
import os
import re
from tabulate import tabulate
from typing import List


def export_to_html(results: List[List], headers: List[str], filename: str) -> None:
    """
    Экспортирует результаты поиска в HTML файл.
    results (list): Список результатов поиска.
    headers (list): Заголовки таблицы.
    filename (str): Имя файла для сохранения результатов.
    """
    numbered_results = [[i + 1] + result for i, result in enumerate(results)]
    table = tabulate(numbered_results, headers=headers, tablefmt='html')
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(table)


def display_results(results: List[List], headers: List[str]) -> None:
    """
    Отображает результаты поиска в удобном формате.
    results (list): Список результатов поиска.
    headers (list): Заголовки таблицы.
    """
    numbered_results = [[i + 1] + result for i, result in enumerate(results)]
    print(tabulate(numbered_results, headers=headers, tablefmt='grid'))


class PriceMachine:
    HEADERS = ['№', 'Наименование', 'цена', 'вес', 'цена за кг.']
    
    def __init__(self):
        self.data = []
        self.result = ''
        self.name_length = 0

    def load_prices(self, directory: str) -> None:
        """
        Загружает ценовые данные из указанной директории.
        directory (str): Путь к директории с файлами ценовых данных.
        """
        self.data = []
        for filename in os.listdir(directory):
            if filename.endswith('.csv') and 'price' in filename.lower():
                self._load_file(os.path.join(directory, filename))

    def _load_file(self, filepath: str) -> None:
        """
        Загружает данные из файла CSV.
        filepath (str): Путь к файлу CSV.
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self._process_row(filepath, row)
        except (IOError, csv.Error) as e:
            print(f"Ошибка при чтении файла {filepath}: {e}")

    def _process_row(self, filename: str, row: dict) -> None:
        """
        Обрабатывает строку из CSV файла и добавляет ее в данные.
        filename (str): Имя файла.
        row (dict): Строка из CSV файла.
        """
        try:
            product_name = self._extract_value(row, r'(название|продукт|товар|наименование)')
            price = float(self._extract_value(row, r'(цена|розница)').replace(',', '.'))
            weight = float(self._extract_value(row, r'(фасовка|масса|вес)').replace(',', '.'))
            self.data.append([product_name, price, weight, round(price / weight, 2)])
        except (TypeError, ValueError) as e:
            print(f"Ошибка при обработке строки {row}: {e}")

    def _extract_value(self, row: dict, pattern: str) -> str:
        """
        Извлекает значение из строки на основе регулярного выражения.
        row (dict): Строка из CSV файла.
        pattern (str): Регулярное выражение для поиска значения.
        Возвращает:
        str: Найденное значение.
        """
        for column_name, value in row.items():
            if re.search(pattern, column_name, re.IGNORECASE):
                return value.strip()
        return ""

    def search_items(self, query: str) -> List[List]:
        """
        Ищет элементы по запросу.
        query (str): Строка для поиска.
        Возвращает:
        list: Список найденных элементов.
        """
        results = [row for row in self.data if re.search(query, row[0], re.IGNORECASE)]
        return sorted(results, key=lambda x: x[3])

    def main(self, directory: str) -> None:
        """
        Основной метод для работы с PriceMachine.
        directory (str): Путь к директории с файлами ценовых данных.
        """
        self.load_prices(directory)
        while True:
            query = input("Введите текст для поиска (или 'exit' для завершения): ")
            if query.lower() in ['exit',]:
                print("Работа завершена.")
                break
            self.find_text(query)

    def find_text(self, query: str) -> None:
        """
        Находит и отображает текст.
        query (str): Строка для поиска.

        """
        results = self.search_items(query)
        display_results(results, self.HEADERS)
        html_filename = 'output.html'
        export_to_html(results, self.HEADERS, html_filename)
        print(f"Результаты поиска сохранены в файле: {html_filename}")


if __name__ == "__main__":
    pm = PriceMachine()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    pm.main(current_directory)
