# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 20:47:16 2020

keep generic ref to each tab here using the same name across
tabs so we can use generic names to de reference.
also keep the getters and setters her
so far this is an expereiment ... will need refactoring

tab_value_obj


"""

import os

import subprocess
from   subprocess import run
from   subprocess import Popen, PIPE, STDOUT
import tkinter as Tk

# local
from   app_global import AppGlobal

# ----------------------------------------------
class AdamTabValues( object ):
    """
    extend to hold commands as well, extend for each tab page .... then perhaps
    it should hold the create gui as well  and be called with
    make and save? the create gui.
    as in adam and eve
    this is first experiment, should probably be ancestor and something lighter here
    one of these may work for all.... maybe gui constructor here as well ... subclass as necessary
    references to the install tab
    values mostly injected from the gui -- at least so far
    where how to ref in gui as self.install_tab_value or in AppGlobal... for now in gui
    ?? build stuff here as well ??
    not all will apply to all subclasses but that is ok
    to_str might blow .... depends on how written, no methods on None
    so associate with each tab, prehaps shouls have extended tabl


    not clear how command and action differ


    """
    # ----------------------------------------
    def __init__(self, ):

        self.cmd_ok             = None       # set if command is computed to ccomand_widget
        self.cmd_widget         = None
        self.dest_file_widget   = None
        self.src_file_widget    = None
        self.op_widget          = None       # operation in words
        self.op_button          = None       # button widget
        self.dst_path_widget    = None
        self.src_path_widget    = None
        self.op_flag_widget     = None
        self.cc_widget          = None       # list of common commands

        self.what_widget          = None       # third in mode action ( the what )

        self.tabp_title         = "implement me"   # title on the tab page
        self.mode_widget        = None
        self.action_widget      = None
        self.action_parm_widget = None

        self.prior_action       = None
        self.prior_action_parm  = None
        self.prior_dst_path     = None
        self.prior_src_path     = None

        self.ccommand_widget    = None    # computed command widget -- or use entered
        self.cmd_widget         = None    # how different from above

        self.prior_mode         = None      # for mode changes
        msg    = f"prior mode set {self.prior_mode}"
        print( msg )

        self.last_cmd           = None        # save last command so we do not over refresh
        # plus getters setters below
        self.tabp_help_fn       = "default.txt"   # set in each
        self.shell_fn           = "cmd_assist.sh"  # file name for shell script  in linux

        self.cmd_do_method       = None   # function to do the command
        self.cmd_show_method     = None   # function to show the command
        self.cmd_check_method    = None   #
        # next are argument for above see show_it and do_it
        self.cmd_data            = None   # data for the function argument more or less
        self.cmd_title           = None



    # # ---------------------------------
    # def do_it( self, ):   # or do the command from some button
    #     msg = "do it called but not implementd"
    #     raise NotImplementedError(  msg )

    # ---------------------------------
    def polling( self, ):   # for the polling of the tab
        """
        this is abstract implemet in child
        """
        msg = "tab_value_obj called for polling but not implementd as in abstract look in child"
        print( msg )
        raise NotImplementedError(  msg )


    # ---------------------------------
    def to_str( self, ):
        ret  = ""
        ret  = f"{ret}   xxxxx {self.cmd_widget}"
        ret  = f"{ret}   tab_title {self.tab_title}"

    # ---------------------------------
    def get_required_what( self, ):
        ret  = self.what
        if self.what == "":
            msg = "for this command you need a 'what'"
            AppGlobal.gui.write_gui( msg  )
            return ""
        else:
            return ret


    # ---------------------------------
    @property
    def cc_cmd( self ):
        ret    =   self.cc_widget.get()
        if ret != "":
            splits  = ret.split( "|" )
            ret     = splits[0]
        return ret

    # ---------------------------------
    @cc_cmd.setter   # looks like you should make a getter befor using a setter
    def cc_cmd( self,  arg ):
        """
        what it says !! may have to set to normal
        """
        #print( " set  list_cmd" )
        #self.list_cmd_widget.set( arg )    # does not work for entry widget
        self.cc_widget.delete(0, Tk.END)
        self.cc_widget.insert(0, arg )

    # ---------------------------------
    @property
    def action( self ):
        ret    = self.action_widget.get()

        #msg    = f"property mode returning {ret}"
        #rint( msg )

        return ret

    # ---------------------------------
    @property
    def action_parm( self ):
        ret    = self.action_parm_widget.get()

        #msg    = f"property mode returning {ret}"
        #rint( msg )

        return ret

    # ---------------------------------
    @property
    def what( self ):
        ret    = self.what_widget.get()
        ret    = ret.strip()
        #msg    = f"property mode returning {ret}"
        #rint( msg )

        return ret

    # ---------------------------------
    @property
    def mode( self ):
        ret    = self.mode_widget.get()

        #msg    = f"property mode returning {ret}"
        #rint( msg )

        return ret

    # ---------------------------------
    @property
    def cmd( self ):
        """
        !! use of none here is a kluge, need to eval this control?



        """
        if self.cmd_widget is None:
            return ""
        ret    = self.cmd_widget.get()
        return ret

    # ---------------------------------
    @cmd.setter   # looks like you should make a getter befor using a setter
    def cmd( self,  arg ):
        """
        what it says !! may have to set to normal
        """
        if self.cmd_widget is None:
            return
        #print( " set  list_cmd" )
        #self.list_cmd_widget.set( arg )    # does not work for entry widget
        self.cmd_widget.delete(0, Tk.END)
        self.cmd_widget.insert(0, arg )

    # ---------------------------------
    @property    # under f for file
    def dst_filexx( self ):
        """
        using path only for now



        """
        ret    =   self.dst_file_widget.get()
        return ret

    # ---------------------------------
    @property    # under f for file
    def src_filexx( self ):
        ret    = self.src_file_widget.get()
        return ret

    # ---------------------------------
    @property    # under p for path
    def dst_path( self ):
        ret    = self.dst_path_widget.get()

        msg = f"get dst_path = >{ret}<"
        return ret

    # ---------------------------------
    @dst_path.setter   # looks like you should make a getter befor using a setter
    def dst_path( self,  arg ):
        """
        what it says !! may have to set to normal
        """
        if self.dst_path_widget is None:
            return
        #print( " set  list_cmd" )
        #self.list_cmd_widget.set( arg )    # does not work for entry widget
        self.dst_path_widget.delete(0, Tk.END)
        self.dst_path_widget.insert(0, arg )

    # ---------------------------------
    @property    # under f for file
    def src_path( self ):

        ret    = self.src_path_widget.get()
        #msg = f"get src_path via property = >{ret}<"
        #print( msg )
        return ret

    # ---------------------------------
    @src_path.setter   # looks like you should make a getter befor using a setter
    def src_path( self,  arg ):
        """
        what it says !! may have to set to normal
        """
        if self.src_path_widget is None:
            return
        #print( " set  list_cmd" )
        #self.list_cmd_widget.set( arg )    # does not work for entry widget
        self.src_path_widget.delete(0, Tk.END)
        self.src_path_widget.insert(0, arg )


    # ---------------------------------
    @property
    def op( self ):
        ret    = self.op_widget.get()
        return ret

    # ---------------------------------
    @property
    def op_button_text( self ):
        #print( "get list_op_button_text  ")
        ret    = self.op_button.cget( "text" )

        return ret

    # ---------------------------------
    @op_button_text.setter   # looks like you should make a getter befor using a setter
    def op_button_text( self,  arg ):
        """
        what it says
        """
        #print( f"set list_opt_button_text with {arg}")
        self.op_button.config( text = arg  )

# self.copy_src_path_widget  = a_widget

    # ---------------------------------
    @property
    def ccommand_widget_text( self ):
        """
        what is ccomand ??  cmd seems to be the one
        """
        #print( "get list_op_button_text  ")
        ret    = self.ccommand_widget.get(  )

        return ret

    # ---------------------------------
    @ccommand_widget_text.setter   # looks like you should make a getter befor using a setter
    def ccommand_widget_text( self,  arg ):
        """
        what it says
        """
        #print( f"set list_opt_button_text with {arg}")


        # self.copy_src_path_widget  = a_widget
        widget   = self.ccommand_widget
        widget.delete(0, Tk.END)
        widget.insert(0, arg )


    # ---------------------------------
    def show_tab_help( self, ):
        """
        use code from twitter reports
        note we need to use self.tabp_help_fn  this has to have no arguments

        """
        # this for display in gui, right now open in text file
        # def display_help( self  ):
        # """
        # user interaction:
        # display help for this report
        # """
        # AppGlobal.gui.do_clear_button( "dummy_event")
        # with open( self.help_file, "r" ) as a_file:
        #     lines = a_file.readlines()
        #     # print( lines )
        #     msg  = "".join( lines )
        #     AppGlobal.gui.display_info_string( msg )
        # return

        full_fn    = AppGlobal.parameters.help_path +  self.tabp_help_fn
        #rint( full_fn )
        AppGlobal.os_open_txt_file(  full_fn )

    # ---------------------------------
    # def do_or_show_cmd_shell( self, it, title = None, do = True ):
    #     """
    #     Purpose: dispatch to correct method based on arguments
    #     arg:   it   what is to be done, string for a command
    #                 list for a shell script

    #     title:  title to assist the user

    #     """

    #     if isinstance( it, list ):
    #         if do:
    #             self.do_as_shell( it, title )
    #         else:
    #             self.show_as_shell( it, title )
    #     else:
    #         if do:
    #             self.do_as_cmd( it, title )
    #         else:
    #             self.show_as_cmd( it, title )

   # ---------------------------------
    def do_it( self, ):
        """
        do command, get arguments for it from this object
        will edit and show first so may not get to  the do method
        """
        msg    = f"in do_it >{self.cmd_do_method}< cmd_data: >{self.cmd_data}<"
        print( msg )
        if self.show_it():

            self.cmd_do_method(   )
        else:
            pass # error in parms

   # ---------------------------------
    def show_it( self, ):
        """
        this will show the command
        and perhaps prepare it as in writing the shell fiel

        """
        msg    = f"in show_it next call {self.cmd_show_method} cmd_data: >{self.cmd_data}<"
        print( msg )
        if self.check_it():
            self.cmd_show_method(   )
            return True
        else:
            return False

   # ---------------------------------
    def check_it( self, ):
        """
        this will check if parms are ok

        """
        msg    = f"in check_it next call {self.cmd_check_method} cmd_data: >{self.cmd_data}<"
        print( msg )
        return self.cmd_check_method( )  # cannot detach from gui so easily

    # ---------------------------------
    def do_as_cmd( self,    ):
        """
        run single line command with popen and capture output
        blocks
        we have pulled out arguments from object so this might be static
        """

        self.show_as_cmd(  ) # just for sure

        po     = subprocess.Popen(  [ self.cmd_data ], shell=True,  stdout = subprocess.PIPE )

        stdout_stuff, stderr_stuff    = po.communicate( input=None, ) # python 3 timeout=None )

        print( stdout_stuff )
        stdout_stuff = stdout_stuff.decode('utf-8')
        AppGlobal.gui.write_gui_wt( "Shell script gives:", stdout_stuff )

    # ---------------------------------
    def show_as_cmd( self,    ):
        """
        show the command -- how see code
        """
        msg = f"in show_as_cmd >{self.cmd_data}<"
        print( msg )
        AppGlobal.gui.write_gui_wt( "Cmd is:", self.cmd_data )


    # ---------------------------------
    def do_as_shell( self,   ):
        """
        runt as a shell script

        """
        self.write_shell_file(   )
        self.show_shell_file()

    # ---------------------------------
    def show_as_shell( self,   ):
        """
        this 2 step is not really required !!

        """
        pass
        self.write_shell_file( self.cmd_data )
        self.show_shell_file()

    # ---------------------------------
    def do_as_cmdline( self,   ):
        """
        run using -- see code
        """

        os.system( self.cmd_data )
        print( "waiting or not ")

    # ---------------------------------
    def show_as_cmdline( self,   ):
        """
        show using -- see code
        """
        msg = f"in show_as_cmdline >{self.cmd_data}"
        AppGlobal.gui.write_gui_wt( "Cmd is:", self.cmd_data )

    # ---------------------------------
    def write_shell_file( self,  ):
        """
        write lines out as a shell script
        can we do this in memory and execute same way
        """
        line_end   = "\n"
        msg        = f"write_shell_file {True}"
        print( msg )

        # file_lines   = [ "#!/bin/sh",
        #                  "ls",
        #                  "cd ~",
        #                  "ls" ]

        with open( self.shell_fn, "w" ) as a_file:

            i_line       = "#!/bin/sh"
            a_file.write( f"{i_line}{line_end}" )

            for i_line in self.cmd_data:
                a_file.write( f"{i_line}{line_end}" )

        msg    = f"done file write  {True}"
        print( msg )

     # ---------------------------------
    def show_shell_file( self,  ):
        """
        show lines out as a shell script


        """

        with open( self.shell_fn, "r" ) as a_file:
                lines = a_file.readlines()
                # print( lines )
                msg  = "".join( lines )
                AppGlobal.gui.write_gui_wt( "Shell script is:", msg )


            #full_fn    = AppGlobal.parameters.help_path +  self.tabp_help_fn
            #rint( full_fn )
        # or
        AppGlobal.os_open_txt_file(  self.shell_fn )
    # ---------------------------------
    def check_parms_ok( self ):
        """
        just a dummy, works for commands without arguments

        """
        return True


