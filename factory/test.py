import subprocess
import glob
import os

print("####Test Java code####")
subprocess.run(['javac', 'Factory.java'])
p1 = subprocess.Popen(['java', 'Factory'])
p1.terminate()

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Factory.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Factory.cpp', '-o', 'Factory'])
subprocess.call(['./Factory'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Factory.ts'])
subprocess.call(['node', 'Factory.js'])

os.remove('Factory')
os.remove('Factory.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)