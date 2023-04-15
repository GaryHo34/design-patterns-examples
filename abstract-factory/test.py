import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'AbstractFactory.java'])
subprocess.call(['java', 'AbstractFactory'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'AbstractFactory.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'AbstractFactory.cpp', '-o', 'AbstractFactory'])
subprocess.call(['./AbstractFactory'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'AbstractFactory.ts'])
subprocess.call(['node', 'AbstractFactory.js'])

os.remove('AbstractFactory')
os.remove('AbstractFactory.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)