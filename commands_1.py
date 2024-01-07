#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of commands
    these seem to be mostly for working with the
        system
        files
        python setup

"""
#---- tof --------

#     ----- main put this at top of each app file:
if __name__ == "__main__":
    import main
    main.main()
# ------------------------------------------

import sys
import tkinter as Tk


#----- local imports
import commands_0
from   app_global import AppGlobal

#import gui_ext
import sync_combo
import gui


# ============================================
class CommandTest_1( commands_0.CommandABC ):
    """
    just a test command
    revise to try a 2d version of 3d sync
    base on pip
    """
    def __init__( self,     ):
        """
        usual init

        """
        super().__init__()
        #rint( super().name )   # ng not sure why
        #super().__init__( )
        #CommandABC.__init__( self )
        self.name             = "CommandTest_1 test cmd command"
        self.key_words        = [ "test",  "testing", "key", "word",]

        self.info             = "This is a test command which\n"
        self.info             = f"{self.info}may do something or nothing\n"
        self.info             = f"{self.info}the Linux command is variable\n"

        self.cmd_fixed        = "base # with comment "
        self.command_help     = "http://bulldog/mediawiki/index.php/Linux_CheatSheet#Ports_Serial_and_..."
        self.cmd_fixed        = None

    # ----------------------------------
    def build_gui_frame( self, parent ):
        """
        return a frame
        """
        # ---- build the widget manager
        a_sync_combo       = sync_combo.SyncCombo()
        self.a_sync_combo  = a_sync_combo
        a_sync_combo.set_label_text( "Command", "Source", "Target", )
        # ---- make the drop down values -- here with values that are tracable
        arg_1 = "z"

        arg_2       =  "ls -a -h -l              # list files"

        arg_3       = ["                         # unneded to list all ",
                       "*.py                     # python files"
                       " | grep                  # grep to limit output",
                       ]

        # ------------------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,   # key 0
                                  arg_2,           # key 1
                                  arg_3 )

        # -------------+-------------------------+-------
        arg_2       =  "nemo                     # launch nemo gui file manager"
        arg_3       = ["                         # ??? ",

                       ]

        a_sync_combo.add_to_dict( arg_1,   # key 0
                                 arg_2,           # key 1
                                 arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "<nautilus>               # launch nautilus gui file manager"
        # -------------+-------------------------+-------
        arg_3       = ["                         #  typically nothing  ",

                       ]

        a_sync_combo.add_to_dict( arg_1,   # key 0
                                 arg_2,           # key 1
                                 arg_3 )

        # --------
        arg_2       =  "<pip> show               #  "

        arg_3       = ["{something to show? }    #  ",

                       ]

        a_sync_combo.add_to_dict( arg_1,   # key 0
                                 arg_2,           # key 1
                                 arg_3 )

        # --------
        arg_2       =  "{whatever_you_want}      # arg_1 anything that works"
        arg_3       = ["{whatever_you_want}      # anything that works",
                       ]

        a_sync_combo.add_to_dict( arg_1,   # key 0
                                 arg_2,           # key 1
                                 arg_3 )

        a_sync_combo.arg_width   = gui.ARG_WIDTH

        a_frame = self.build_gui_3d_frame_from_args(
                                       parent,
                                       a_sync_combo     = a_sync_combo,
                                       command_str      = None,
                                       short_desc       = None,
                                       arg_1_label      = None,
                                       w_type_1         = None,
                                       arg_2_label      = "label for arg_2",
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
        may not be up to standards !!
        return none
        "ls; echo \'an echo\';ls ex_p*.*; bash ex_popen.sh;  exec bash"
        """
        print( "may not be done for new gui above look at command copy and adapt ")
        return  "test_1 does not meet standards to return a command "
        # get_3_args.( )   # all comes from self

