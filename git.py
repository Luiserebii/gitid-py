import subprocess
from git_user import GitUser

class Git: 

    @staticmethod
    def get_user_global(): 
        name = subprocess.check_output(["git", "config", "--global", "user.name"]).decode(sys.stdout.encoding)
        email = subprocess.check_output(["git", "config", "--global", "user.email"]).decode(sys.stdout.encoding)
        signing_key = subprocess.check_output(["git", "config", "--global", "user.signingkey"]).decode(sys.stdout.encoding)

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
