from gitAuthentication import RepoObject
from gitRepository import GitRepository

# Create a RepoObject

access_token = "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"

GitRepositoryObj = RepoObject(access_token, "sayanmondal2098")

discordBot = GitRepositoryObj.getRepoObject("Discord-bot")

discordBotObj = GitRepository(discordBot)

discordBotObj.print_repo()

discordBotObj.downloadRepo()
