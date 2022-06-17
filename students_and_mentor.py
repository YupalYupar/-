class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_from_students:
               lecturer.grades_from_students[course] += [grade]
            else:
               lecturer.grades_from_students[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades_from_students = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

first_student = Student('Danny', 'DeVito', 'male')
first_student.courses_in_progress += ['Python']

first_reviever = Reviewer('Indiana', 'Jones')
first_reviever.courses_attached += ['Python']

first_lecturer = Lecturer('Jany', 'Fox')
first_lecturer.courses_attached += ['Python']

first_reviever.rate_hw(first_student, 'Python', 9)
first_reviever.rate_hw(first_student, 'Python', 9)
first_reviever.rate_hw(first_student, 'Python', 9)

first_student.rate_hw(first_lecturer, 'Python', 10)
first_student.rate_hw(first_lecturer, 'Python', 10)
first_student.rate_hw(first_lecturer, 'Python', 10)

print("Оценки студента от лектора-", first_student.grades)
print("Оцеки лектора от студента-", first_lecturer.grades_from_students)
