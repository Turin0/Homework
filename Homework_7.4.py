import os
import time

count = 0
directory = 'G:\\PythonProjectUrbanUniversity\\Homework_M7'
for root, dirs, files in os.walk(directory):
    for file in files:
        filePath = os.path.join(root, file)
        fileTime = os.path.getmtime(filePath)
        formattedTime = time.strftime("%d.%m.%Y %H:%M", time.localtime(fileTime))
        fileSize = os.path.getsize(filePath)
        parentDir = os.path.dirname(filePath)
        print(f'Обнаружен файл: {file}, Путь: {filePath}, Размер: {fileSize} байт, Время изменения: {formattedTime},'
              f'Родительская директория: {parentDir}')

