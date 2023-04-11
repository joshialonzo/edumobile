from dataclasses import dataclass
from typing import List


@dataclass
class Student:
    name: str


@dataclass
class TeacherExam:
    answers: List[str]


@dataclass
class StudentExam:
    teacher: TeacherExam
    student: Student
    answers: List[str]

    def grade(self):
        answer_sheet = self.teacher.answers
        name = self.student.name
        answers = self.answers
        total = 0
        answers_number = len(answer_sheet)
        for i in range(answers_number):
            right_answer = answer_sheet[i]
            student_answer = answers[i]
            if student_answer == right_answer:
                total += 1
        percentage = round(total / answers_number * 100, 1)
        return name, percentage
