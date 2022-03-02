''' Author: Samantha Inneo
    Description: This assignment uses a github API to return the repo names and commits of a user
    Github Link: https://github.com/samanthainneo99/SSW567HW4

    How I designed the code: 
    One of the main points I considered when desigining easily testable code was the easy of finding suitable test cases. This program didn't really have any edge cases to worry 
    about, which would normally be one of the first things I would consider. For this assingment, I was worried about formatting the output in a way that would be consistent across all
    the cases.  I used the example given in the documentation for this assignment because I felt it worked well. Another thing I considered were the if statements to check invalid
    inputs or other failures.  In the github documentation for the API, the return code 200 was given for nonexistent users.  I knew I would have to test for this, so it was the first 
    thing I check after calling the API. Next, I needed a way to check for users without any repos. I did so by checking the length of the json.  If this is 0, then the user does not
    have any repositories. 
    '''
from nose.tools import assert_true    
import requests
import json

def FindRepos(username):
    repoList = requests.get("https://api.github.com/users/"+username+"/repos")
    
    if repoList.status_code != 200: #code from documentation when user can't be found
        return("Cannot find requested user")

    repoList = repoList.json() #store json results


    if len(repoList) == 0: #no repos were found
        return ("No Repositories")

    for r in repoList: #for every repo, get the number of commits and print formatted nicely
        repos = requests.get(r['commits_url'].split("{")[0])
        repos = repos.json()
        print("Repo: "+ r['name'] + " Number of commits: " + str(len(repos)))
    
    return len(repoList) #i return the amount of repos since it is relevant



if __name__ == "__main__":
    repo = input("Please enter Github username: ")
    FindRepos(repo)