import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'Bridge.java'])
subprocess.call(['java', 'Bridge'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Bridge.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Bridge.cpp', '-o', 'Bridge'])
subprocess.call(['./Bridge'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Bridge.ts'])
subprocess.call(['node', 'Bridge.js'])

os.remove('Bridge')
os.remove('Bridge.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)