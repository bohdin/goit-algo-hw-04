def total_salary(path):
    try:
        # Відкриття файлу для читання
        with open(path, 'r', encoding='utf-8') as file:
            
            # Зчитування усіх рядків з файлу та ініціалізація sum для обрахунків
            lines = file.readlines()
            sum = 0
            
            # Ітерація по рядках
            for line in lines:
                # Розбивка рядка на ім'я та зарплату
                _, salary = line.strip().split(',')
                # Конвертація зарплати у int і додавання до суми
                salary = int(salary)
                sum += salary
            
            # Обчислення середньої зарплати
            average = sum // len(lines) 
            return sum, average
    except Exception as e:
        # Обробка винятків та виведення повідомлення про помилку
        print(f"Помилка при обробці файлу: {e}")
        return None, None

total, average = total_salary('calary.txt')
total, average = total_salary('Data\\Salary.txt')
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")