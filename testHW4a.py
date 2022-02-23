import unittest

from HW4a import FindRepos



class TestGithubAPI(unittest.TestCase):
    def testGithub(self):
        self.assertEqual(FindRepos('samanthainneo9999'), "Cannot find requested user")
    def testGithub2(self):
        self.assertEqual(FindRepos('samanthainneo99'), "Repo: CS-146 Number of commits: 30\nRepo: SSW540 Number of commits: 4\nRepo: SSW567-Testing Number of commits: 4\nRepo: SSW567HW1 Number of commits: 12\nRepo: SSW567HW2 Number of commits: 17\nRepo: SSW567HW3 Number of commits: 2\nRepo: SSW567HW4 Number of commits: 2\nRepo: Team-4-Code Number of commits: 30\nRepo: test Number of commits: 2\nRepo: testing Number of commits: 2")
       
if __name__ == '__main__':
    unittest.main()