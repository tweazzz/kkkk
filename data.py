import csv

# Открываем CSV файл для чтения и временный файл для записи изменений
with open('zzz.csv', newline='', encoding='utf-8') as csvfile, \
        open('modified_file.csv', 'w', newline='', encoding='utf-8') as modifiedcsvfile:

    reader = csv.reader(csvfile)
    writer = csv.writer(modifiedcsvfile)

    # Проходимся по строкам и добавляем ":00" ко всем значениям в третьем столбце
    for row in reader:
        row[2] += ":00"  # Добавляем ":00" к третьему столбцу
        writer.writerow(row)

print("К третьему столбцу было добавлено ':00' во всех строках. Результат записан в файл 'modified_file.csv'.")
