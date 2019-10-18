from git_user import GitUser
from util import Util

class Git: 

    @staticmethod
    def get_user_global(): 
        name = Util.exec(["git", "config", "--global", "user.name"])
        email = Util.exec(["git", "config", "--global", "user.email"])
        signing_key = Util.exec(["git", "config", "--global", "user.signingkey"])

        git_user = GitUser(name, email, signing_key)
        return git_user;

    @staticmethod
    def get_user_local():
        name = Util.exec(["git", "config", "--local", "user.name"])
        email = Util.exec(["git", "config", "--local", "user.email"])
        signing_key = Util.exec(["git", "config", "--local", "user.signingkey"])

        git_user = GitUser(name, email, signing_key)
        return git_user;

    @staticmethod
    def set_user_global(git_user, prefix_cmd=None):
        cmd = ["git", "config", "--global", "user.name"].append(git_user.name) \
            + ["git", "config", "--global", "user.email"].append(git_user.email)
        if(git_user.signing_key != None):
            cmd += ["git", "config", "--global", "user.signingkey"].append(git_user.signing_key)
        if(prefix_cmd != None):
            cmd = prefix_cmd.append("&&") + cmd

        # Finally after constructing the command, run
        Util.exec(cmd)
        return true;

    @staticmethod
    def set_user_local(): 
        cmd = ["git", "config", "--local", "user.name"].append(git_user.name) \
            + ["git", "config", "--local", "user.email"].append(git_user.email)
        if(git_user.signing_key != None):
            cmd += ["git", "config", "--local", "user.signingkey"].append(git_user.signing_key)
        if(prefix_cmd != None):
            cmd = prefix_cmd.append("&&") + cmd

        # Finally after constructing the command, run
        Util.exec(cmd)
        return true;

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
printUser(Git.get_user_local())
