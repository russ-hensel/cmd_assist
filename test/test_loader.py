# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:59:38 2020

@author: russ
"""






def do_prep( a_pi ):

        a_pi.my_data[ "loader_1"]    =   [ "where_1",     "who",     "p . ( 0 0 ) ",          "ng so far"]
        a_pi.my_data[ "loader_2"]    =   [ "where_2",     "me",      "my_secrets",             "comment" ]



class PiPi( object ):
    """
    build commands from gui fragments,
    called from time to time
    uses reference to gui and get and sets to update the
    gui with the current assembled command


    """
    # ----------------------------------------
    def __init__(self, ):

        self.my_data  = {}
        do_prep( self )

    def print_it( self, ):
        print( self.my_data )


def main( ):
    a_pi_pi   = PiPi()
    a_pi_pi.print_it()


# ----------------------------------------
if __name__ == "__main__":
    #----- run the full app
    #import cmd_assist
    main()