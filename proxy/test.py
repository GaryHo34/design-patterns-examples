import subprocess
import glob
import os

print("####Test Java code####")
subprocess.call(['javac', 'Proxy.java'])
subprocess.call(['java', 'Proxy'])

print("\n\n####Test Python code####")
subprocess.call(['python3', 'Proxy.py'])

print("\n\n####Test CPP code####")
subprocess.call(['g++','-std=c++17', 'Proxy.cpp', '-o', 'Proxy'])
subprocess.call(['./Proxy'])

print("\n\n####Test TS code####")
subprocess.call(['tsc', 'Proxy.ts'])
subprocess.call(['node', 'Proxy.js'])

os.remove('Proxy')
os.remove('Proxy.js')
for fl in glob.glob("*.class"):
    #Do what you want with the file
    os.remove(fl)