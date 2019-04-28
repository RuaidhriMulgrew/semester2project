def main():
    load_data()
    show_menu()
    save_data()


def load_data():
    print("load_data() function")
    print()


def save_data():
    print()
    print("save_data() function")


def show_all_employees():
    print("Show all employees.")


def show_employee():
    print("View a particular employee.")


def change_salary():
    print("Edit the salary of an employee.")


def add_employee():
    print("Add a new employee.")


def remove_employee():
    print("Remove an employee.")


def save_bonus_info():
    print("Give a bonus to each employee, writing the details to a file.")


def generate_report():
    print("Generate a report for management.")


def show_menu():
    run = True
    while run:
        user_input = int(input("Enter number of desired choice:\n"
                               "1. View all employees.\n"
                               "2. View a particular employee.\n"
                               "3. Edit the salary of an employee.\n"
                               "4. Add a new employee.\n"
                               "5. Remove an employee.\n"
                               "6. Give a bonus to each employee, writing the details to a file.\n"
                               "7. Generate a report for management.\n"
                               "8. Quit.\n"))

        if user_input == 1:
            # Calling placeholder function that just contains a print statement.
            show_all_employees()
        elif user_input == 2:
            show_employee()
        elif user_input == 3:
            change_salary()
        elif user_input == 4:
            add_employee()
        elif user_input == 5:
            remove_employee()
        elif user_input == 6:
            save_bonus_info()
        elif user_input == 7:
            generate_report()
        elif user_input == 8:
            print("Quit.")
            run = False


main()
