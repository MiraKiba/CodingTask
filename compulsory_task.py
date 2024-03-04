class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def head_office_location(self):
        print("Head office location: Cape Town")

class OOPCourse(Course):
    def __init__(self):
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):
        print("Course description:", self.description)
        print("Trainer:", self.trainer)

    def show_course_id(self):
        print("Course ID number: #12345")

# Creating an object of the subclass
course_1 = OOPCourse()

# Calling methods
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()