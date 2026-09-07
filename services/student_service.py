from repositories.student_repository import StudentRepository


class StudentService:

    def __init__(self, repo: StudentRepository):
        self.repo = repo

    def get_all_students(self):
        return self.repo.get_all()

    def get_student_by_roll(self, roll_no):
        student = self.repo.find_by_roll(roll_no)

        if student is None:
            return None

        return student

    def create_student(self, name, age, marks):
        return self.repo.add(name, age, marks)

    def update_student(self, roll_no, name, age, marks):
        student = self.repo.find_by_roll(roll_no)

        if student is None:
            return None

        return self.repo.update(
            student,
            name,
            age,
            marks
        )

    def delete_student(self, roll_no):
        student = self.repo.find_by_roll(roll_no)

        if student is None:
            return None

        self.repo.delete(student)

        return True