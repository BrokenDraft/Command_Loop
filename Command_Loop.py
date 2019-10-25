#!/usr/bin/env python2

## Import Library's

import sys
import os
import subprocess
import time

## Argv[] Check

if len(sys.argv) != 3 and len(sys.argv) != 4 :
    print ('Need 2 or 3 arguments : \n[line to start at]\n[command sheet]\n[time between commands] (Optional)')    exit()

## Initialisation

_start = sys.argv[1]
_sheet = sys.argv[2].strip()
_pwd = os.popen('pwd').read()
_counter = 1
_pwd = _pwd.strip()
_file_path = (_pwd + '/' + _sheet) #File Path

if len(sys.argv) == 4:
    _sec = sys.argv[3]
else:
    _sec = 0.3

## getting the sheet in a List

with open(_file_path) as f:
    _sheet = f.readlines()
_sheet = [x.strip() for x in _sheet]

## Def of Error_Handeling

def error_handeling(cmd, line):
    i = 0
    tmp2 = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, err = tmp2.communicate()
    #print(tmp2.returncode)
    while (i < 10 and err):
        tmp2 = subprocess.Popen(cmd , stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, err = tmp2.communicate()
        if output:
            with open("log_file", "a") as myfile:
                myfile.write(output)
        if err:
            print "______Error :", err.strip(), "______"
            with open("err_log", "a") as myfile:
                myfile.write(err)
        time.sleep(i)
        i += 1

    if i >= 10 and err:
        with open("err_log", "a") as myfile:
            myfile.write("\n10 failed attempt at line\n")
            myfile.write('{}'.format(line))
            myfile.write("\n\n")
        print "Waiting 10 minutes from :"
        subprocess.call('date')
        #exit()
        time.sleep(600)

## Main Loop

for x in _sheet:
    cmd = x + " | tee -a log_file"
    tmp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, err = tmp.communicate()
    if output:
        print(output.strip())
    if err:
        print(err.strip())
        with open("err_log", "a") as myfile:
            #myfile.write(err.strip())
            myfile.write("\n___At Line : ")
            myfile.write('{}'.format(_counter))
            myfile.write("___\n")
        error_handeling(x, _counter)
    time.sleep(float(_sec))
    _counter += 1