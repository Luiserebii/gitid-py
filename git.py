from git_user import GitUser
from util import Util

class Git: 

    @staticmethod
    def get_user_global(): 
        name = util.exec(["git", "config", "--global", "user.name"])
        email = util.exec(["git", "config", "--global", "user.email"])
        signing_key = util.exec(["git", "config", "--global", "user.signingkey"])

        git_user = GitUser(name, email, signing_key)
        return git_user;

    @staticmethod
    def get_user_local():
        return

    @staticmethod
    def set_user_global():
        return

    @staticmethod
    def set_user_local(): 
        return

    @staticmethod
    def clone():
        return

    @staticmethod
    def revise():
        return

    @staticmethod
    def build_revise_cmd():
        return

def printUser(u):
    print(u.name + " " + u.email + " " + u.signing_key)

printUser(Git.get_user_global())
