import os

data_file = 'phonebook.txt'


def load_data():
    """Загрузка данных из файла в список записей."""
    if os.path.exists(data_file):
        with open(data_file, 'r') as f:
            lines = f.readlines()
            return [line.strip().split(',') for line in lines]


def save_data(entries):
    """Сохронение списка записей в файл."""
    with open(data_file, 'w') as f:
        for entry in entries:
            f.write(', '.join(entry) + '\n')


def display_entries(entries, page_size, page_number):
    """Вывод постранично записей на экран"""

    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size

    if entries:
        for index, entry in enumerate(entries[start_index:end_index], start=1):
            print(f'{index}', ','.join(entry))
    else:
        print('Записей нет, спрева добавте их.')


def search_entries(entries):
    """Поиск записей по одной или нескольким характеристикам."""
    search_term = input('Введите данные строки, для поиска: ')
    results = []

    for entry in entries:
        if any(search_term.lower() in e.lower() for e in entry):
            results.append(entry)

    if results:
        print('Резильтат поиска:')
        for index, result in enumerate(results, start=1):
            print(f'{index}. ', ', '.join(result))
    else:
        print('Ничего не найдено.')


def add_entry(entries):
    """Добовление новой записи в справочник."""
    print('\nДобавление новой записи:')
    personal_data = ['Фамилия', 'Имя', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон']
    new_entry = []

    for data in personal_data:
        entry = input(f'{data}: ')
        while entry == '':
            print('Заполните эту часть.')
            entry = input(f'{data}: ')

        new_entry.append(entry.strip())

    entries.append(new_entry)

    print('\nЗапись добавлена.\n')


def edit_entry(entries):
    """Редоктирование записи в справочнике"""
    print('Редоктриование записи:')

    display_entries(entries, len(entries), 1)
    entry_index = int(input('Введите номер записи которую хотите изменить: ')) - 1
    edit_data = ['Фамилия', 'Имя', 'Отчество', 'Организация', 'Рабочий телефон', 'Личный телефон']
    new_entry_data = []

    if 0 <= entry_index < len(entries):
        for data in edit_data:
            entry = input(f'{data}: ')
            new_entry_data.append(entry)

        entries[entry_index] = new_entry_data
        print("Запись обновлена.")

    else:
        print('Не верный номер записи.')


def main():
    entries = load_data()
    page_size = 5
    menu = """
        Меню:
        1. Вывести записи
        2. Добавить запись
        3. Редактировать запись
        4. Поиск записей
        5. Выйти
        
    """
    while True:
        print(menu)
        choice = input('Выберите опцию: ')

        if choice == '1':
            page_number = int(input('Введите номер страницы: '))
            display_entries(entries, page_size, page_number)

        elif choice == '2':
            add_entry(entries)

        elif choice == '3':
            edit_entry(entries)

        elif choice == '4':
            search_entries(entries)

        elif choice == '5':
            save_data(entries)
            break

        else:
            print('Не верный выбор, выберите снова')

        save_data(entries)


if __name__ == '__main__':
    main()
