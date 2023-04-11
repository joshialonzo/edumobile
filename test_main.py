from main import Student, StudentExam, TeacherExam


def test_grade_allan():
    answer_sheet = [
        "A",
        "A",
        "C",
        "D",
        "D",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "D",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "D",
        "A",
    ]
    student_answers = [
        "A",
        "C",
        "C",
        "B",
        "D",
        "B",
        "C",
        "A",
        "C",
        "B",
        "A",
        "A",
        "C",
        "B",
        "D",
        "C",
        "B",
        "A",
        "D",
        "A",
    ]

    student = Student(name="Allan")
    teacher = TeacherExam(answers=answer_sheet)
    student_exam = StudentExam(
        teacher=teacher,
        student=student,
        answers=student_answers,
    )
    assert student_exam.grade() == (
        "Allan",
        85.0,
    )
