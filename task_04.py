def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            return "Expect one argument"
        except ValueError:
            return "Expect two arguments"
        except KeyError:
            return "No such name in contacts"
    return inner

# мені не подобається цей декоратор, зробив щоб тут і зараз він працював для домашки
# але насправді хочеться щоб кожна функція відповідала за те, яку помилку віддавати клієнту
# зараз декоратор лише приблизно здогадується про те, що насправді потрібно функції
# і будь-яка нова функція легко зробить роботу декоратора не коректною

def add_contact_test(args, contacts: dict):
    """
    Функція не використовується, але більше подобається
    """
    try:
        name, phone = args
    except:
        return "Expect [name] [phone] arguments"
    if name in contacts:
        return "Contact already added, change it"
    contacts[name] = phone
    return "Contact added"

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts: dict):
    name, phone = args
    if name in contacts:
        return "Contact already added, change it"
    contacts[name] = phone
    return "Contact added"

@input_error
def change_contact(args, contacts: dict):
    name, phone = args
    if not name in contacts:
        return "Contact not exist, add it"
    contacts[name] = phone
    return "Contact changed"

@input_error
def single_phone(args, contacts: dict):
    name = args[0]
    return name + " number is " + contacts[name]

def all_phones(contacts: dict):
    if not contacts:
        return ["Contacts is empty"]
    result = []
    for name, phone in contacts.items():
        result.append(name + " number is " + phone)
    return result

def main():
    contacts = {}
    commands = [
        "close", 
        "exit", 
        "hello", 
        "add [username] [phone]", 
        "change [username] [phone]", 
        "phone [username]", 
        "all"
    ]
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
            print(single_phone(args, contacts))
        elif command == "all":
            print("\n".join(all_phones(contacts)))
        else:
            print("Invalid command. Available commands:\n   ", "\n    ".join(commands))

if __name__ == "__main__":
    main()
