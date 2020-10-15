import System 
import pytest
import Student


#tests if the program can handle a incorrect password 
def test_view_assignments(grading_system):

    grading_system.test_view_assignments()


@pytest.fixture
def grading_system():
    name = "akend3"
    users = ["akend3","hdjsr7"]
    courses = ["comp_sci","databases"]
    gradingSystem = Student.Student(name,users,courses)
    return gradingSystem
