import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'Builder.java'])
subprocess.call(['java', 'Builder'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Builder.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Builder.cpp', '-o', 'Builder'])
subprocess.call(['./Builder'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Builder.ts'])
subprocess.call(['node', 'Builder.js'])

os.remove('Builder')
os.remove('Builder.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)