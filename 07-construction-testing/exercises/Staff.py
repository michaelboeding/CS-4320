import json
import User

class Staff(User.User):

    def update_course_db(self):
        with open('Data/courses.json', 'w') as fp:
            json.dump(self.all_courses, fp)

    def create_assignment(self,assignment_name, due_date, course):
        course = {
            assignment_name: {
                'due_date': due_date
            }
        }
        self.all_courses[course]['assignments'].update(course)
        self.update_course_db()

    def change_grade(self,user,course,assignment,grade):
        user['courses'][course]['assignments'][assignment]['grade'][grade]
        self.update_user_db()

    def check_grades(self,name,course):
        assignments = self.users[name]['courses'][course]
        grades = []
        for key in assignments:
            grades.append([key, assignments[key]['grade']])
        return grades



