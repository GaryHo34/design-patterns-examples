import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'Decorator.java'])
subprocess.call(['java', 'Decorator'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Decorator.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Decorator.cpp', '-o', 'Decorator'])
subprocess.call(['./Decorator'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Decorator.ts'])
subprocess.call(['node', 'Decorator.js'])

os.remove('Decorator')
os.remove('Decorator.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)