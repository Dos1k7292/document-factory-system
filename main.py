from documents import (
    ReportCreator,
    ResumeCreator,
    LetterCreator,
    InvoiceCreator
)


# Функция для получения нужного создателя (фабрики)
def get_creator(choice):

    if choice == "1":
        return ReportCreator()

    elif choice == "2":
        return ResumeCreator()

    elif choice == "3":
        return LetterCreator()

    elif choice == "4":
        return InvoiceCreator()

    else:
        # Если выбор неверный
        return None


# Главная функция программы
def main():

    # Цикл для создания нескольких документов
    while True:

        # Меню выбора типа документа
        print("\nChoose document type:")
        print("1 - Report")
        print("2 - Resume")
        print("3 - Letter")
        print("4 - Invoice")

        choice = input("Enter choice: ")

        # Получаем соответствующую фабрику
        creator = get_creator(choice)

        # Проверка на корректность выбора
        if creator is None:
            print("Invalid choice")
            continue

        # Создаем документ через фабрику
        document = creator.create_document()

        # Открываем документ
        document.open()

        # Спрашиваем пользователя, создать ли еще документ
        again = input("Create another document? (yes/no): ")

        if again.lower() != "yes":
            break


# Точка входа в программу
if __name__ == "__main__":
    main()
