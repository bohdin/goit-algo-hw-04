
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    # Перевіряємо, щоб після add йшов список з ім'ям та телефоном
    if len(args) != 2:
        return "Invalid contact"

    # Розбиваємо список
    name, phone = args
    # Робим щоб імена починалися з великої літери
    name = name.capitalize()
    # Якщо такою людини ще немає в словнику додаємо
    if name not in  contacts.keys():
        
        contacts[name] = phone
        return "Contact added."
    else:
        return "Contact already exists." # В іншому випадку виводимо, що вже контакт існує


def change_contact(args, contacts):
    # Перевіряємо, щоб після change йшов список з ім'ям та телефоном
    if len(args) != 2:
        return "Invalid contact"
    
    #  Розбиваємо список
    name, phone = args
    # Робим щоб імена починалися з великої літери
    name = name.capitalize()
    # Перевіряємо чи є людина в словнику
    if name in  contacts.keys():
        contacts[name] = phone
        return "Contact change."
    else:
        return "Contact doesn`t exists." # В іншому випадку виводимо, що контакт не існує

def show_phone(args, contacts):
    # Перевіряємо, щоб після phone йшло тільки ім'я
    if len(args) != 1:
        return "Invalid contact"
    
    # Приводимо ім'я до потрібної нам форми
    name = args[0].capitalize()
    #  Перевіряємо чи є людина в словнику
    if name in contacts.keys():
        return contacts[name]
    else:
        return "Contact doesn`t exists." # В іншому випадку виводимо, що контакт не існує
    


def show_all(contacts):
    # Якщо словник не пустий, виводимо контакти через enter
    if contacts:
        return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts."
        

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        
        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
             print(show_all(contacts))

        else:
            print("Invalid command.")




if __name__ == "__main__":
    main()
