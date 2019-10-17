import subprocess

class Git: 

    @staticmethod
    def get_user_global(): 
        name = subprocess.check_output(["git", "config", "--global", "user.name"])
        email = subprocess.check_output(["git", "config", "--global", "user.name"])
        signing_key = subprocess.check_output(["git", "config", "--global", "user.signingkey"])
        git_user = GitUser(name, email, signing_key)
        return git_user;


    @staticmethod
    def get_user_local:

    @staticmethod
    def set_user_global:

    @staticmethod
    def set_user_local: 

    @staticmethod
    def clone:

    @staticmethod
    def revise:

    @staticmethod
    def build_revise_cmd:
