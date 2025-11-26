def main():
    # Основной список для хранения данных студентов
    students = []

    while True:
        # Главное меню программы
        print("--- Student Grade Analyzer ---")
        print("1. Add new student")
        print("2. Add grades for a student")
        print("3. Generate a full report")
        print("4. Find the top student")
        print("5. Exit program")

        choice = input("Enter your choice: ")

        try:
            # Обработка выбора пользователя
            if choice == "1":
                AddNewStudents(students)
            elif choice == "2":
                AddGradesForStudent(students)
            elif choice == "3":
                FullReport(students)
            elif choice == "4":
                TopStudents(students)
            elif choice == "5":
                print("Exiting program")
                break
            else:
                print("Enter a valid number from 1 to 5")
        except Exception as e:
            # Общая обработка ошибок в меню
            print(f'Error: {e}')


def AddNewStudents(students):
    # Добавление нового студента
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty")
        return

    # Проверка на существующего студента
    for student in students:
        if student["name"].strip() == name.strip():
            print(f'Student with name {name} already exists')
            return

    # Создание записи нового студента
    newStudent = {
        "name": name,
        "grades": []
    }
    students.append(newStudent)
    print(f'Student {name} added successfully')


def AddGradesForStudent(students):
    # Добавление оценок для существующего студента
    if not students:
        print("No students added, at first add students")
        return

    name = input("Enter student name: ").strip()
    studentFound = None

    # Поиск студента по имени
    for student in students:
        if student["name"].lower() == name.lower():
            studentFound = student
            break

    if studentFound is None:
        print(f'Student with name {name} not found')
        return

    # Цикл ввода оценок
    print(f'Enter grades for student {studentFound["name"]}: ')
    while True:
        grade_input = input("Enter grade (or enter 'done' to finish'): ").strip().lower()
        if grade_input == 'done':
            break
        try:
            # Валидация и добавление оценки
            grade = int(grade_input)
            if 0 <= grade <= 100:
                studentFound["grades"].append(grade)
                print(f'Grade {grade} added successfully')
            else:
                print(f'Enter a number from 1 to 100')

        except ValueError:
            print(f'Invalid grade. Enter a valid grade.')


def AvgGrades(grades):
    # Расчет среднего балла
    if not grades:
        return None
    else:
        average = sum(grades) / len(grades)
        return average


def FullReport(students):
    # Генерация полного отчета по всем студентам
    if not students:
        print("No students added, at first add students")
        return

    avgGrades = []  # Список для хранения средних баллов

    for student in students:
        try:
            avg = AvgGrades(student["grades"])

            if avg is None:
                print(f'Average grade for student {student["name"]} is N/A')
            else:
                form_avg = round(avg, 2)
                print(f'Average grade for student {student["name"]} is {form_avg}')
                avgGrades.append(form_avg)

        except ZeroDivisionError:
            print(f'Average grade for student {student["name"]} is N/A')
        except Exception as e:
            print(f"Error calculating average for {student["name"]}: {e}")

    # Фильтрация студентов с оценками
    AvgValid = [avg for avg in avgGrades if avg is not None]

    if not AvgValid:
        return

    # Вывод статистики
    print("-------------------")
    print(f'Max average grade: {max(AvgValid)}')
    print(f'Min average grade: {min(AvgValid)}')
    print(f'Overall average grade: {round(sum(AvgValid) / len(AvgValid), 1)}')


def TopStudents(students):
    # Поиск студента с наивысшим средним баллом
    if not students:
        print("No students added, at first add students")
        return

    # Создание списка студентов с оценками
    StudentsWithGrades = []
    for student in students:
        avg = AvgGrades(student["grades"])
        if avg is not None:
            StudentsWithGrades.append((student, avg))

    if not StudentsWithGrades:
        print("No students with grades available")
        return

    try:
        # Поиск лучшего студента с использованием lambda
        topStudent, topGrade = max(StudentsWithGrades, key=lambda x: x[1])
        print(f'The student with the highest average grade is {topStudent["name"]} with grade {round(topGrade, 1)}')
    except Exception as e:
        print(f"Error finding top student: {e}")


if __name__ == '__main__':
    main()