# ============================================
class CommandLs( commands_0.CommandABC ):
    """
    ls command to list files

    """
    def __init__( self,     ):
        """
        usual init

        """
        super().__init__()
        #rint( "CommandLs.__init__()"  )
        self.name             = "CommandLs ls list files dir directory"

        self.build_key_words( self.name )

        self.command_string   = "ls"
        self.short_desc       = "ls -a -h -l >> list files () # arg_1 is protype for files to list "
        #self.shell_fn         = ""
        self.info             = "This will list the files in your current directory\n"
        self.info             = f"{self.info}or any other directory you specify\n"
        self.info             = f"{self.info}the Linux command is ls\n"

        self.set_py_env       = False   #  True  !! prob true for conda
        self.cmd_fixed        = "ls -a -h -l"

        self.command_help     =  "http://bulldog/mediawiki/index.php/Linux_CheatSheet#Files"

    # ----------------------------
    def build_gui_frame( self, parent ):
        """
        return a frame
        with the gui for this command
        see text help for more ?
        install                     Install packages.
        download                    Download packages.
        uninstall                   Uninstall packages.
        freeze                      Output installed packages in requirements format.
        list                        List installed packages.
        show                        Show information about installed packages.
        """

        # ---- build the widget manager
        a_sync_combo            = sync_combo.SyncCombo()
        a_sync_combo.set_label_text( "z", "Command:", "Command Arg:", )
        a_sync_combo.arg_width  = gui.ARG_WIDTH
        self.a_sync_combo       = a_sync_combo

        # -------------+-------------------------+-------
        typically_0 = ["                         # Typically none", ]
        arg_needed  = ["                         # Arg needed", ]
        # ---- make the drop down values -- here with values that are tracable
        arg_1       = "z"  # hidden single value

        # =============+-------------------------+-------
        arg_2       =  "ls -a -h -l              # list files"#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["                         # unneded to list all ",
                       "*.py                     # python files"
                       " | grep                  # grep to limit output",
                       ]

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "nemo                     # launch nemo gui file manager"#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["                         # ??? ",
                       ]

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "<nautilus>               # launch nautilus gui file manager"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "{whatever_you_want}      # arg_1 anything that works"#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["{whatever_you_want}      # anything that works",
                       ]

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # ---- build frame
        a_frame = self.build_gui_3d_frame_from_args(
                                       parent,
                                       a_sync_combo     = a_sync_combo,
                                       command_str      = None,
                                       short_desc       = None,
                                       arg_1_label      = "Command",
                                       w_type_1         = None,
                                       arg_2_label      = "Software Name",
                                       w_type_2         = None,   )

        AppGlobal.gui.gui_style.style_frame( a_frame )

        # Tk.DISABLED Tk.DISABLE  Tk.NORMAL
        AppGlobal.gui.button_browse_file_src.config( state = Tk.DISABLED )
        AppGlobal.gui.button_browse_file_dst.config( state = Tk.DISABLED )
        AppGlobal.gui.button_browse_dir_src.config(  state = Tk.DISABLED )
        AppGlobal.gui.button_browse_dir_dst.config(  state = Tk.DISABLED )

        if self.set_py_env:
            print( "do set_py_env")

        return a_frame

    # ----------------------------------
    def build_command( self, add_echo = True, add_newline = False ):
        """
        return a command as a single string
        "ls; echo \'an echo\';ls ex_p*.*; bash ex_popen.sh;  exec bash"

        """
        return self.build_command_1_2( add_echo = add_echo, add_newline = add_newline )

