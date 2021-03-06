#!/usr/bin/env python
from neovim import attach
import os, sys

args = sys.argv[1:]

addr = os.environ.get("NVIM_LISTEN_ADDRESS")
if not addr:
    os.execvp('nvim', ('nvim', ) + tuple(args))

nvim = attach("socket", path=addr)
def normalizePath(name):
    return os.path.abspath(name).replace(" ", "\\ ")

def openFiles():
    # To escape terminal mode. Not sure if bug.
    nvim.feedkeys('',"n")
    for x in args:
        nvim.command("drop {}".format(normalizePath(x)))

openFiles()
