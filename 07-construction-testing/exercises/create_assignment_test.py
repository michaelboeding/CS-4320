import System 
import pytest
import Staff


#tests if the program can handle a incorrect password 
def test_create_assignment(grading_system):

    assignment_name = "assignment4"
    assignment_due_date = "06/15/20"
    course = "comp_sci"
    grading_system.create_assignment(assignment_name,assignment_due_date,course)



@pytest.fixture
def grading_system():
    gradingSystem = Staff.Staff()
    return gradingSystem
