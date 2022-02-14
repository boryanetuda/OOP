from statistics import mean


class Student:

    items = []

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.items.append(self.grades)

    def add_fin_courses(self, course_name):
        self.finished_courses.append(course_name)

    def add_prog_courses(self, course_name):
        self.courses_in_progress.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) \
                and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def ave_grade(self):
        sum_grades = 0
        i = 0
        while True:
            for k, v in self.grades.items():
                sum_grades += mean(v)
                i += 1
            return f'{sum_grades/i:.1f}'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за дз: {self.ave_grade()}\n' \
              f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
              f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.ave_grade() < other.ave_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.ave_grade() <= other.ave_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.ave_grade() == other.ave_grade()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    items = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.items.append(self.grades)

    def ave_grade(self):
        sum_grades = 0
        i = 0
        while True:
            for k, v in self.grades.items():
                sum_grades += mean(v)
                i += 1
            return f'{sum_grades / i:.1f}'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.ave_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.ave_grade() < other.ave_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.ave_grade() <= other.ave_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.ave_grade() == other.ave_grade()


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


some_student1 = Student('Ruoy', 'Eman')
some_student1.courses_in_progress += ['Python', 'Git']

some_student2 = Student('Ruuooyy', 'Eemaan')
some_student2.courses_in_progress += ['Git']

some_lecturer1 = Lecturer('Some', 'Buddy')
some_lecturer1.courses_attached += ['Python', 'Git']

some_lecturer2 = Lecturer('Soomee', 'Buuddyy')
some_lecturer2.courses_attached += ['Git']

some_reviewer1 = Reviewer('Bobba', 'Fett')
some_reviewer1.courses_attached += ['Python', 'Git']

some_reviewer2 = Reviewer('Boobbaa', 'Feett')
some_reviewer2.courses_attached += ['Git']

some_reviewer1.rate_hw(some_student1, 'Python', 9)
some_reviewer1.rate_hw(some_student1, 'Python', 9)
some_reviewer1.rate_hw(some_student1, 'Python', 9)
some_reviewer1.rate_hw(some_student1, 'Git', 2)
some_reviewer1.rate_hw(some_student1, 'Git', 2)
some_reviewer1.rate_hw(some_student1, 'Git', 2)
some_student1.add_fin_courses('Введение в программирование')

some_reviewer2.rate_hw(some_student2, 'Git', 3)
some_reviewer2.rate_hw(some_student2, 'Git', 3)
some_reviewer2.rate_hw(some_student2, 'Git', 3)
some_student2.add_fin_courses('Введение в программирование')

some_student1.rate_lec(some_lecturer1, 'Python', 8)
some_student1.rate_lec(some_lecturer1, 'Python', 8)
some_student1.rate_lec(some_lecturer1, 'Python', 8)
some_student1.rate_lec(some_lecturer1, 'Git', 4)
some_student1.rate_lec(some_lecturer1, 'Git', 4)
some_student1.rate_lec(some_lecturer1, 'Git', 4)

some_student2.rate_lec(some_lecturer2, 'Git', 5)
some_student2.rate_lec(some_lecturer2, 'Git', 5)
some_student2.rate_lec(some_lecturer2, 'Git', 5)


def ave_grades_all(grade_list, course_name):
    ave_grades = []
    for courses in grade_list:
        for course, grades in courses.items():
            if course_name in course:
                ave_grades.extend(grades)
    print(f'Средняя оценка по курсу {course_name}: {mean(ave_grades):.2f}\n')

print(some_reviewer1, '\n')
print(some_reviewer2, '\n')
print(some_lecturer1, '\n')
print(some_lecturer2, '\n')
print(some_student1, '\n')
print(some_student2, '\n')

print(some_student2 < some_student1)
print(some_student2 <= some_student1)
print(some_student2 == some_student1, '\n')

print(some_lecturer2 > some_lecturer1)
print(some_lecturer2 >= some_lecturer1)
print(some_lecturer2 != some_lecturer1, '\n')

ave_grades_all(Student.items, 'Git')
ave_grades_all(Lecturer.items, 'Git')
