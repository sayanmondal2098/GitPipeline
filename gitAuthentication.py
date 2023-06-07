from github import Github

class RepoObject():

    def __init__(self, access_token, username):
        self.access_token = access_token
        self.username = username
        self.g = Github(self.access_token)
        self.user = self.g.get_user(self.username)

    def searchRepo(self, repoName):
        return self.user.get_repo(repoName)
    
    def getRepoObject(self, repoName):
        return self.searchRepo(repoName)
    
    def __str__(self) -> str:
        return super().__str__()
    
