import System 
import pytest
import Staff


#tests if the program can handle a incorrect password 
def test_change_grade(grading_system):
    user = "akend3"
    course = "comp_sci"
    assignment = "assignment1"
    grade = 99

    grading_system.change_grade(user,course,assignment,grade)



@pytest.fixture
def grading_system():
    gradingSystem = Staff.Staff()
    return gradingSystem
