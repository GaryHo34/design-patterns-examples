import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'Adapter.java'])
subprocess.call(['java', 'Adapter'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Adapter.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Adapter.cpp', '-o', 'Adapter'])
subprocess.call(['./Adapter'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Adapter.ts'])
subprocess.call(['node', 'Adapter.js'])

os.remove('Adapter')
os.remove('Adapter.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)