import subprocess

print("####Test Java code####\n\n")
subprocess.call(['javac', 'SimpleFactory.java'])
subprocess.call(['java', 'SimpleFactory'])

print("####Test Python code####\n\n")
subprocess.call(['python3', 'SimpleFactory.py'])

print("####Test CPP code####\n\n")
subprocess.call(['g++','-std=c++17', 'SimpleFactory.cpp', '-o', 'SimpleFactory'])
subprocess.call(['./SimpleFactory'])

print("####Test TS code####\n\n")
subprocess.call(['tsc', 'SimpleFactory.ts'])
subprocess.call(['node', 'SimpleFactory.js'])
