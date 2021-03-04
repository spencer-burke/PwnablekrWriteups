#!/usr/bin/python3
import sys
import subprocess

def pad(arg):
    res = ""
    if(len(str(arg)) < 20):
        diff = 20 - len(str(arg))
        res = str(arg)
        for x in range(diff-1):
            res = "0" + res
    if(res != ""):
        return res
    else:
        return arg 

def main():
    num = 0;
    with open("log.out", "a") as f:
        for x in range(99999999999999999999):
            f.write(subprocess.check_output("./run " + str(pad))) 

if __name__ == "__main__":
    main()

