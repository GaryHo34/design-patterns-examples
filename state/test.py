import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'State.java'])
subprocess.call(['java', 'State'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'State.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'State.cpp', '-o', 'State'])
subprocess.call(['./State'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'State.ts'])
subprocess.call(['node', 'State.js'])

os.remove('State')
os.remove('State.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)