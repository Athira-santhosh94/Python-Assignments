# Question 1

class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_info(self):
        return f"Course Code: {self.course_code}, Course Name: {self.course_name}, Credit Hours: {self.credit_hours}"

class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def display_info(self):
        required_status = "Yes" if self.required_for_major else "No"
        return super().display_info() + f", Required for Major: {required_status}"

class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def display_info(self):
        return super().display_info() + f", Elective Type: {self.elective_type}"

# Example usage
core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
elective_course = ElectiveCourse("HIST201", "World History", 2, "liberal arts")

print(core_course.display_info())
print(elective_course.display_info())

#Question 2

# Step 1 - Create employee.py file 
%%writefile employee.py

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

# Step 2 - Import the employee module and create an object
import employee
emp1 = employee.Employee("John Doe", 50000)
print("Employee Name:", emp1.get_name())
print("Employee Salary:", emp1.get_salary())
