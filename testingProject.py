import unittest
# from project import project

class testProject(unittest.Testcase):

	def  test_add_skills(self):
		self.assertTrue(project(None), msg='Please add a course:')
	def test_view_skills(self):
		self.assertTrue(project(None), msg='Please complete a course:')
	
	if __name__ == '__main__':
		unittest.main()