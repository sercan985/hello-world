#!/usr/bin/env python3
import ctypes
import os,sys
from models.Word import Word
from models.Phrase import Phrase

if __name__ == "__main__":
    
    if os.name != "nt":
        print("This program only works on Windows")
        sys.exit(1)
        
    hello = Word([33,4,11,11,14])
    world = Word([48,14,17,11,3])
    hello_world = Phrase([hello,world])

    msvcrt = ctypes.cdll.LoadLibrary("C:\\Windows\\System32\\msvcrt.dll")
    msvcrt.printf(hello_world.to_bytes())
