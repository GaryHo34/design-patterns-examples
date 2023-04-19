import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'Command.java'])
subprocess.call(['java', 'Command'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Command.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Command.cpp', '-o', 'Command'])
subprocess.call(['./Command'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Command.ts'])
subprocess.call(['node', 'Command.js'])

os.remove('Command')
os.remove('Command.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)