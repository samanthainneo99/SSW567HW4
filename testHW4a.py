import unittest

from HW4a import FindRepos



class TestGithubAPI(unittest.TestCase):
    def test1(self):
        self.assertEqual(FindRepos('samanthainneo9999'), "Cannot find requested user")
    def test2(self):
        self.assertEqual(FindRepos('samanthainneo99'), 11)
    def test3(self):
        self.assertEqual(FindRepos('samanthainneo'), "No Repositories")
       
if __name__ == '__main__':
    unittest.main()