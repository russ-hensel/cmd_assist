#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
this will with one parm run python programs in a conda env
import in commands.py  ... later make configurable


"""

# put this at top of each app file:
# ---- main ------------------------------------------
if __name__ == "__main__":
    import main
    main.main()

# ------------------------------------------

import tkinter as Tk

# ---- local
from   app_global import AppGlobal
import commands_0

import sync_combo
import gui

# ---- Outline me


# ============================================
class CommandRunPython( commands_0.CommandABC ):
    """
    what it says



    """
    def __init__( self,     ):
        """
        usual init

        sudo xed /etc/hosts
        """
        super().__init__()
        print( "CommandRunPython.__init__()"  )
        # ----------------------+---------------------+-------
        self.name             = "CommandRunPython      >>>>>>>>>>>>>>>work in procss run python testpython"
        self.build_key_words( self.name  )

        self.command_string   = "edit"
        self.short_desc       = "edit text files"

        self.info             = "This will edit text files\n"
        self.info             = f"{self.info}often used to make it executable\n"
        #self.info             = f"{self.info}......\n"
        self.web_ref          = r"http://bulldog/mediawiki/index.php/Linux_CheatSheet#copy_files"
        self.set_py_env       = False

        self.cmd_fixed        = "xed # name of editor in parameter.py"

    # ----------------------------------
    def build_gui_frame( self, parent ):
        """
        return a frame
        """
        # ---- build the widget manager
        a_sync_combo             = sync_combo.SyncCombo()
        a_sync_combo.arg_width   = gui.ARG_WIDTH
        a_sync_combo.set_label_text( "Command", "Source", "Target", )
        self.a_sync_combo        = a_sync_combo

        # looks like i am sharing file lists for now
        # -------------+-------------------------+-------
        # here a list of directories
        a_file_list = ["/mnt/WIN_D/Russ/0000/python00/python3/_projects/   # ",
                       "/mnt/WIN_D/Russ/0000/python00/python3/_projects/clipboard# home ",
                       "/home/russ/Desktop ",
                       "mnt/WIN_D/Russ/0000/python00/python3/_projects/clipboard #   " ,
                       "  # just a blank for you to optional fill",
                       ]



        # ---- make the drop down values -- here with values that are tracable
        arg_1       = "z"

        # ---- atom
        # -------------+-------------------------+-------
        arg_2       = "atom               #        "
        arg_3       = a_file_list
        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,           # key 0
                                  arg_2,           # key 1
                                  arg_3 )

        # ---- gedit
        # -------------+-------------------------+-------
        arg_2       =  "gedit               # optinally use sudo  may want to pick another editor"#no  , !
        arg_3       = a_file_list
        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,           # key 0
                                  arg_2,           # key 1
                                  arg_3 )

        # ---- xxx

        # ---- done for now
        a_frame = self.build_gui_3d_frame_from_args(
                                       parent,
                                       a_sync_combo     = a_sync_combo,
                                       command_str      = None,
                                       short_desc       = None,
                                       arg_1_label      = "Editor or File Manger",
                                       w_type_1         = None,
                                       arg_2_label      = "File Name",
                                       w_type_2         = None,   )

        AppGlobal.gui.gui_style.style_frame( a_frame )

        AppGlobal.gui.button_browse_file_src.config( state = Tk.DISABLED )   # Tk.DISABLE  Tk.NORMAL
        AppGlobal.gui.button_browse_file_dst.config( state = Tk.DISABLED )
        AppGlobal.gui.button_browse_dir_src.config(  state = Tk.DISABLED )
        AppGlobal.gui.button_browse_dir_dst.config(  state = Tk.DISABLED )

        if self.set_py_env:
            print( "do set_py_env")

        return a_frame

# ----------------------------------
    def build_command( self, add_echo = True, add_newline = False ):
        """
        for now lets see what we can get in
        local varabiles to later use in f_strings
        need to understand this
        """
        args        = self.get_ddl_args()
        print(  "<<<<<<<<<<<<<<<<<<<<<build_command" )
        print( f"    args          >>{args}<<  "  )
        # -----------+-------------+-----------------------

        arg_1   = self.get_arg_or_none( self.arg_1_var )
        arg_2   = self.get_arg_or_none( self.arg_2_var )
        print( f"    arg_1         >>{arg_1}<< arg_2    >>{arg_2}<<")
        # -----------+-------------+-----------------------

        a_dir      = AppGlobal.gui.get_default_dir()  # possible test for existance !!
        print( f"    a_dir         >{a_dir}<")
        # -----------+-------------+-----------------------

        #----- from build prefix
        set_py_env   = self.set_py_env
        print( f"    set_py_env    >{set_py_env}<")
        # -----------+-------------+-----------------------

        a_dir      = AppGlobal.gui.get_default_dir()  # possible test for existance !!
        print( f"    a_dir         >{a_dir}<")
        # -----------+-------------+-----------------------
        py_env_with = AppGlobal.parameters.py_env_with
        print( f"    py_env_with    >>{py_env_with}<< ")
        # -----------+-------------+-----------------------
        env    = AppGlobal.gui.python_env_var.get()
        print( f"    env           >>{env}<< ")
        # -----------+-------------+-----------------------
        # error on next
        # get_pass  = gui.sudo_pass_var.get( )
        # print( f"     get_pass    >>{get_pass}<< ")



        # cmd_prefix  = self.build_prefix()

        # cmd_list    = cmd_prefix + [ f"{args[1]} {args[2]}",
        #                              "exec bash",
        #                              ]

        # self.cmd_fixed
        # file_name  = AppGlobal.parameters.shell_file_name
        # if add_echo:
        #     cmd_list    = self.build_echo( cmd_list )

        # if add_newline:
        #     cmd_str     = "\n".join( cmd_list )   # may still want to stip exec bash  !!

        # else:
        #     cmd_str     = ";".join( cmd_list )
        #     cmd_str     = f'gnome-terminal -- bash -c "{cmd_str}"'

        # print( cmd_str )
        # print( cmd_list )
        # cmd_str
        return "see print"



    # ----------------------------------
    def build_command_old( self, add_echo = True, add_newline = False ):
        """
        return a command as a single string
        add_echo    see code
        add_newline   see code

        """
        args        = self.get_ddl_args()
        #rint( f"build_command args {args}")

        cmd_prefix  = self.build_prefix()

        cmd_list    = cmd_prefix + [ f"{args[1]} {args[2]}",
                                     "exec bash",
                                     ]

        if add_echo:
            cmd_list    = self.build_echo( cmd_list )

        if add_newline:
            cmd_str     = "\n".join( cmd_list )   # may still want to stip exec bash  !!

        else:
            cmd_str     = ";".join( cmd_list )
            cmd_str     = f'gnome-terminal -- bash -c "{cmd_str}"'

        print( cmd_str )
        print( cmd_list )

        return cmd_str






# ---- =================== eof ==============================

