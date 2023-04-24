import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'Template.java'])
subprocess.call(['java', 'Template'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Template.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Template.cpp', '-o', 'Template'])
subprocess.call(['./Template'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Template.ts'])
subprocess.call(['node', 'Template.js'])

os.remove('Template')
os.remove('Template.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)