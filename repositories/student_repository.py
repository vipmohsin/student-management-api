import os
import json 
from student import Student

class StudentRepository:
    def __init__(self,filename="students.json"):
        self.filename=filename
        self.students=[]
        self.next_roll=101
        
        self._load()

    # load students ---------------------------------------------------------------
    def _load(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            self.next_roll = data["next_roll_no"]

            for student_data in data["students"]:
                student = Student.from_dict(student_data)
                self.students.append(student)

        except json.JSONDecodeError as e:
            raise RuntimeError(
            "Student data file contains invalid JSON."
        ) from e

        except KeyError as e:
            raise RuntimeError(
            "Student data file has an invalid structure."
            ) from e

        except OSError as e:
            raise RuntimeError(
            "Student data file could not be read."
        ) from e
       
            
    #save students 
    def _save(self):
        students_data=[student.to_dict() for student in self.students]
        data={
            "next_roll_no": self.next_roll,
            "students":students_data
        }    
        # data file----------------------------------------------------------------
        try:
            with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)

        except OSError as e:
            raise RuntimeError(
            "Student data could not be saved."
            ) from e
        
    
    def get_all(self):
        return self.students.copy() 
    
    def find_by_roll(self,roll):
        for student in self.students:
            if student.roll_no == roll:
                return student  
        return None 
             
    def add(self,name, age, marks):
        student=Student(self.next_roll,name,age,marks)
        self.students.append(student)     
        self.next_roll +=1
        try:
            self._save()
        except Exception:
            # Rolling back changes in memory 
            self.students.remove(student)
            self.next_roll-=1
            
            # sending the error upward
            raise 
        
        return student
    
    def update(self,student,name, age, marks):
        old_name= student.name
        old_age=student.age
        old_marks=student.marks
        
        student.name=name
        student.age=age 
        student.marks=marks
        
        try:
            self._save()
        except Exception:
            #Roll back to previous values
            student.name=old_name
            student.age=old_age 
            student.marks=old_marks
            raise
        return student
        
    def delete(self,student):
        index = self.students.index(student)
        
        self.students.remove(student)
        try:   
            self._save()
        except Exception:
            #Roll back insert the student back at its original position
            self.students.insert(index,student)  
            raise

        return True
