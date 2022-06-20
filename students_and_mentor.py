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

print()

#3 Задание

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.allmarks = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_from_students:
               lecturer.grades_from_students[course] += [grade]
            else:
               lecturer.grades_from_students[course] = [grade]
        else:
            return 'Ошибка'

    def students_marks(self):
      for k,v in self.grades.items():
        self.allmarks = (sum(v)/len(v))
        return self.allmarks

    def __str__(self):
      return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.allmarks}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"

    def __le__(self,other):
      return self.allmarks <= other.lect_allmarks

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.grades_from_students = {}
      self.lect_allmarks = []
      self.courses_attached = []

    def lecturer_marks(self):
      for k,v in self.grades_from_students.items():
        self.lect_allmarks = (sum(v)/len(v))
        return self.lect_allmarks

    def __str__(self):
      return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.lect_allmarks}"

    def __le__(self,other):
      return self.allmarks <= other.lect_allmarks


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
      return f"Имя: {self.name}\nФамилия: {self.surname}"

first_student = Student('Danny', 'DeVito', 'male')
first_student.courses_in_progress += ['Python','Git']
first_student.finished_courses += ['Введение в программирование']

first_reviever = Reviewer('Indiana', 'Jones')
first_reviever.courses_attached += ['Python']

first_lecturer = Lecturer('Jany', 'Fox')
first_lecturer.courses_attached += ['Python']

first_reviever.rate_hw(first_student, 'Python', 9)
first_reviever.rate_hw(first_student, 'Python', 8)
first_reviever.rate_hw(first_student, 'Python', 7)

first_student.rate_hw(first_lecturer, 'Python', 10)
first_student.rate_hw(first_lecturer, 'Python', 9)
first_student.rate_hw(first_lecturer, 'Python', 8)


print("Оценки студента от лектора-", first_student.grades)
print("Оцеки лектора от студента-", first_lecturer.grades_from_students)
print(first_student.students_marks())
print(first_lecturer.lecturer_marks())
print(first_student)
print(first_lecturer)
print(first_reviever)
print(first_student.allmarks >= first_lecturer.lect_allmarks)

print()

#4 Задание

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.allmarks = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_from_students:
               lecturer.grades_from_students[course] += [grade]
            else:
               lecturer.grades_from_students[course] = [grade]
        else:
            return 'Ошибка'

    def students_marks(self):
      for k,v in self.grades.items():
        self.allmarks = (sum(v)/len(v))
        return self.allmarks

    def __str__(self):
      return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.allmarks}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}"

    def __le__(self,other):
      return self.allmarks <= other.lect_allmarks

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.grades_from_students = {}
      self.lect_allmarks = []
      self.courses_attached = []

    def lecturer_marks(self):
      for k,v in self.grades_from_students.items():
        self.lect_allmarks = (sum(v)/len(v))
        return self.lect_allmarks

    def __str__(self):
      return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.lect_allmarks}"

    def __le__(self,other):
      return self.allmarks <= other.lect_allmarks


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
      return f"Имя: {self.name}\nФамилия: {self.surname}"

first_student = Student('Danny', 'DeVito', 'male')
first_student.courses_in_progress += ['Python','Git']
first_student.finished_courses += ['Введение в программирование']

second_student = Student('Arnold', 'Schwarzenegger', 'male')
second_student.courses_in_progress += ['Python','Git']
second_student.finished_courses += ['Введение в программирование']

first_reviever = Reviewer('Indiana', 'Jones')
first_reviever.courses_attached += ['Python']

second_reviever = Reviewer('Julia','Roberts')
second_reviever.courses_attached += ['Python']

first_lecturer = Lecturer('Jany', 'Fox')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Dwayne', 'Johnson')
second_lecturer.courses_attached += ['Python']

first_reviever.rate_hw(first_student, 'Python', 9)
first_reviever.rate_hw(first_student, 'Python', 8)
first_reviever.rate_hw(first_student, 'Python', 7)

first_reviever.rate_hw(second_student, 'Python', 8)
first_reviever.rate_hw(second_student, 'Python', 7)
first_reviever.rate_hw(second_student, 'Python', 6)

second_reviever.rate_hw(first_student, 'Python', 10)
second_reviever.rate_hw(first_student, 'Python', 9)
second_reviever.rate_hw(first_student, 'Python', 8)

second_reviever.rate_hw(second_student, 'Python', 7)
second_reviever.rate_hw(second_student, 'Python', 6)
second_reviever.rate_hw(second_student, 'Python', 5)

first_student.rate_hw(first_lecturer, 'Python', 10)
first_student.rate_hw(first_lecturer, 'Python', 9)
first_student.rate_hw(first_lecturer, 'Python', 8)

first_student.rate_hw(second_lecturer, 'Python', 10)
first_student.rate_hw(second_lecturer, 'Python', 8)
first_student.rate_hw(second_lecturer, 'Python', 6)

second_student.rate_hw(first_lecturer, 'Python', 10)
second_student.rate_hw(first_lecturer, 'Python', 9)
second_student.rate_hw(first_lecturer, 'Python', 8)

second_student.rate_hw(second_lecturer, 'Python', 10)
second_student.rate_hw(second_lecturer, 'Python', 10)
second_student.rate_hw(second_lecturer, 'Python', 10)




print("Оценки первого студента от лекторов-", first_student.grades)
print(f'Средная оценка: {first_student.students_marks()}')

print("Оценки второго студента от лекторов-", second_student.grades)
print(f'Средная оценка: {second_student.students_marks()}')

print("Оцеки первого лектора от студентов-", first_lecturer.grades_from_students)
print(f'Средая оценка: {first_lecturer.lecturer_marks()}')

print("Оцеки второго лектора от студентов-", second_lecturer.grades_from_students)
print(f'Средая оценка: {second_lecturer.lecturer_marks()}')

print(first_student)
print(second_student)
print(first_lecturer)
print(second_lecturer)
print(first_reviever)
print(second_reviever)
print(first_student.allmarks >= first_lecturer.lect_allmarks)
print(first_student.allmarks <= second_lecturer.lect_allmarks)

group_student = [first_student,second_student]
group_lecturer = [first_lecturer,second_lecturer]

def all_students_marks(marks,course):
  students_marks_list = []
  for obj in marks:
    students_marks_list.append(sum(obj.grades[course])/len(obj.grades[course]))
    return f'Средняя оценка за домашние задания по всем студентам в рамках курса {course} составляет {students_marks_list}'
print(all_students_marks(group_student,'Python'))

def all_lecturer_marks(marks,course):
  lecturer_marks_list = []
  for obj in marks:
    lecturer_marks_list.append(sum(obj.grades_from_students[course])/len(obj.grades_from_students[course]))
    return f'средняя оценки за лекции всех лекторов в рамках курса {course} составляет {lecturer_marks_list}'
print(all_students_marks(group_student,'Python'))
print(all_lecturer_marks(group_lecturer,'Python'))

print('Последние 2 функции что то не правильно, если не сложно подскажите примерно как реализовать, заранее спасибо')
