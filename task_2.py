def get_cats_info(path):
    # Створуєму пустий список для зберігання інформації про котів  
    info = []

    try:
        # Відкриваємо файл для читання
        with open(path, 'r', encoding='utf-8') as file:
            # Зчитуємо усі ряди з файлу
            lines = file.readlines()

            # Ітерація по рядках
            for line in lines:
                # Створюємо пустий словник для кожного кота
                cat = dict()
                # Розбиваємо рядок
                id, name, age = line.strip().split(',')
                
                # Додаємо інформацію в словник
                cat['id'] = id
                cat['name'] = name
                cat['age'] = age
                
                # Додаємо словник до списку
                info.append(cat)
            
            return info
        
    except Exception as e:
        # Обробка винятків та виведення повідомлення про помилку
        print(f"Помилка при обробці файлу: {e}")
        return []
    
cats_info_1 = get_cats_info('sats.txt')
cats_info_2 = get_cats_info('Data\\Cats.txt')
for i in cats_info_2:
    print(i)