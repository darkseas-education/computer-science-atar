#!/usr/bin/env python
"""
Module:      dodo.py
Description: Automated tasks by python doit
Author:      Gavin Coombes
Date:        20 December 2023

"""
# Imports

# Constants

# Functions
def task_build():
    _dir = "."
    actions = [f'jb build {_dir}']
    return {
        'actions': actions,
        'verbosity': 2,
    }

def task_lab():
    actions = ['jupyter lab']
    return {
        'actions': actions,
        'verbosity': 2
    }

# Classes

# Tests

if __name__ == "__main__":

    

    print("__done__")
 
