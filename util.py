import sys, subprocess

class Util:

    @staticmethod:
    exec(args, no_strip=False):

        out = subprocess.run(args, stderr=subprocess.STDOUT).stdout
        if(!no_strip) out = out.strip();
        return out;

