#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 11:16:57 2020

@author: russ


gui_venv.py


Plan:

    make an environment

    activate an environment

    open terminal, python or spyder in an environment

could make and run a bash script instead of
really having a terminal

for now just focus on command




"""

import tkinter as Tk
import logging
from   tkinter.filedialog import askopenfilename
#import  sys
from   tkinter import ttk
from   tkinter.scrolledtext import ScrolledText


# local
import tab_value_obj
from   gui import *      # because this file is just a continuation of gui, but in a different file
import gui_helper
import tab_value_obj
from   app_global import AppGlobal
# import parameters -- get from AppGlobal


# ------------------------------------------
def make_tabp( gui, parent_frame,  ):
    """
    a tab in its own file -- actually not a tab, but a factory for one -- name of tab in .py
    also should pack away some commands and values
    do we have place for this, is it in AdamTabValues

    each tabpage needs to set up its polling in build_cmd   tab_dispach_dict .... can we add dynamically from here
    polling eliminates actions on clicks....
    """

    self   = gui    # a trick to make it look like a instance method, and pretty much work like one
    #self.install_tab_values  = tab_values.InstallTabValues()

    my_control_obj     = TabpVenv()

    # test_tab_values    = tab_value_obj.AdamTabValues()   #  !!  fix unnecessary ref
    # tab_values         = test_tab_values # shorter faster ref

    a_frame          = Tk.Frame( parent_frame, bg = "gray" ,  borderwidth = 2, relief = "solid" )
    #a_frame.grid_columnconfigure( 0, weight = 1, ) # sticky = "uniform"    ) #sticky = Tk.W + Tk.E )
    a_frame.grid_columnconfigure( 0, weight=1, uniform="fred")
    a_frame.grid_columnconfigure( 1, weight=1, uniform="fred")
    a_frame.grid_columnconfigure( 2, weight=1, uniform="fred")
    a_frame.grid_columnconfigure( 3, weight=1, uniform="fred")

    ix_col  = 0
    ix_row  = 0

    # lables to define grid use for testing layout then delete
    a_widget = Tk.Label( a_frame, text = "1:",  anchor="w" ) #   relief = RAISED,  )
    a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W ) #rowspan = 2, columnspan = 2 )
    ix_col   += 1

    a_widget = Tk.Label( a_frame, text = "2:",  anchor="w" ) #   relief = RAISED,  )
    a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W ) #rowspan = 2, columnspan = 2 )
    ix_col   += 1

    # lables to define grid
    a_widget = Tk.Label( a_frame, text = "3:",  anchor="w" ) #   relief = RAISED,  )
    a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W ) #rowspan = 2, columnspan = 2 )
    ix_col   += 1

    a_widget = Tk.Label( a_frame, text = "4:",  anchor="w" ) #   relief = RAISED,  )
    a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W ) #rowspan = 2, columnspan = 2 )
    ix_col   += 1

    ix_col  = 0
    ix_row  += 1
    a_widget = Tk.Button( a_frame , width = 10, height = 1, text = "TabHelp" )
    self.copy_op_button  = a_widget
    # a_widget.config( command = foo )
    a_widget.grid( row = ix_row, column = ix_col, rowspan = 1, sticky = Tk.E + Tk.W + Tk.N + Tk.S )
    ix_col   +=  1

    #--- Mode
    ix_col  = 0
    ix_row  += 1
    a_widget = Tk.Label( a_frame, text = "Mode:",  anchor="w" ) #   relief = RAISED,  )
    a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W ) #rowspan = 2, columnspan = 2 )
    ix_col   += 1

    values        = [ "Venv Only" ]
    a_widget      = Tk.ttk.Combobox( a_frame, values = values, state = 'normal', width = 90 )
    a_widget.set( values[0] )
    my_control_obj.mode_widget = a_widget    # if just one use src
    a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W    ) # rowspan = 2, columnspan = 2 )
    ix_col   += 1

    #--- Action
    ix_row   += 1
    ix_col   = 0
    a_widget = Tk.Label( a_frame, text = "Action:",  anchor="w" ) #   relief = RAISED,  )
    a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W ) #rowspan = 2, columnspan = 2 )
    ix_col   += 1

    values        = [ "Create", "Activate", "Terminal", "Python", "Spyder" ]
    a_widget      = Tk.ttk.Combobox( a_frame, values = values, state = 'normal', width = 90 )
    a_widget.set( values[0] )

    my_control_obj.action_widget = a_widget    # if just one use src
    a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W    ) # rowspan = 2, columnspan = 2 )
    ix_col   += 1


    # a_widget = Tk.Label( a_frame, text = "Action:",  anchor="w" ) #   relief = RAISED,  )
    # a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W ) #rowspan = 2, columnspan = 2 )
    # ix_col   += 1

    # a_widget      = Tk.ttk.Combobox( a_frame, values = self.list_cmd_flag_values, state = 'readonly' )
    # self.install_flag_widget   = a_widget   # ?? this stuff might go in a control dict
    # tab_values.op_flag_widget  = a_widget

    # a_widget.set( self.list_cmd_flag_values[0] )
    # a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W    ) # rowspan = 2, columnspan = 2 )
    # ix_col   += 1

    ix_row   += 1
    ix_col   = 0

    #--- what  here which environment
    a_widget = Tk.Label( a_frame, text = "What:",  anchor="w", ) #   relief = RAISED,  )
    a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W ) #rowspan = 2, columnspan = 2 )
    ix_col   += 1
    # might want a editable dropdown for common stuff

    a_widget      = Tk.Entry( a_frame,   state = 'normal',  width = 100, )
    a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W    ) # rowspan = 2, columnspan = 2 )
    my_control_obj.what_widget    = a_widget
    ix_col   += 1

    #--- command
    ix_row   += 1
    ix_col   = 0
    a_widget = Tk.Label( a_frame, text = "Command:",  anchor="w", ) #   relief = RAISED,  )
    a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W,   ) #rowspan = 2, columnspan = 2 )
    ix_col   += 1
    # might want a editable dropdown for common stuff

    a_widget      = Tk.Entry( a_frame,   state = 'normal',  width = 100, )
    a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W, columnspan = 2    ) # rowspan = 2, columnspan = 2 )
    my_control_obj.ccommand_widget    = a_widget
    ix_col   += 2

    # ---- do it
    ix_col  = 0
    ix_row  += 1
    a_widget = Tk.Button( a_frame , width = 10, height = 1, text = "DoIt" )
    self.copy_op_button  = a_widget
    a_widget.config( command = my_control_obj.do_it )
    a_widget.grid( row = ix_row, column = ix_col, rowspan = 1, sticky = Tk.E + Tk.W + Tk.N + Tk.S )
    ix_col   +=  1

    a_widget = Tk.Button( a_frame , width = 10, height = 1, text = "ShowIt ??" )
    self.copy_op_button  = a_widget
    #a_widget.config( command = my_control_obj.do_it )
    a_widget.grid( row = ix_row, column = ix_col, rowspan = 1, sticky = Tk.E + Tk.W + Tk.N + Tk.S )
    ix_col   +=  1

    return a_frame, my_control_obj

# ----------------------------------------------
class TabpVenv( tab_value_obj.AdamTabValues ):
    """
    this is for common commands
    """
    # ----------------------------------------
    def __init__(self, ):
        pass
        # super( )  # hope this is how we do it seems not to be working try:

        tab_value_obj.AdamTabValues.__init__( self )
        self.tabp_title          = "Venv"   # title on the tab
        AppGlobal.tab_dispatch_obj[ self.tabp_title ] = self
        print( "TabpCondaPip init"  )
        print( f"TabpCondaPip init AppGlobal.tab_dispatch_obj {AppGlobal.tab_dispatch_obj}"  )

        msg    = f"prior mode in TabpCondaPip {self.prior_mode}"
        print( msg )

    # ----------------------------------------
    def polling( self, ):   # for the polling of the tab

        mode     = self.mode

        # msg = f"TabpCondaPip.polling() ok {mode}"
        # rint( msg )

        if mode != self.prior_mode:
            msg = "mode change"
            print( msg )
            self.prior_mode = mode
        else:
            pass
            # msg = "no mode change"
            # print( msg )

    # ---------------------------------
    def do_it( self, ):   # or do the command from some button
        msg    = "what"
        #rint( msg )


        key   = self.mode.lower()

        msg  = f"TabpCondaPip.do_it for {key}"
        print( msg )


        if   key   == "conda":
            self.do_it_conda()

        elif key   == "pip":
            msg = f"TabpCondaPip do it for {self.mode}"
            print( msg )

        elif key   == "v enviroment":

            self.do_it_venv

        else:
            msg = f"no do it for mode {self.mode}"



   # ---------------------------------
    def do_it_venv( self, ):   # or do the command from some button
        """
        for mode "V Enviroment" do the action
        note: need to coordinate with drop down, think of better way
              whole thing might be moved to dict approach

        Command reference — conda 4.8.4.post65+1a0ab046 documentation
        https://docs.conda.io/projects/conda/en/latest/commands.html
        -e, --envs
        r"C:\apps\Anaconda3\condabin\conda.bat list"
        r"C:\apps\Anaconda3\condabin\conda.bat info -e"

        e 'conda activate envname' l

        Examples:

        conda create -n myenv sqlite

        for some I would like to end up manually in terminal ??

        """

        conda_bat    = r"C:\apps\Anaconda3\condabin\conda.bat"    # may need in parameters
        #msg    = "what"
        #rint( msg )
        key    = self.action.lower()
        msg = f"TabpCondaPip.do_it_venv for {key}"
        print( msg )
        if   key   == "activate environment":
            cmd = f"{conda_bat} list"

        elif   key   == "create environment":
            cmd = f"{conda_bat} tbd"

        elif key   == "list enviroments":

            cmd = f"{conda_bat} info -e"

        else:
            msg = f"no do it for mode {key}"
            AppGlobal.gui.write_gui( result  )
            return

        msg = f"TabpCondaPip.do_it_venv  for {key}"
        print( msg )

        AppGlobal.build_cmd.do_cmd( cmd )

# =======================================
if __name__ == "__main__":
    #----- run the full app
    import cmd_assist
    cmd_assist.main()





