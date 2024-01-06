

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        

    def add_corsess(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rating(students, course):  
        for student in students:
            result = float(sum(student.grades.get(course)) / len(student.grades.get(course)))
            student.average_grades = result

    def __str__(self):
        result = f"Имя: {self.name}\nФамилия: {self.surname}\n" \
                 f"Средняя оценка за домашние задания: {self.average_grades}\n" \
                 f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
                 f"Завершенные курсы: {','.join(self.finished_courses)}"
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Students')
            return
        return self.average_grades < other.average_grades


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grades = float()

    def calculation_of_average_grades(lecturers, course):
        for lecturer in lecturers:
            result = float(sum(lecturer.grades.get(course)) / len(lecturer.grades.get(course)))
            lecturer.average_grades = result
        return

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
                 f'Средняя оценка за лекции: {self.average_grades}'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.average_grades < other.average_grades


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}'
        return result

#Создаем экземпляры класса Student
petrov = Student('Some', 'Buddy', 'Мужчина')
petrov.courses_in_progress += ['Python']
ivanov = Student('Some', 'Buddy', 'Мужчина')
ivanov.courses_in_progress += ['Python']
ivanov.courses_in_progress += ['GIT']

#Создаем экземпляры класса Lecturer
lecturer_1 = Lecturer('Some', 'Buddy')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Some', 'Buddy')
lecturer_2.courses_attached += ['Python']

#Создаем экземпляры класса Reviewer
reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_2 = Reviewer('Some', 'Buddy')
reviewer_2.courses_attached += ['Python']

#Добавляем оценки студентам за курс Python
reviewer_1.rate_hw(petrov, 'Python', 10)
reviewer_1.rate_hw(ivanov, 'Python', 9)
reviewer_2.rate_hw(petrov, 'Python', 10)
reviewer_2.rate_hw(ivanov, 'Python', 10)

#Добавляем оценки лекторам за курс Python
petrov.rate_lecture(lecturer_1, 'Python', 10)
petrov.rate_lecture(lecturer_2, 'Python', 9)
ivanov.rate_lecture(lecturer_1, 'Python', 10)
ivanov.rate_lecture(lecturer_2, 'Python', 10)

#Добавляем пройденный курс студенту
petrov.add_corsess('Введение в программирование')

#Рассчитываем средние оценки для сутеднтов за курс Python
Student.average_rating([petrov,ivanov], 'Python')

#Рассчитываем средние оценки для лекторов за курс Python
Lecturer.calculation_of_average_grades([lecturer_1,lecturer_2], 'Python')

#Проверяем переопределенные методы для созданных классов
print(reviewer_1, end='\n\n')
print(lecturer_1, end='\n\n')
print(lecturer_2, end='\n\n')
print(lecturer_1 > lecturer_2, end='\n\n')
print(ivanov, end='\n\n')
print(petrov, end='\n\n')
print(ivanov > petrov, end='\n\n')


