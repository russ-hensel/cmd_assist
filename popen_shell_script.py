#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 16:21:18 2020
for linux run a shell script, and capute output

python - Running shell command and capturing the output - Stack Overflow
https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output

@author: russ
"""
import subprocess
import os

# ----------------------------------------
def ex_run_shell_script():
    print( """
    ================ ex_run_shell_script():  blocking, captures output  ===============
    """ )

    # result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    # print( result.stdout )    # no \n visible

    # print( "\n================================\n")

    # result_str    = result.stdout.decode('utf-8')
    # print( result_str )   # much nicer output

    fn     = "popen_shell_script.sh"
    result = subprocess.run([f"./{fn}"], stdout=subprocess.PIPE)

    print( "\n==============run shell script ==================\n")

    result_str    = result.stdout.decode('utf-8')
    print( result_str )   # much nicer output

#ex_run_shell_script()     # works on bulldog

# ----------------------------------------
def ex_launch():
    print( """
    ================ ex_launch(): want no blocking,   ===============
    nautilus --new-window %U    %U seems to cause problem
    Depending on your requirements, os.system( cmdline ) might be the simples solution.
    """ )

    cmdline   =   "nautilus --new-window &"   # amper lets us detach
    os.system( cmdline )
    print( "waiting or not ")

ex_launch()    # works on bulldog, but blocks






