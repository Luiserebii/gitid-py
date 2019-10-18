import sys, subprocess

class Util:

    @staticmethod
    def exec(args, no_strip=False):

        out = subprocess.run(args, stderr=subprocess.STDOUT).stdout
        if(not no_strip): out = out.strip();
        return out;

