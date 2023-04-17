import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'Singleton.java'])
subprocess.call(['java', 'Singleton'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Singleton.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Singleton.cpp', '-o', 'Singleton'])
subprocess.call(['./Singleton'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Singleton.ts'])
subprocess.call(['node', 'Singleton.js'])

os.remove('Singleton')
os.remove('Singleton.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)