''' Author: Samantha Inneo
    Description: This assignment uses a github API to return the repo names and commits of a user'''
import requests
import json

def FindRepos(username):
    response = requests.get("https://api.github.com/users/"+username+"/repos")
    
    if response.status_code != 200:
        return("Cannot find requested user")

    response = response.json()

    if len(response) == 0:
        return ("No Repositories")
  
    for repo in response:
        repoResponse = requests.get(repo['commits_url'].split("{")[0])
        repoResponse = repoResponse.json()
        # print(str(repoResponse))
        print("Repo: "+ repo['name'] + " Number of commits: " + str(len(repoResponse)))
   
    return True

if __name__ == "__main__":
    repo = input("Please enter Github username: ")
    FindRepos(repo)