import csv
import requests
from unidecode import unidecode

# Получаем данные из API для учителей
api_url_teacher = 'https://bilimge.kz/admins/api/teacher/?school=kaz15'
response_teacher = requests.get(api_url_teacher)
api_data_teacher = response_teacher.json()

# Открываем исходный CSV файл для чтения и новый CSV файл для записи изменений
with open('modified_file.csv', newline='', encoding='utf-8') as csvfile, \
        open('zzz.csv', 'w', newline='', encoding='utf-8') as modified_csvfile:

    reader = csv.reader(csvfile)
    writer = csv.writer(modified_csvfile)

    # Проходимся по строкам и изменяем значения только для строк, где school_id равен 31
    for row in reader:
        # Проверяем, что строка содержит достаточное количество полей
        if len(row) < 7:
            writer.writerow(row)
            continue

        # Проверяем, что поле с фамилией учителя не пустое и не равно запятой
        if row[6].strip() == '' or row[6].strip() == ',':
            writer.writerow(row)
            continue

        if row[0] == '31':  # Если это строка с school_id равным 31
            row_teacher_name = row[6]  # Фамилия учителя находится в седьмом столбце
            row_teacher_name_normalized = unidecode(row_teacher_name.split()[0]).lower()  # Нормализуем фамилию
            for teacher in api_data_teacher:
                api_teacher_name_normalized = unidecode(teacher['full_name'].split()[0]).lower()  # Нормализуем фамилию из API
                if row_teacher_name_normalized == api_teacher_name_normalized:
                    row[4] = str(teacher['id'])  # Заменяем фамилию на id учителя из API
                    break

        writer.writerow(row)

print("Изменения были записаны в файл 'zzz.csv'.")
