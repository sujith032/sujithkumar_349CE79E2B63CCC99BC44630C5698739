'''
implement a function called sort_students that takes a list of student objects as input and sorts the
list based on their CGPA(cumulative grade point average) in descending order.each student object
has the following attributes: name(string),roll_number(string)andcgpa(float).test the function
with different input lists of students.
'''


class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the student_list in descending order of cgpa
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


# Example usage:
students = [
    Student("hari", "A123", 7.8),
    Student("srikanth", "A124", 8.9),
    Student("saumya", "A125", 9.1),
    Student("mahidhar", "A126", 9.9),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                     student.roll_number,
                                                     student.cgpa))
