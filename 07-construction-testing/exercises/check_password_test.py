import System 
import pytest




#tests if the program can handle a incorrect password 
def test_check_password(grading_system):
    name = 'akend3'
    passwordEntered =  '123454321'
    grading_system.check_password(name,passwordEntered)



@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem
