import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'Strategy.java'])
subprocess.call(['java', 'Strategy'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Strategy.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Strategy.cpp', '-o', 'Strategy'])
subprocess.call(['./Strategy'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Strategy.ts'])
subprocess.call(['node', 'Strategy.js'])

os.remove('Strategy')
os.remove('Strategy.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)