# ============================================
class CommandPip( commands_0.CommandABC ):
    """
    what it says

    """
    def __init__( self,     ):
        """
        usual init

        """
        super().__init__()

        self.name             = "CommandPip pip python install module setup"

        self.build_key_words( self.name )

        self.command_string   = "pip"
        self.short_desc       = "pip: install python module "
        self.shell_fn         = ""
        self.info             = "This will install a module for python\n"
        self.info             = f"{self.info}or any other directory you specify\n"
        self.info             = f"{self.info}the Linux command is xxxx\n"

        self.set_py_env       = False   #  True  !! prob true for conda

        self.cmd_fixed        = "pip"
        self.command_help     =  "http://bulldog/mediawiki/index.php/Python_CheatSheet#Pip"

    # ----------------------------
    def build_gui_frame( self, parent ):
        """
        return a frame
        with the gui for this command
        see text help for more ?
        install                     Install packages.
        download                    Download packages.
        uninstall                   Uninstall packages.
        freeze                      Output installed packages in requirements format.
        list                        List installed packages.
        show                        Show information about installed packages.
        """
        # ---- build the widget manager
        a_sync_combo            = sync_combo.SyncCombo()
        a_sync_combo.set_label_text( "z", "Command:", "Command Arg:", )
        a_sync_combo.arg_width  = gui.ARG_WIDTH
        self.a_sync_combo       = a_sync_combo

        # -------------+-------------------------+-------
        typically_0 = ["                         # Typically none", ]
        arg_needed  = ["                         # Arg needed", ]
        # ---- make the drop down values -- here with values that are tracable
        arg_1       =  "z"  # hidden single value
        # =============+-------------------------+-------
        arg_2       =  "<pip> list               # list installed packages"#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["                         # unneded to list all ",
                       " | grep                  # grep to limit output",
                       ]

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "<pip> install            # install a package"#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["{what_to_install}        # what to install ",
                       ]

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "<pip> download           #  "#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["                         # ??? ",
                       ]

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "<pip> config             #  "#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["{something to config? }  #  ",
                       ]

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "<pip> show               #  "#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["{something to show? }    #  ",
                       ]

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "{whatever_you_want}      # arg_1 anything that works"#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["{whatever_you_want}      # anything that works",
                       ]

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # ---- build frame
        a_frame = self.build_gui_3d_frame_from_args(
                                       parent,
                                       a_sync_combo     = a_sync_combo,
                                       command_str      = None,
                                       short_desc       = None,
                                       arg_1_label      = "Command",
                                       w_type_1         = None,
                                       arg_2_label      = "Software Name",
                                       w_type_2         = None,   )

        AppGlobal.gui.gui_style.style_frame( a_frame )

        # Tk.DISABLED Tk.DISABLE  Tk.NORMAL
        AppGlobal.gui.button_browse_file_src.config( state = Tk.DISABLED )
        AppGlobal.gui.button_browse_file_dst.config( state = Tk.DISABLED )
        AppGlobal.gui.button_browse_dir_src.config(  state = Tk.DISABLED )
        AppGlobal.gui.button_browse_dir_dst.config(  state = Tk.DISABLED )

        if self.set_py_env:
            print( "do set_py_env")

        return a_frame

    # ----------------------------------
    def build_command( self, add_echo = True, add_newline = False ):
        """
        return a command as a single string
        "ls; echo \'an echo\';ls ex_p*.*; bash ex_popen.sh;  exec bash"


        """
        args        = self.get_ddl_args()

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

        #rint( cmd_str )
        #rint( cmd_list )

        return cmd_str

# ============================================
class CommandConda( commands_0.CommandABC ):
    """

    what it says
    no sudo !!

    """
    def __init__( self,     ):
        """
        usual init

        """
        super().__init__()

        self.name             = "CommandConda conda python install module, enviroment"
        #key_words_str         = "conda python install module, enviroment"
        self.build_key_words( self.name )
        #rint( f"")

        self.command_string   = "ls"
        self.shell_fn         = ""
        self.info             = "This will install a module for python\n"
        self.info             = f"{self.info}or any other directory you specify\n"
        self.info             = f"{self.info}the Linux command is xxxx\n"
        self.set_py_env       = False   #  True  !! prob true for conda

        self.cmd_fixed        = "conda"
        self.command_help     =  "http://bulldog/mediawiki/index.php/Python_CheatSheet#Conda"

    # ----------------------------------
    def build_gui_frame( self, parent ):
        """
        return a frame
        with the gui for this command
        """
        # ---- build the widget manager
        a_sync_combo            = sync_combo.SyncCombo()
        a_sync_combo.set_label_text( "z", "Command:", "Command Arg:", )
        a_sync_combo.arg_width  = gui.ARG_WIDTH
        self.a_sync_combo       = a_sync_combo

        # -------------+-------------------------+-------
        typically_0 = ["                         # Typically none", ]
        # arg_needed  = ["                         # Arg needed", ]
        # ---- make the drop down values -- here with values that are tracable
        arg_1       = "z"  # hidden single value
        # =============+-------------------------+-------
        arg_2       =  "<conda> -V               # version of conda"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "<conda> info             # list environments based on arg 2"#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["--envs                   # list enviroments",
                       "--*                      # current environments",
                       ]

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "<conda> activate         # conda activate environment_name"#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["{environment_name}       # environment name",
                       "base                     # base environment",
                       ]

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "<conda> remove -n        # conda remove -n environment_name"#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["{environment_name}       # environment name",
                       "                         # blank for you to fill ",
                       ]

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # ---- build frame
        a_frame = self.build_gui_3d_frame_from_args(
                                       parent,
                                       a_sync_combo     = a_sync_combo,
                                       command_str      = None,
                                       short_desc       = None,
                                       arg_1_label      = "Command",
                                       w_type_1         = None,
                                       arg_2_label      = "Software Name",
                                       w_type_2         = None,   )

        AppGlobal.gui.gui_style.style_frame( a_frame )

        # Tk.DISABLED Tk.DISABLE  Tk.NORMAL
        AppGlobal.gui.button_browse_file_src.config( state = Tk.DISABLED )
        AppGlobal.gui.button_browse_file_dst.config( state = Tk.DISABLED )
        AppGlobal.gui.button_browse_dir_src.config(  state = Tk.DISABLED )
        AppGlobal.gui.button_browse_dir_dst.config(  state = Tk.DISABLED )

        if self.set_py_env:
            print( "do set_py_env")

        return a_frame

    # ----------------------------------
    def build_command( self, add_echo = True, add_newline = False ):
        """
        return a command as a single string
        add_echo    see code
        add_newline   see code

        """
        return self.build_command_1_2( add_echo = add_echo, add_newline = add_newline )

