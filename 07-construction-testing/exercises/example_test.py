import pytest
import System

#Tests if the program can handle a wrong username
def test_login(grading_system):
    username = 'akend3'
    password =  '123454321'
    grading_system.login(username,password)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem