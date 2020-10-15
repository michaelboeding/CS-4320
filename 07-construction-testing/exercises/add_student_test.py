import System 
import pytest
import Professor


#tests if the program can handle a incorrect password 
def test_add_student(grading_system):

    grading_system.add_student()


@pytest.fixture
def grading_system():
    name = "goggins"
    users = ["akend3","hdjsr7"]
    courses = ["databases","software_engineering"]
    gradingSystem = Professor.Professor(name,users,courses)
    return gradingSystem