# ============================================
class CommandSysCtrl( commands_0.CommandABC ):
    """
    what it says
    need to work in sudo for some commands

    """
    def __init__( self,     ):
        """
        usual init
        systemctl to list services on systemd Linux ...
        """
        super().__init__()

        self.name             = "CommandSysCtrl systemctl system control start stop  ctl reload"
        #key_words_str         = "system control start stop systemctl ctl reload"
        self.build_key_words( self.name )

        self.command_string   = "systemctl"
        self.shell_fn         = ""
        self.info             = "Use this to control system services \n"
       # self.info             = f"{self.info}or any other directory you specify\n"
       # self.info             = f"{self.info}the Linux command is xxxx\n"
        self.set_py_env       = False

    # ----------------------------------
    def build_gui_frame( self, parent ):
        """
        return a frame
        """
        # ---- build the widget manager
        a_sync_combo            = sync_combo.SyncCombo()
        a_sync_combo.set_label_text( "z", "Command:", "Command Arg:", )
        a_sync_combo.arg_width  = gui.ARG_WIDTH
        self.a_sync_combo       = a_sync_combo

        # -------------+-------------------------+-------
        # typically_0 = ["                         # Typically none", ]
        # arg_needed  = ["                         # Arg needed", ]
        # ---- make the drop down values -- here with values that are tracable
        arg_1         = "z"  # hidden single value
        # f"{sudo}systemctl {arg_1} {arg_2}",
         # values  = [ "list-units --type=service", "list-units",
         #            "start", "stop", "reload", "status", "cat", ]
         # self.arg_1_widget.configure( values = values )
         # #self.arg_1_var.set( "install")
         # self.arg_1_var.set( values[ 0 ])

         # values  = [ "", "some service name" ]

        # =============+-------------------------+-------
        arg_2       =  "sudo systemctl"#no  , !
        # -------------+-------------------------+-------
        arg_3       = [ "list-units --type=service", "list-units",
                        "start", "stop", "reload", "status", "cat", ]

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "sudo systemctl start    # Start a service "#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["{what_to_start}          # what to start ",
                       ]

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "sudo systemctl stop     # Stop a service "#no  , !
        # -------------+-------------------------+-------
        arg_3       = "{what_to_stop}            # what to start "

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "sudo systemctl reload     # Reload a service "#no  , !
        # -------------+-------------------------+-------
        arg_3       = "{what_to_reload}            # what to reload "

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # ---- build frame
        a_frame = self.build_gui_3d_frame_from_args(
                                       parent,
                                       a_sync_combo     = a_sync_combo,
                                       command_str      = None,
                                       short_desc       = None,
                                       arg_1_label      = "Command",
                                       w_type_1         = None,
                                       arg_2_label      = "Software Name",
                                       w_type_2         = None,   )

        AppGlobal.gui.gui_style.style_frame( a_frame )

        # Tk.DISABLED Tk.DISABLE  Tk.NORMAL
        AppGlobal.gui.button_browse_file_src.config( state = Tk.DISABLED )
        AppGlobal.gui.button_browse_file_dst.config( state = Tk.DISABLED )
        AppGlobal.gui.button_browse_dir_src.config(  state = Tk.DISABLED )
        AppGlobal.gui.button_browse_dir_dst.config(  state = Tk.DISABLED )

        if self.set_py_env:
            print( "do set_py_env")

        return a_frame

    # ----------------------------------
    def build_command( self, add_echo = True, add_newline = False ):
        """
        return a command as a single string
        add_echo    see code
        add_newline   see code

        """
        return self.build_command_1_2( add_echo = add_echo, add_newline = add_newline )

