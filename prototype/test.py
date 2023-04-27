import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'Prototype.java'])
subprocess.call(['java', 'Prototype'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Prototype.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Prototype.cpp', '-o', 'Prototype'])
subprocess.call(['./Prototype'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Prototype.ts', '--target', 'es6'])
subprocess.call(['node', 'Prototype.js'])

os.remove('Prototype')
os.remove('Prototype.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)