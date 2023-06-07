from github import Github
import base64

from pprint import pprint
import git 

class GitRepository():

    def __init__(self, repoObject):
        self.repoObject = repoObject

    def print_repo(self):
        # repository full name
        print("Full name:", self.repoObject.full_name)
        # repository description
        print("Description:", self.repoObject.description)
        # the date of when the repo was created
        print("Date created:", self.repoObject.created_at)
        # the date of the last git push
        print("Date of last push:", self.repoObject.pushed_at)
        # home website (if available)
        print("Home Page:", self.repoObject.homepage)
        # programming language
        print("Language:", self.repoObject.language)
        # number of forks
        print("Number of forks:", self.repoObject.forks)
        # number of stars
        print("Number of stars:", self.repoObject.stargazers_count)
        print("-"*50)
        # repository content (files & directories)
        print("Contents:")
        for content in self.repoObject.get_contents(""):
            print("License:", base64.b64decode(self.repoObject.get_license().content.encode()).decode())
            print(content)
        print("-"*50)

    def getrepoName(self):
        return self.repoObject.full_name
    
    def getrepoDescription(self):
        return self.repoObject.description
    
    def getrepoCreatedDate(self):
        return self.repoObject.created_at

    def getrepoURL(self):
        return self.repoObject.clone_url

    def downloadRepo(self):
        name = self.getrepoName()
        URL = self.getrepoURL()
        print("Downloading: "+name + " from URL : " + URL)
        print("Saving to: "+"./repos/"+name)
        git.Repo.clone_from(URL, "./repos/"+name)

    def getRepoObject(self):
        return self.repoObject
    
    def __str__(self) -> str:
        return super().__str__()