# all of rest is junk .... move
# ----------------------------------------------
class InstallTabValues( AdamTabValues ):
    """
    as in adam and eve
    this is first experiment, should probably be ancestor and something lighter here
    one of these may work for all.... maybe gui constructor here as well ... subclass as necessary
    references to the install tab
    values mostly injected from the gui -- at least so far
    where how to ref in gui as self.install_tab_value or in AppGlobal... for now in gui
    ?? build stuff here as well ??
    not all will apply to all subclasses but that is ok
    to_str might blow .... depends on how written, no methods on None
    """
    # ----------------------------------------
    def __init__(self, ):
        pass
        self.super( )  # hope this is how we do it

# ----------------------------------------------
class TestTabValues( AdamTabValues ):
    """
    as in adam and eve
    this is first experiment, should probably be ancestor and something lighter here
    one of these may work for all.... maybe gui constructor here as well ... subclass as necessary
    references to the install tab
    values mostly injected from the gui -- at least so far
    where how to ref in gui as self.install_tab_value or in AppGlobal... for now in gui
    ?? build stuff here as well ??
    not all will apply to all subclasses but that is ok
    to_str might blow .... depends on how written, no methods on None
    """
    # ----------------------------------------
    def __init__(self, ):
        pass
        self.super( )  # hope this is how we do it


# ----------------------------------------------
class CommonCmdTabValues( AdamTabValues ):
    """
    this is for common commands
    """
    # ----------------------------------------
    def __init__(self, ):
        pass
        super( )  # hope this is how we do it
        self.tab_title          = "Common Cmd"   # title on the tab

# ----------------------------------------------
if __name__ == "__main__":
    #----- run the full app
    import cmd_assist
    cmd_assist.main()












