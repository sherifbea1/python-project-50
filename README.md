# gendiff

### Hexlet tests and linter status:
[![Actions Status](https://github.com/sherifbea1/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/sherifbea1/python-project-50/actions)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=sherifbea1_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=sherifbea1_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=sherifbea1_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=sherifbea1_python-project-50)

## Описание
**gendiff** — CLI-инструмент для поиска различий в конфигурационных файлах.  
Поддерживаются форматы **JSON** и **YAML**, сравнение работает рекурсивно.  
Вывод доступен в форматах: stylish (по умолчанию), plain, json.  

## Установка
Клонируйте репозиторий и установите зависимости командой `make install`.  
Также можно установить через `uv sync`.  

## Использование
Запуск осуществляется через команду:  
`gendiff [-h] [-f FORMAT] first_file second_file`  

### Опции
- `-h, --help` — показать справку  
- `-f, --format` — задать формат вывода (stylish, plain, json)  

## Примеры работы

### Шаг 4. Сравнение плоских JSON
[![asciinema demo step 4](https://asciinema.org/a/8AhRdwRYB0uPIS9dqaEEoa12o)]

### Шаг 6. Поддержка YAML
[![asciinema demo step 6](https://asciinema.org/a/GSiQ1ww7T9pK7axLJ6vQt3LJQ)]

### Шаг 7. Рекурсивное сравнение
[![asciinema demo step 7](https://asciinema.org/a/QUhMEot87SCeOtfZ1PmL1q9HZ)]

### Шаг 8. Вывод в формате plain
[![asciinema demo step 8](https://asciinema.org/a/baY4ViV5iHjtTFgEYOqL2Lhl7)]

### Шаг 9. Вывод в формате JSON
[![asciinema demo step 9](https://asciinema.org/a/N1KmTBDwOx03mCtQKlw9wv33Z)]
