import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'Flyweight.java'])
subprocess.call(['java', 'Flyweight'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Flyweight.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Flyweight.cpp', '-o', 'Flyweight'])
subprocess.call(['./Flyweight'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Flyweight.ts', '--target', 'es6'])
subprocess.call(['node', 'Flyweight.js'])

os.remove('Flyweight')
os.remove('Flyweight.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)