#!/bin/python
import subprocess

def subpro_scan(command: str) -> str:
    cmd = command
    p = subprocess.Popen(cmd, shell=True, stdout= subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode()
    return out
