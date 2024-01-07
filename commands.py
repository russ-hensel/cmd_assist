#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 21:28:47 2021

@author: russ

"""

# ---- main put this at top of each app file:
if __name__ == "__main__":
    import main
    main.main()
# ------------------------------------------

import sys

#from   tkinter import ttk

#----- local imports

#import build_cmd
#import os_values

# import here -- then use below --- change to make auto, how??
import commands_1
import commands_2
import commands_3
import commands_4
import commands_5

from   app_global import AppGlobal
# local
sys.path.append( "../rshlib" )     # ok in win and linux but only for development
import gui_ext
#import gui_ext

# ============================================
class CommandsDict(  ):
    """
    contains a dict and other
    """
    # ------------------------------------------
    def __init__( self,     ):
        """
        usual init

        """
        #rint( "CommandsDict.__init__()"  )

        # change to have items register themselves ??  still have to create them !
        self.dict    = {}

        self.make_dict_entry( commands_1.CommandLs() )
        self.make_dict_entry( commands_1.CommandTest_1() )
        self.make_dict_entry( commands_1.CommandPip() )
        self.make_dict_entry( commands_1.CommandConda() )
        self.make_dict_entry( commands_1.CommandSysCtrl() )
        self.make_dict_entry( commands_1.CommandApt() )
        self.make_dict_entry( commands_1.CommandCopy() )
        # self.make_dict_entry( commands_1.CommandChmod() )

        # ---- commands_2
        self.make_dict_entry( commands_2.CommandEditFile()   )
        self.make_dict_entry( commands_2.CommandMisc()       )
        self.make_dict_entry( commands_2.CommandHW()         )
        self.make_dict_entry( commands_2.CommandNamesPass()  )
        self.make_dict_entry( commands_2.CommandFind()       )

        # ---- commands_3
        self.make_dict_entry( commands_3.CommandNet()   )
        self.make_dict_entry( commands_3.CommandQemu()  )
        self.make_dict_entry( commands_3.CommandGrep()  )
        self.make_dict_entry( commands_3.CommandDmesg()  )


        # ---- commands_4
        self.make_dict_entry( commands_4.CommandEditFiles()   )
        self.make_dict_entry( commands_4.CommandManageFiles() )
        # self.make_dict_entry( commands_3.CommandQemu()   )
        self.make_dict_entry( commands_5.CommandRunPython()  )



        # self.make_dict_entry( commands_3.CommandGrep() )


    # ------------------------------------------
    def make_dict_entry( self,  a_command   ):
        """
        what it says read
        ?? may be obsolete or not
        """
        name      =    a_command.name.split()[0]
        self.dict[ name ] =  a_command
        return self.dict.keys()

        # ------------------------------------------
    def get_names( self,     ):
        """
        get the names of the commands as a list
        """
        return self.dict.keys()

    # ------------------------------------------
    def get_long_names( self, keys = None    ):
        """
        gets list of long names ... perhaps a comph ??
        keys   -> list of keys in the self.dict
        """
        names    = []
        if keys is None:
            keys = self.dict.keys()

        for i_key in  keys:
            i_name   = self.dict[i_key].name
            names.append( i_name  + " " )
        return names

    # ------------------------------------------
    def get_command_by_name( self,  name   ):
        """
        return the command associated with the name
        """
        #rint( f"\n\nname >>{name}<< for the dict >>{self.dict}<<" )
        #name    = name.split( " " )[0]
        #rint( f"name >>{name}<<" )
        try:  # or use get ??
            cmd    =  self.dict[name]
        except KeyError as ex:
            # Catch the custom exception
            print( f"get_command_by_name KeyError:    {ex}" ) #, f"arg.message  {arg.message}" )
            return None

        return self.dict[name]

    # ------------------------------------------
    def select_by_key_words( self,  key_words   ):
        """
        need shift to lc
        key_words -- key words to search for a list
        """

        print( f"key_words for search {key_words}" )
        key_words_output      = []
        # if last letter is an s, remove it
        for i_word in key_words:
            i_word = i_word.lower()
            if i_word == "":
                continue
            if i_word[ -1] == "s":   # need to strip search term as well or will loose match
                i_word = i_word[ : -1 ]
            key_words_output.append( i_word )

        # key_words    = key_words_output

        key_words    = set( key_words_output )
        #rint( f"key_words {key_words} and self.dict >>{self.dict}<<")

        if  key_words != set( [""] ):
            selected_names   = []
            for i_name in self.get_names():
                #rint( f"dict[i_name] >>{i_name}<< >>{self.dict[i_name]}<<"  )
                test_words   = set( self.dict[i_name].key_words )
                match_set    = key_words & test_words
                if key_words == match_set:
                    selected_names.append( i_name )
        else:
            # !! change to comphrension
            selected_names   = []
            for i_name in self.get_names():
                selected_names.append( i_name )

        #rint( f"selected_names{selected_names}")

        return selected_names

# # =================================================
# if __name__ == "__main__":

#     # ------------------------------------------

#     #----- run the full app
#     sys.path.append( "../rshlib" )     # ok in win and linux but only for development
#     import cmd_assist
#     cmd_assist.main()


# ----   eof ==============================

