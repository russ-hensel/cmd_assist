#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 22:24:14 2021

@author: russ
"""
# ============================================
class CommandSysCtrl( CommandABC ):
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

        self.name             = "CommandSysCtrl"
        self.key_words        = [ "system",  "control", "start", "stop", "systemctl", "ctl", "reload" ]
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
        #a_frame    = self.build_gui_frame_from_args( parent, arg_1_label= "conda1", arg_2_label = "conda2"   )
        a_frame    = self.build_gui_frame_from_args( parent, arg_1_label= "action", w_type_1 = "combo",  arg_2_label = "more", w_type_2 = "combo"  )

        values  = [ "list-units --type=service", "list-units", "start", "stop", "reload", "status", "cat", ]
        self.arg_1_widget.configure( values = values )
        #self.arg_1_var.set( "install")
        self.arg_1_var.set( values[ 0 ])

        values  = [ "", "some service name" ]
        self.arg_2_widget.configure( values = values )
        self.arg_2_var.set( values[ 0 ])

        AppGlobal.gui.button_browse_file_src.config( state = Tk.DISABLED )   # Tk.DISABLE  Tk.NORMAL
        AppGlobal.gui.button_browse_file_dst.config( state = Tk.NORMAL )
        AppGlobal.gui.button_browse_dir_src.config(  state = Tk.DISABLED )
        AppGlobal.gui.button_browse_dir_dst.config(  state = Tk.DISABLED )

        if self.set_py_env:
            pass
            print( "do set_py_env")

        return a_frame

    # ----------------------------------
    def build_command( self, add_echo = True, add_newline = False ):
        """
        return a command as a single string
        add_echo    see code
        add_newline   see code

        """
        arg_1       = self.arg_1_var.get()
        arg_2       = self.arg_2_var.get()

        if arg_1 in [  "start", "stop", "reload",   ]:
            sudo = "sudo "
        else:
            sudo = ""

        cmd_prefix  = self.build_prefix()

        #cmd_list    = cmd_prefix + [ "ls", "echo  'next >> ls ex_p\n'", "ls ex_p*.*",   "exec bash" ]
        cmd_list    = cmd_prefix + [ f"{sudo}systemctl {arg_1} {arg_2}",   "exec bash" ]

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

    # ----------------------------------
    def run_command( self,  ):
        """
        run command
        return ??
        """
        print( f"default_dir >>{self.get_default_dir()}<<" )

        full_cmd   = self.build_command()

        print( f"full_cmd   = {full_cmd}" )

        os.system( full_cmd  )
