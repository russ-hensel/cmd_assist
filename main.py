#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 21:02:33 2022

@author: russ
just to make main easy to find, also at
bottom of many files


"""
import sys
sys.path.append( "../rsh" )     # ok in win and linux but only for development
sys.path.append( "../rshlib" )     # ok in win and linux but only for development


def main( ):
    import cmd_assist
    cmd_assist.main()


# --------------------
if __name__ == "__main__":
    # #----- run the full app
    main( )


# # put this at top of each app file:
# # ---- main ------------------------------------------
# if __name__ == "__main__":
#     import main
#     main.main()

# ------------------------------------------




# =================== eof ==============================