import subprocess

print("####Test Java code####")
subprocess.call(['javac', 'Factory.java'])
subprocess.call(['java', 'Factory'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Factory.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Factory.cpp', '-o', 'Factory'])
subprocess.call(['./Factory'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Factory.ts'])
subprocess.call(['node', 'Factory.js'])

subprocess.call(['rm', '-rf', '*.class', 'Factory', 'Factory.js'])