import unittest
from unittest.mock import Mock, patch
from nose.tools import assert_true    
from nose.tools import assert_is_not_none
import requests


from HW4a import FindRepos



class TestGithubAPI(unittest.TestCase):
    def test_request_response(self):#This is the example given by the third link provided in the assignment
        # Send a request to the API server and store the response.
        response = requests.get('https://api.github.com/users/samanthainneo99/repos') 
        # Confirm that the request-response cycle completed successfully.
        assert_true(response.ok)  
    def test_request_response2(response): #next example from the third link
        response == FindRepos('samanthainneo9999')
        assert_is_not_none(response)

    @patch('requests.get')
    def test1(self, mock_get):
        mock_get.return_value.ok = False
        self.assertEqual(FindRepos('samanthainneo9999'), "Cannot find requested user")
    # @patch('requests.get')
    # def test2(self, mock_request):
    #     mock_request.get('https://api.github.com/users/samanthainneo99/repos')
    #     self.assertEqual(FindRepos('samanthainneo99'), 11)
    # @patch('requests.get')
    # def test3(self, mock_request):
    #     mock_request.get('https://api.github.com/users/samanthainneo99/repos')
    #     self.assertEqual(FindRepos('samanthainneo'), "No Repositories")
     
if __name__ == '__main__':
    unittest.main()