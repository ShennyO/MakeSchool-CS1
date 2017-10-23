from classroom import Classroom
from student import Student
import pdb

# this is the function we call after we set up our classroom
def classroom_actions(classroom):
    action = input("Hi! Welcome to your new classroom! Here are some of your actions for your classroom:(addStu - adds a new student to your classroom, remStu - removes named student from class, getStu - enter student account for further student actions: ")
    if action == "addStu":
        student_name = input("What is the name of your new student: ")
        classroom.create_student(student_name)
        print("Nice! You added %s to your %s classroom" % (student_name, Classroom))
        classroom_actions(classroom)
    if action == "remStu":
        student_name = input("What is the name of the student you want to remove: ")
        classroom.delete_student(student_name)
    if action == "getStu":
        student_name = input("Which student do you want to see: ")
        selected_student = classroom.students[student_name]
        student_action = input("What do you want to do for your student:(adda - add an assignment for your student, rema - remove an assignment for your student, upda - updates an assignment for your student: ")
        if student_action == "adda":
            assignment_name = input("What is your assignment name: ")
            selected_student.add_assignment(assignment_name)
            print("Awesome, you just added %s to your student's assignments" % assignment_name)
            classroom_actions(classroom)
        elif student_action == "upda":
            assignment_name = input("What is the assignment you're looking for: ")
            assignment_grade = input("What is the grade for that assignment: ")
            selected_student.update_assignment(assignment_name, assignment_grade)
            print("You just updated %s's %s assignment to an %s grade" % (selected_student.name, assignment_name, assignment_grade))
            classroom_actions(classroom)
        elif student_action == "rema":
            assignment_name = input("What is the assignment you're looking for: ")
            selected_student.remove_assignment(assignment_name)
            print("You just removed %s assignment from %s assignment list" % (assignment_name, selected_student.name))
            classroom_actions(classroom)
        else:
            pass



def create_class(class_dict):
    name_of_class = input("Let's create a new classroom, What's the name of your class: ")
    day_class = input("What day/days does your class meet: ")
    time_class = input("What time does your class meet: ")
    new_class = Classroom(name_of_class, day_class, time_class)
    class_dict[name_of_class] = new_class
    print("Congratulations! You created %s class that meets %s at %s" % (name_of_class, day_class, time_class))
    action = input("What do you want to do next? (enter_class - enters the selected class, new_class - make a new class: ")
    if action == "enter_class":
        classroom_actions(new_class)

    if action == "new_class":
        create_class(classes_list)


def main():
    classes_list = {}
    create_class(classes_list)


main()