# ============================================
class CommandCopy( commands_0.CommandABC ):
    """
    what it says

    plus a bunch of similiar commands at least for now
    use triple dropdowns, at least for now
    """
    def __init__( self,     ):
        """
        usual init
        copy argumen1 argument 2

        """
        super().__init__()
        #rint( "CommandCopy.__init__()"  )
        self.name             = "CommandCopy cp copy mv move rename del delete Files nemo"
        self.build_key_words( self.name )   # must be here after rest of init

        self.cmd_list          = None
            # put in build cmd with fstring ..!! local variable should be fine

        self.shell_fn         = ""
        self.info             = "This will copy file from one place to another\n"
        self.info             = f"{self.info}additionaly you can move files\n"
        self.info             = f"{self.info}or you can use a GUI File Manager\n"
        self.web_ref          = r"http://bulldog/mediawiki/index.php/Linux_CheatSheet#copy_files"
        self.info             = f"{self.info}the Linux command is xxxx\n"
        self.set_py_env       = False   #  True  !! prob true for conda

        self.cmd_fixed        = "cp     # copf from source to destination "
        self.command_help     = "http://bulldog/mediawiki/index.php/Python_CheatSheet#what"

    # ----------------------------------
    def build_gui_frame( self, parent ):
        """
        return a frame
        with the gui for this command
        """

        arg_width  = 100

        # ---- build the widget manager
        a_sync_combo             = sync_combo.SyncCombo()
        a_sync_combo.arg_width   = gui.ARG_WIDTH
        a_sync_combo.set_label_text( "Command:", "Source:", "Target:", )
        self.a_sync_combo        = a_sync_combo

        # ------------------------+-------------------------+-------
        a_file_name            = ["                         # A file name", ]
        # ---- make the drop down values -- here with values that are tracable
        # ------------------------+-------------------------+-------
        a_sync_combo.add_to_dict( "cp                       # copy cmd {source} {dest}",   # key 0
                                  "                         # source file name",           # key 1
                                [ "                         # dest file name",             # key3


                                  ] )
        # ------------------------+-------------------------+-------
        a_sync_combo.add_to_dict( "mv                       # move cmd {source} {dest}",   # key 0
                                  "                         # source file name",           # key 1
                                [ "                         # dest file name",             # key3
                                 ] )
        # ------------------------+-------------------------+-------
        a_sync_combo.add_to_dict( "del                      # delete cmd {source} {dest}",   # key 0
                                  "                         # target file name",           # key 1
                                [ "                         # usually blank",             # key3

                                  ] )
        # ------------------------+-------------------------+-------
        # ------------------------+-------------------------+-------
        a_sync_combo.add_to_dict( "nemo                     # launch gui _> file manager",   # key 0
                                  "                         # usually blank",              # key 1
                                [ "                         # usually blank",             # key3

                                  ] )


        arg_1        = "sudo chmod               # Change file mode"
        # =============+-------------------------+-------
        arg_2      =   "755                      # Make executable"#no
        # -------------+-------------------------+-------
        arg_3          = a_file_name

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2      =   "                         # Enter a mode#"#no
        # -------------+-------------------------+-------
        arg_3       = a_file_name

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        a_frame = self.build_gui_3d_frame_from_args(
                                       parent,
                                       a_sync_combo     = a_sync_combo,
                                       command_str      = None,
                                       short_desc       = None,
                                       arg_1_label      = None,
                                       w_type_1         = None,
                                       arg_2_label      = "label for arg_2",
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
        return a command as a single string
        "ls; echo \'an echo\';ls ex_p*.*; bash ex_popen.sh;  exec bash"
        """
        args = self.a_sync_combo.get_3_args()

        #rint( f"build_command args {args}")

        cmd_prefix  = self.build_prefix()


        cmd_list    = cmd_prefix + [ f"{args[0]} {args[1]} {args[2]}",
                                     "exec bash",
                                     ]

        if add_echo:
            cmd_list    = self.build_echo( cmd_list )

        if add_newline:
            cmd_str     = "\n".join( cmd_list )   # may still want to stip exec bash  !!

        else:
            cmd_str     = ";".join( cmd_list )
            cmd_str     = f'gnome-terminal -- bash -c "{cmd_str}"'

        #rint( cmd_str )
        #rint( cmd_list )

        return cmd_str

# ============================================
class CommandApt( commands_0.CommandABC ):
    """
    what it says

    """
    def __init__( self,     ):
        """
        usual init
        """
        super().__init__()
        self.name             = "CommandApt apt get install program"
        self.build_key_words( self.name )
        self.command_string   = "apt"
        self.short_desc       = "apt -> install programs"
        self.shell_fn         = ""
        self.info             = "This will install a module for linux\n"
        self.info             = f"{self.info}or any other directory you specify\n"
        self.info             = f"{self.info}the Linux command is xxxx\n"

    # ----------------------------------
    def build_gui_frame( self, parent ):
        """
        return a frame
        sudo apt update        # Fetches the list of available updates
        sudo apt upgrade       # Installs some updates; does not remove packages
        sudo apt full-upgrade  # Installs updates; may also remove some packages, if needed
        sudo apt autoremove    # Removes any old packages that are no longer needed

        """
        # ---- build the widget manager
        a_sync_combo             = sync_combo.SyncCombo()
        a_sync_combo.arg_width   = gui.ARG_WIDTH
        a_sync_combo.set_label_text( "z", "Command:", "Command Arg:", )
        self.a_sync_combo  = a_sync_combo

        # -------------+-------------------------+-------
        a_file_list = ["/etc/hosts               # identify other machines",
                       "/what                    # place holder",
                       "/why                     # place holder",
                       ]

        # ---- make the drop down values -- here with values that are tracable
        arg_1       =  "z"
        # -------------+-------------------------+-------
        arg_2       =  "sudo apt update          # Fetches the list of available updates"#no  , !
        arg_3       = a_file_list
        # -------------+-------------------------+-------
        arg_3       = ["                         #  typically nothing  ",
                       ]

        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,   # key 0
                                  arg_2,           # key 1
                                  arg_3 )

        # =====
        # -------------+-------------------------+-------
        arg_2       =  "sudo apt upgrade         # Installs some updates; does not remove packages"#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["                         #  typically nothing  ",
                       ]
        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,   # key 0
                                  arg_2,           # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "sudo apt full-upgrade    # Installs updates; may also remove some packages, if needed"#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["                         #  typically nothing  ",
                       ]

        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =====
        # -------------+-------------------------+-------
        arg_2       =  "sudo apt autoremove      # Removes any old packages that are no longer needed"#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["                         #  typically nothing  ",
                       ]

        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =====
        # -------------+-------------------------+-------
        arg_2       =  "sudo apt install         # Install some software"#no  , !
        # -------------+-------------------------+-------
        arg_3       = ["                         # Name of software to install",
                       ]

        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        a_frame = self.build_gui_3d_frame_from_args(
                                       parent,
                                       a_sync_combo     = a_sync_combo,
                                       command_str      = None,
                                       short_desc       = None,
                                       arg_1_label      = "Command",
                                       w_type_1         = None,
                                       arg_2_label      = "Software Name",
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
        return a command as a single string
        "ls; echo \'an echo\';ls ex_p*.*; bash ex_popen.sh;  exec bash"
        """
        args = self.a_sync_combo.get_3_args()
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

        #rint( cmd_str )
        #rint( cmd_list )

        return cmd_str



# ---- eof =================== eof ==============================

