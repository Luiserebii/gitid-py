import sys, subprocess

class Util:

    @staticmethod
    def exec(args, no_strip=False):
        out = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout.decode(sys.stdout.encoding)
        if(not no_strip):
            out = out.strip();
        return out;

