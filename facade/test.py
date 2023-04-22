import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'Facade.java'])
subprocess.call(['java', 'Facade'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Facade.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Facade.cpp', '-o', 'Facade'])
subprocess.call(['./Facade'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Facade.ts'])
subprocess.call(['node', 'Facade.js'])

os.remove('Facade')
os.remove('Facade.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)