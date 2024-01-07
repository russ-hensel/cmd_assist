# -*- coding: utf-8 -*-
"""
    gui for cmd_assist.py
"""

# put this at top of each app file:
# ---- main ------------------------------------------
if __name__ == "__main__":
    import main
    main.main()
# ------------------------------------------

import sys
import tkinter as tk
import logging
#from   tkinter.scrolledtext import ScrolledText
import pyperclip
import functools
import os
from   functools import partial

# ----- local
from   app_global import AppGlobal
import gui_ext    # gui_tk_ext would be better

import commands

# may need better place for these
STICKY_ALL          = tk.E + tk.W + tk.S + tk.N
ARG_WIDTH           = 100      # for width of things like 3d ddl
FRAME_BG            = "red"    # for descrete frames  may be in
# self.gui_style.style_widget( a_frame )
LAB_WIDTH           = 30       # used for some labels to keep stuff alligned
STD_BUTTON_HEIGHT   = 1  # needs to be int

# ------------------------------------------
def compute_tab_id_string( tab_title ):
    """
    get rid of this use full string !!


    """
    return tab_title[ 0: 4].lower()

# ===================== class
class GUI(   ):
    """
    yes this is the GUI
    """

    def __init__( self,   ):

        AppGlobal.gui       = self
        self.controller     = AppGlobal.controller
        self.parameters     = self.controller.parameters
        self.logger         = logging.getLogger( AppGlobal.logger_id + ".gui")
        self.logger.info("in class GUI init for the cmd_assist") # logger not currently used by here

        #rint( f"init GUI" )
        # self._set_widget_values( )

        self.gui_style     = gui_ext.GuiStyle( self.parameters.gui_style )

        self.test_tab_values  =  None   # populate later and others for other tabs

        # ----- start building gui
        self.root   = tk.Tk()

        icon_fn     =  '/mnt/WIN_D/Russ/0000/python00/python3/_projects/clipboard/icon_black.png'
        icon_fn     =  '/mnt/WIN_D/Russ/0000/python00/python3/_projects/clipboard/icon_red.png'

        icon_fn     =  '/mnt/WIN_D/Russ/0000/python00/python3/_projects/clipboard/icon_white.png'
        # icon_fn     =  '/mnt/WIN_D/Russ/0000/python00/python3/_projects/mushroom_data_2022/obs/2023_07_19/02/PXL_20230719_154004367.jpg'
        # icon_fn     =  '/mnt/WIN_D/Russ/0000/python00/python3/_projects/clipboard/icon_red.gif'
        # icon_fn     =  '/usr/share/icons/Faenza/apps/48/spacefm-find.png'   # worked
        icon_fn     =  '/mnt/WIN_D/Russ/0000/python00/python3/_projects/cmd_assist/cmd_assist_a.ico'  # ng try convert
        icon_fn     =  '/mnt/WIN_D/Russ/0000/python00/python3/_projects/cmd_assist/cmd_assist_a.png'  #   converted above with pinta and now works
                           # but does not seem to work as a desktop icon
        gui_ext.set_icon( self.root, icon_fn )
        self.text_in        = None    # init later

        self.commands        = None # list of commands ... all of them search for me

        # self.trans_combo_case     = [ ("Trans 1", "xxx" ),
        # ("Trans 2", "xxx" ), ( "nothing", "yyy") ]
        # ( text, function_call ) and use index

        self.text_out       = None    # used in controller? set below

        # self.button_var     = tk.IntVar()
        # self.button_var.set( self.controller.parameters.rb_num_on )

        self.commander       = None
            # needs to be set when a new commander
            #is setup perhaps cmd_assist .cb_install_cmd_gui

        # define here or in the panel with waring??

        #self.cb_mulp_cmd_var   = tk.IntVar()

        self.cb_star_cmd_var   = tk.IntVar()
        self.cb_url_var        = tk.IntVar()

        self.root.title( f"{self.controller.app_name} mode: {AppGlobal.parameters.mode} " +
                         f" version: {self.controller.version}" )

        #        # ----- set up root for resizing
        #        self.root.grid_rowconfigure(    0, weight=0 )
        #        self.root.grid_columnconfigure( 0, weight=1 )
        #
        #        self.root.grid_rowconfigure(    1, weight=1 )
        #        self.root.grid_columnconfigure( 1, weight=1 )

        # self.tab_id_dict   =  {}      # shortened name: tab_id
        self._build_gui( )


        self.root.geometry( self.controller.parameters.win_geometry )
        #rint( "next icon..." )
        if self.parameters.os_win:
            # icon may cause problem in linux for now only use in win
#            Changing the application and taskbar icon - Python/Tkinter - Stack Overflow
#            https://stackoverflow.com/questions/14900510/changing-the-application-and-taskbar-icon-python-tkinter
            import ctypes
            myappid = self.parameters.icon # arbitrary string
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
            print( "in windows setting icon" )
            self.root.iconbitmap( self.parameters.icon )
        msg       = "... icon done...."
        print( msg )

    # ------------------------------------------
    def _build_gui( self,    ):
        """
        build the visual elements

        """

        self._menu( self.root )

        self.root.grid_rowconfigure(    0, weight=0 )
        self.root.grid_rowconfigure(    1, weight=0 )
        self.root.grid_rowconfigure(    2, weight=0 )
        # moving to frame placement
        # self.root.grid_rowconfigure(    3, weight=1 )
        # self.root.grid_rowconfigure(    4, weight=1 )

        self.root.grid_columnconfigure( 0, weight=1 )
        #self.root.grid_columnconfigure( 1, weight=1 )

        ix_row    = -1  # we are going to place frames from top to bottom

        # # ----- _make_meta_control_frame_top application buttons
        # a_frame   = self._make_meta_control_frame_( self.root,  )
        # ix_row   += 1
        # a_frame.grid( row        = ix_row,
        #               column     = 0,
        #               columnspan = 2,
        #               sticky     = STICKY_ALL )

        # ---- spacer
        a_frame   = tk.Frame( self.root,
                              width    =300,
                              height   =20,
                              bg       = "red",
                              relief   = tk.RAISED, ) # borderwidth=1 )
        ix_row   += 1
        a_frame.grid( row         = ix_row,
                      column      = 0,
                      columnspan  = 2,
                      sticky      = STICKY_ALL )

        # ---- another spacer ??
        a_frame   = tk.Frame( self.root,
                              width   = 300,
                              height  = 20,
                              bg      = "green",
                              relief  = tk.RAISED, ) # borderwidth=1 )
        ix_row   += 1
        a_frame.grid( row         = ix_row,
                      column      = 0,
                      columnspan  = 2,
                      sticky      = STICKY_ALL )

        # # ---- _make_select_cmd_frame - new command frame was above -> tab frame ==========
        a_frame  = self._make_select_cmd_frame( self.root )   # tab_frame
        a_frame.grid( row = ix_row, column=0, columnspan = 4,
                     sticky = STICKY_ALL )
        ix_row   += 1   # start incrementing at the end
        #self.tab_frame = a_frame

        # ---- make_env_frame
        a_frame  = self._make_env_frame_( self.root )   # tab_frame
        a_frame.grid( row         = ix_row,
                      column      = 0,
                      columnspan  = 4,
                      sticky      = STICKY_ALL )

        ix_row   += 1   # start incrementing at the end
        #self.tab_frame = a_frame

        #  ---- _make_test_frame
        a_frame  = self._make_test_frame( self.root )   # tab_frame
        a_frame.grid( row = ix_row, column=0, columnspan = 4, sticky = tk.N + tk.S + tk.E + tk.W )

        self.gui_cmd_ix_row   = ix_row   # so we can correctly place later

        ix_row   += 1   # start incrementing at the end
        #self.tab_frame = a_frame

        # ----_make_browse_frame  right now for copy, move to tabs
        a_frame  = self._make_browse_frame( self.root )
        ix_row   += 1
        a_frame.grid( row = ix_row, column=0, columnspan = 4, sticky=tk.N + tk.S + tk.E + tk.W )

        # frames on left and right
        ix_row   += 1

        # ---- message frame
        frame0 = self._make_message_frame( self.root )
        frame0.grid( row=ix_row, column=0, sticky=tk.N + tk.S + tk.E + tk.W )
        self.root.grid_rowconfigure(    ix_row, weight=1 )

        self.root.geometry( self.controller.parameters.win_geometry )
#        print( "next icon..." )
        if self.parameters.os_win:
            # icon may cause problem in linux for now only use in win
#            Changing the application and taskbar icon - Python/Tkinter - Stack Overflow
#            https://stackoverflow.com/questions/14900510/changing-the-application-and-taskbar-icon-python-tkinter
            import ctypes
            myappid = self.parameters.icon # arbitrary string
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
#            #rint( "in windows setting icon" )
            self.root.iconbitmap( self.parameters.icon )
        msg       = "... icon done...."
        print( msg )

    # ------------------------------------------
    def _make_meta_control_frame_( self, parent_frame,  ):
        """
        this contains a button area for app control stuff -- the meta functions or introspcecito
        parent_frame >> passed a parent frame
        returns      >> this frame we make
        """
        placement = gui_ext.PlaceInGrid(  99, False )
        a_frame   = tk.Frame( parent_frame )

        # a_button  = tk.Button( a_frame , width=10,
        #                      height=STD_BUTTON_HEIGHT, text = "Ed Log" )
        # a_button.config( command = self.controller.os_open_logfile  )
        # placement.place( a_button )
        # self.gui_style.style_button( a_button )

        # # ---- edit parms
        # a_button = tk.Button( a_frame , width=10, height=STD_BUTTON_HEIGHT,
        #                      text = "Ed Parms" )
        # a_button.config( command = self.controller.os_open_parmfile  )
        # placement.place( a_button )
        # self.gui_style.style_button( a_button )

        # # ---- show parms
        # a_button = tk.Button( a_frame , width=10, height = STD_BUTTON_HEIGHT,
        #                      text = "Show Parms" )
        # a_button.config( command = self.show_parms  )
        # placement.place( a_button )
        # self.gui_style.style_button( a_button )

        # # ---- dev_notes_txt
        # if self.parameters.dev_notes_fn is not None:   # could just use the truth value ??
        #     a_button = tk.Button( a_frame , width=10,
        #                           height    = STD_BUTTON_HEIGHT,
        #                           text      = "Dev. Notes" )
        #     a_button.config( command = self.controller.os_open_dev_notes  )
        #     placement.place( a_button )
        #     self.gui_style.style_button( a_button )

        # a_button = tk.Button( a_frame , width=10,
        #                      height= STD_BUTTON_HEIGHT, text = "Restart" )
        # a_button.config( command = self.controller.restart  )
        # placement.place( a_button )
        # self.gui_style.style_button( a_button )

        # ---- help
        a_button = tk.Button( a_frame , width=10, height= STD_BUTTON_HEIGHT, text = "Help" )
        a_button.config( command = self.controller.os_open_help  )
        placement.place( a_button )
        self.gui_style.style_button( a_button )

        # # ---- about
        # a_button = tk.Button( a_frame , width=10, height= STD_BUTTON_HEIGHT, text = "About" )
        # a_button.config( command = self.open_about )
        # placement.place( a_button )
        # self.gui_style.style_button( a_button )

        return a_frame

    #---------------------
    def _menu (self, parent ) :
        """
        adds a menu bar to the parent
        returns:
            nothing

        """
        # ---- configuration
        menubar    = tk.Menu( parent )
        # !! some of these could use partial instead
        a_menu     = tk.Menu( menubar, tearoff = 0)

        a_menu.add_command( label   = "Show Parameters",
                            command = self.show_parms )

        a_menu.add_command( label   = "Edit Parameters File",
                            command = self.controller.os_open_parmfile )

        if self.parameters.readme_fn is not None:
            a_menu.add_command( label   = "Edit Readme",
                                command = self.controller.os_open_readme )

        if self.parameters.gui_text_log_fn:
            a_menu.add_command( label   = "Edit Gui Log",
                                command = self.controller.os_open_gui_log )

        a_menu.add_command( label   = "Edit Log File",
                            command = self.controller.os_open_logfile )

        a_menu.add_command( label   = "Restart",
                            command = self.controller.restart )

        menubar.add_cascade( label  = "Configuration",   menu = a_menu )

        # ---- About ---- help
        a_menu = tk.Menu( menubar, tearoff = 0 )

        # change to partial ??
        a_menu.add_command( label   = "Show General Help",
                            command = self.controller.os_open_help )

        # partial to open other help



        #help_function    = partial( AppGlobal.os_open_txt_file, "./help/command.txt" )
        help_function    =  self.controller.open_txt_help
        a_menu.add_command( label   = "Show Command Help",
                            command = help_function )

        # partial to open other help
        open_other_help    = partial( AppGlobal.os_open_txt_file, "./help/other_help.txt" )
        a_menu.add_command( label   = "Show Other Help",
                            command = open_other_help )

        # a_menu.add_command( label   = "Show Tab Page Help",
        #                     command = self.controller.open_tabp_help )

        # help_function    = partial( AppGlobal.os_open_txt_file, "./readme_rsh.txt" )
        # a_menu.add_command( label   = "Show Developer Notes",
        #                     command = help_function )

        a_menu.add_command( label   = "About...",
                            command = self.open_about )

        menubar.add_cascade( label  = "Help", menu = a_menu )

        parent.config( menu = menubar )
    # ------------------------------------------
    def _make_env_frame_( self, parent, ):
        """
        this frame is for the default directory
           the default python env
           and....
        """
        a_frame    = tk.Frame( parent,  bg  = "yellow", )   #
        self.gui_style.style_frame( a_frame )
        placement  = gui_ext.PlaceInGrid(  99, False )

        # ---- sudo password
        self.sudo_pass_var     = tk.IntVar()    # get() => value    set(string)  var = StringVar()

        a_widget   = tk.Checkbutton( a_frame, text="Sudo Pass",
                                    variable = self.sudo_pass_var, ) # command=cb_cb )

        placement.place( a_widget, sticky = tk.W )
        # self.gui_style.style( a_widget )   !! fix me

        # ---- default dir
        a_widget   =  tk.Label( a_frame,
                                text         = "Default Directory:",
                                justify      = tk.LEFT,
                                anchor       = tk.E,
                                width        = 30,
                                borderwidth  = 5, )
        placement.place( a_widget, sticky = tk.E )
        self.gui_style.style_label( a_widget )

        self.default_dir_var   = tk.StringVar()
        a_widget               = tk.Entry( a_frame ,
                                           width        = ARG_WIDTH,
                                                # syncedc to width in commands
                                           text         = "entry for dir",
                                           textvariable = self.default_dir_var  )

        self.gui_style.style_widget( a_widget )
        placement.place( a_widget )
        self.default_dir_widget   = a_widget

        placement.new_row()

        # ---- minimize on use
        self.minimize_var     = tk.IntVar()    # get() => value    set(string)  var = StringVar()
        a_widget   = tk.Checkbutton( a_frame, text="Min. on use",
                                    variable = self.minimize_var, ) # command=cb_cb )
        placement.place( a_widget, sticky = tk.W )

        #placement.ix_col   += 1    # to move across one

        # ---- python env
        a_widget   =  tk.Label( a_frame, text = "Python Env:",
                                justify     = tk.LEFT,
                                anchor      = tk.E,
                                width       = LAB_WIDTH,
                                borderwidth = 5, )
        self.gui_style.style_label( a_widget )
        placement.place( a_widget, sticky = tk.E )

        self.python_env_var   = tk.StringVar()
        a_widget              = tk.Entry( a_frame ,
                                         width        = ARG_WIDTH,
                                         text         = "Python env",
                                         textvariable = self.python_env_var  )

        self.python_env_widget   = a_widget
        self.gui_style.style_entry( a_widget )
        placement.place( a_widget )

        return a_frame

   # ------------------------------------------
    def _make_select_cmd_frame( self, parent, ):
        """
        this is the list of all commands.....
        make the command frame with search and ........

        was
        make the tab frame the frame for all the tab pages tabp and all its tab pages
        Return:  a frame with the controls in it
        """
        a_frame    = tk.Frame( parent,   bg   = "blue", )   #
        self.gui_style.style_widget( a_frame )
        placement  = gui_ext.PlaceInGrid(  99, False )

        # ---- key word
        # mess with placement to go down
        # placement.ix_row    += 1
        # placement.ix_col    -= 1
        a_widget   =  tk.Label( a_frame, text = "Key Words:",
                                justify       = tk.LEFT,
                                anchor        = tk.W,
                                borderwidth   = 5, ) #relief = tk.RAISED,  )
        self.gui_style.style_widget( a_widget )
        placement.place( a_widget )

        self.key_word_var   = tk.StringVar()
        a_widget            = tk.Entry( a_frame ,
                                        width        = 50,
                                        text         = "bound",
                                        textvariable = self.key_word_var )
        self.gui_style.style_entry( a_widget )
        placement.place( a_widget )
        a_widget.bind( "<Return>", self.search_commands_2  )

        self.key_word_var.set( AppGlobal.parameters.defaut_key_words )

        # ---- listbox
        listbox_scroll     = gui_ext.ListboxScroll( a_frame,
                                                   "Selected Commands (click to activate)",
                                                   height = 50 )

        listbox_scroll.set_click_function( self.activate_clicked_command )

        self.commands   = commands.CommandsDict()

        for value in self.commands.get_long_names():
            # cannot just do values ?? ... this is a extension
            #rint( value )
            listbox_scroll.insert_row( value )

        a_widget           = listbox_scroll.frame
        a_widget.configure( height = 50, width = 200 )
        self.gui_style.style_widget( a_widget )
        listbox_scroll.listbox.configure( height = 10, width = 100 )
        self.listbox_scroll = listbox_scroll

        placement.place( a_widget, rowspan = 10 )

        # ---- Select
        #rint( self.key_word_var.get(   ) )
        a_button   = tk.Button( a_frame , width=10,
                                height    = STD_BUTTON_HEIGHT,
                                text      = "Select",
                                relief    = tk.RAISED, )
        a_button.config( command =  self.search_commands  )   # no argumnts sent
        self.gui_style.style_button( a_button )
        placement.new_row()
        placement.place( a_button )

        #rint( self.key_word_var.get(   ) )
        a_button   = tk.Button( a_frame ,
                                width     = 10,
                                height    = STD_BUTTON_HEIGHT,
                                text      = "Clear",
                                relief    = tk.RAISED, )

        a_button.config( command =  self.do_clear_kw_button )   # no argumnts sent
        self.gui_style.style_button( a_button )
        placement.place( a_button )

        return a_frame

   # ------------------------------------------
    def _make_test_frame( self, parent, ):
        """
        make
        """
        a_frame    = tk.Frame( parent,  bg         = "green", )

        placement = gui_ext.PlaceInGrid(  99, False )

        a_button = tk.Button( a_frame , width=10, height=2, text = "test frame button " )
        #a_button.config( command = self.controller.cb_test  )
        placement.place( a_button )

        a_widget   =  tk.Label( a_frame, text = "test frame",
                                justify= tk.LEFT,
                                anchor = tk.W,
                                borderwidth = 5, relief = tk.RAISED,  )

        placement.place( a_widget )

        return a_frame

   # ------------------------------------------
    def _make_browse_frame( self, parent, ):
        """
        browse for file and directories -- 2 browses
        Return:  a frame with the controls in it

        !! more customization of browse needed
        """
        a_frame    = tk.Frame( parent, width=600, height = 200, bg ="gray",
                              relief = tk.RAISED, borderwidth=1 )
        AppGlobal.gui_style.style_widget( a_frame )

        lrow       = 0

        lcol        = 0
        lrow       += 1
        bw_for_file               = gui_ext.FileBrowseWidget( a_frame )
        bw_for_file.grid( row     = lrow, column = lcol, columnspan = 1 )
        bw_for_file.set_text(       AppGlobal.parameters.default_file  )   # !! change parm name
        bw_for_file.initialdir    = AppGlobal.parameters.file_initialdir
        bw_for_file.title         = AppGlobal.parameters.file_title
        bw_for_file.filetypes     = AppGlobal.parameters.file_filetypes
        bw_for_file.label_widget.configure( width = LAB_WIDTH )

        self.bw_for_file          = bw_for_file  # save reference  !! left over
        lcol   += 1

        a_widget     = tk.Button( a_frame, text="Default Path",   width = 10, anchor="w" )
        cb           = functools.partial(
                                          self.copy_browse_to_default_dir,
                                          a_widget  = self.bw_for_file, )
        a_widget.config( command = cb )
        #a_widget.config( command = self.copy_browse_to_default_dir  )
        a_widget.config( borderwidth = 5, relief = tk.RAISED,  )
        AppGlobal.gui_style.style_button( a_widget )
        a_widget.grid( row = lrow, column = lcol, rowspan = 1,
                       sticky = tk.E + tk.W + tk.N + tk.S )
        self.button_browse_file_default = a_widget  # for enable disable
        lcol +=  1

        a_widget     = tk.Button( a_frame, text="Src File",   width = 10, anchor="w" )
        cb  = functools.partial( self.set_src_dest,
                                a_widget  = self.bw_for_file,
                                a_type    = "file" ,
                                a_target  = "src")
        a_widget.config( command = cb )
        a_widget.config( borderwidth = 5, relief = tk.RAISED,  )
        AppGlobal.gui_style.style_button( a_widget )
        a_widget.grid( row = lrow, column = lcol, rowspan = 1, sticky = tk.E + tk.W + tk.N + tk.S )
        self.button_browse_file_src = a_widget
        lcol +=  1

        a_widget     = tk.Button( a_frame,
                                 text      = "Dest File",
                                 width     = 10,
                                 anchor    = "w" )
        cb  = functools.partial( self.set_src_dest,
                                a_widget   = self.bw_for_file,
                                a_type     = "file" ,
                                a_target   = "dest")
        a_widget.config( command = cb )
        # a_widget.config( borderwidth = 5, relief = tk.RAISED,  )
        self.gui_style.style_widget( a_widget )
        a_widget.grid( row = lrow, column = lcol, rowspan = 1, sticky = tk.E + tk.W + tk.N + tk.S )
        self.button_browse_file_dst = a_widget  # for enable disable
        lcol +=  1

        # ---- dir browse
        lcol        = 0
        lrow       += 1
        bw_for_dir      = gui_ext.DirBrowseWidget( a_frame )
        bw_for_dir.grid( row = lrow, column = lcol, columnspan = 1 )
        # bw_for_dir.set_text( AppGlobal.parameters.default_dir  )
        # some of this may not be functional for a dir browse
        bw_for_dir.set_text(       AppGlobal.parameters.default_dir  )
        bw_for_dir.initialdir    = AppGlobal.parameters.dir_initialdir
        bw_for_dir.title         = AppGlobal.parameters.dir_title
        bw_for_dir.filetypes     = AppGlobal.parameters.dir_filetypes
        bw_for_dir.label_widget.configure( width = LAB_WIDTH )
        self.bw_for_dir          = bw_for_dir
        lcol   += 1

        a_widget     = tk.Button( a_frame, text="Default Path",
                                 width = 10, anchor="w" )
        cb  = functools.partial( self.copy_browse_to_default_dir,
                                 a_widget  = self.bw_for_dir, )
        a_widget.config( command = cb )
        #a_widget.config( borderwidth = 5, relief = tk.RAISED,  )
        self.gui_style.style_widget( a_widget )
        a_widget.grid( row = lrow, column = lcol, rowspan = 1,
                       sticky = tk.E + tk.W + tk.N + tk.S )
        lcol +=  1

        a_widget     = tk.Button( a_frame, text="Src Path",   width = 10, anchor="w" )
        cb  = functools.partial( self.set_src_dest,
                    a_widget  = self.bw_for_dir, a_type = "dir" , a_target = "src")
        a_widget.config( command = cb )

        #a_widget.config( borderwidth = 5, relief = tk.RAISED,  )
        self.gui_style.style_widget( a_widget )
        a_widget.grid( row = lrow, column = lcol, rowspan = 1, sticky = tk.E + tk.W + tk.N + tk.S )
        self.button_browse_dir_src = a_widget  # for enable disable
        lcol +=  1

        a_widget     = tk.Button( a_frame, text="Dest Path",   width = 10, anchor="w" )
        cb  = functools.partial( self.set_src_dest,
                                a_widget  = self.bw_for_dir, a_type = "dir" , a_target = "dest")
        a_widget.config( command = cb )

        #a_widget.config( borderwidth = 5, relief = tk.RAISED,  )
        self.gui_style.style_widget( a_widget )
        a_widget.grid( row = lrow, column = lcol, rowspan = 1, sticky = tk.E + tk.W + tk.N + tk.S )
        self.button_browse_dir_dst = a_widget  # for enable disable
        lcol +=  1

        return  a_frame

    # ------------------------------------------
    def _make_message_frame( self, parent,  ):
        """
        a frame with scrolling text area and controls for it
        -- there is a scrolled_text control, not currently using it --- why??
        need to convert to gui_ext
        !!
        """
        a_frame            = gui_ext.MessageFrame( parent, self.gui_style  )
        self.message_frame = a_frame

        for i_widget in self.message_frame.button_widgets:
            i_widget.configure( height = STD_BUTTON_HEIGHT )


        return a_frame

        # ---- old moving out

        self.max_lines      = 500
        self.cb_scroll_var  = tk.IntVar()  # for check box in reciev frame
        color               = "red"

        iframe  = tk.Frame( parent, width=300, height=800,
                           bg ="blue", relief=tk.RAISED,
                           borderwidth=1,  )
        self.iframe = iframe
        self.gui_style.style_widget( iframe )

        bframe  = tk.Frame( iframe, bg ="black", width=30  )
        # width=300, height=800, bg ="blue", relief=RAISED, borderwidth=1,  )
        bframe.grid( row=0, column=0, sticky = tk.N + tk.S )

        text0 = tk.Text( iframe , width=50, height=20 )
        #text0.configure( bg = "red" )

        s_text0 = tk.Scrollbar( iframe  )  # LEFT left
        s_text0.grid( row=0, column=2, sticky = tk.N + tk.S )

        s_text0.config( command=text0.yview )
        text0.config( yscrollcommand = s_text0.set )

        text0.grid( row=0, column=1, sticky = tk.N + tk.S + tk.E + tk.W  )
        #self.rec_text  = text0
        self.text_in   = text0   # not very ellegant

        iframe.grid_columnconfigure( 1, weight=1 )
        iframe.grid_rowconfigure(    0, weight=1 )

        # spacer
        s_frame = tk.Frame( bframe, bg ="green", height=20 ) # width=30  )
        s_frame.grid( row=0, column=0  )
        row_ix   = 0

        # --------------------
        b_clear = tk.Button( bframe , width=10, height=2, text = "Clear" )
        b_clear.bind( "<Button-1>", self.do_clear_button )
        self.gui_style.style_widget( b_clear )
        b_clear.grid( row=row_ix, column=0   )
        row_ix   += 1

        # ----- copy selection, moving to my new coding standards
        a_widget = tk.Button( bframe , width=10, height=2, text = "Copy/Sel." )
        # a_widget.bind( "<Button-1>", self.do_copy_button )
        a_widget.config( command = self.cb_copy_selection )
        self.gui_style.style_widget( a_widget )
        a_widget.grid( row=row_ix, column=0   )
        row_ix += 1

        # ----- copy all
        a_widget = tk.Button( bframe , width=10, height=2, text = "Copy/All" )
        # a_widget.bind( "<Button-1>", self.do_copy_button )
        a_widget.config( command = self.cb_copy_all )
        AppGlobal.gui_style.style_widget( a_widget )
        a_widget.grid( row=row_ix, column=0   )
        row_ix += 1

        # ------- auto scroll
        a_widget = tk.Checkbutton( bframe,  width=7, height=2, text="A Scroll",
                                variable=self.cb_scroll_var,  command=self.do_auto_scroll )
        a_widget.grid( row=row_ix, column = 0, sticky = tk.E + tk.W   )
        row_ix += 1

        self.cb_scroll_var.set( self.parameters.default_scroll )

        return iframe
    # ----  end construction ====================

    # ----  gets --------
    # ----------------------------------------
    def activate_command_by_key( self, a_key  ):
        """
        taking a key from a row
        activate the corresponding command
        see activate_clicked_command
        note that key needs to be stripped down
        ex:  gui.activate_command_by_key( "CommandCopy"  )
        """
        a_key   = a_key.split( " " )[ 0 ]
        #rint( f"test_callback a_key = {a_key}" )
        a_command = self.commands.get_command_by_name( a_key )
        #print( f"command key words {a_command.key_words}" )  error

        # ?? what is this next
        #rint( f"command info {a_ctest_callbacktest_callbackommand.info}" )
        self.controller.cb_install_cmd_gui( a_command )
        #self.commands_dict.select_by_key_words( [ "install", "python" ] )
        return a_key

    # ----------------------------------------
    def activate_clicked_command( self, event ):
        """
        this is called from click on scroll box
        this activates the gui it is not the search function
        select a command from the list of commands
        set up for clicked command
        event is the event sent
        need to change to a key

        a_key    a string identifying the command

        """
        print( ">>>>>>>>>>>>>>>>>>>>>>>>>> activate_clicked_command")
        a_key   = event.widget.selection_get()
        a_key   = self.activate_command_by_key( a_key )

        #self.commands_dict.select_by_key_words( [ "install",   ] )
        return a_key   # probaly never used

    # ----------------------------------------
    def test_callback( self, a_key ):
        """
        test, should not be in finished app

        """
        a_key ="return value"
        # # print( f"test....test...test {event} ")
        # # a_key   = event.widget.selection_get()
        # print( f"test_callback {a_key}" )
        # # a_command = self.commands_dict.get_command_by_name( a_key )
        # # print( f"command key words {a_command.key_words}" )
        # # print( f"command info {a_command.info}" )
        # # self.controller.cb_install_cmd_gui( a_command )
        # # #self.commands_dict.select_by_key_words( [ "install", "python" ] )
        # self.commands_dict.select_by_key_words( [ "install",   ] )
        return a_key

    # ----------------------------------------
    def search_commands_2( self, an_event ):
        """
        read code
        """
        print( "search_commands_2" )
        self.search_commands()

    # ----------------------------------------
    def search_commands( self, ):
        """
        using key words search for matching commands
        !! should some of this code move to commands.py
        """
        #rint( f"search_commands{1}")

        #  get the key words
        key_words = self.key_word_var.get( ).strip()
        #rint( f"search_commands key_words {key_words}")

        key_words  = key_words.split( " " )
        #rint( f"search_commands key_words {key_words}")

        found_commands         = self.commands.select_by_key_words(key_words )
        command_long_names     = self.commands.get_long_names( found_commands )

        # ================== found commands to long names put the commands in list
        self.listbox_scroll.clear_rows()

        for value in command_long_names:  # cannot just do values ?? ... this is a extension
            #rint( value )
            self.listbox_scroll.insert_row( value )
        # ---- now auto select the first
        if len( command_long_names ):
            a_listbox  = self.listbox_scroll.listbox
            a_value    = a_listbox.get( 0 ) #not the listbox but gui_ext
            self.activate_command_by_key( a_value )

    # ------------------------------------------
    def copy_browse_to_default_dir( self, a_widget = None ):
        """
        take the browsed file name and copy to the src file widget
        !! is a_widget = None required for partial
        """
        #sg   = "copy_browse_to_default_dir"
        #rint( "msg" )
        file_name    =      a_widget.get_text( )

        file_name, action   = self.make_dir_name( file_name )

        self.default_dir_var.set( file_name )
        # self.default_dir_widget.config( text  = fn, ) #anchor = "e" ) for a label

    # ------------------------------------------
    def do_clear_kw_button( self, ):
        """
        for the clear key words button --
        arguments:  event, ignored can be anything
        clear the receive area
        """
        self.key_word_var.set( "" )

    # ------------------------------------------
    def do_clear_button( self, event):
        """
        for the clear button -- text or message box
        arguments:  event, ignored can be anything
        clear the receive area
        """
        self.text_in['state'] = 'normal'      # normal  disabled
        self.text_in.delete( 1.0, tk.END )
        # !! may need refresh here is next any good
        self.root.update()
        self.text_in['state'] = 'disabled'      # normal  disabled

    # ------------------------------------------
    def do_copy_button( self, event ):
        """
        copy all text to the clipboard
        """
        data  = self.text_in.get( 1.0, tk.END )
        pyperclip.copy( data )

    # ------------------------------------------
    def do_auto_scroll( self,  ):
        """
        still configured so needed, but will not work ??
        pass, not needed, place holder see
        """
        print( "do_auto_scroll fix !!" )
        # not going to involve controller

    # ------------------------------------------
    def cb_copy_selection( self,  ):
        """
        copy selected text in the message/receive area
        """
        # this change to normal seems be required to copy delte... ?
        self.text_in['state'] = 'normal'      # normal  disabled
        try:
            data  = str( self.text_in.get( "sel.first", "sel.last" ) )
            pyperclip.copy( data )
        except Exception as exception:  # if no selection -- this is too broad and exception !!
            msg  = f"cb_copy_selection pyperclip exception {exception}"
            print( msg )
        self.text_in['state'] = 'disabled'      # normal  disabled

    # ------------------------------------------
    def cb_copy_all( self,  ):
        """
        copy all from message/receive area
        new from terminal implementation
        """
        # pass
        # this change to normal seems be required to copy delte... ?
        self.text_in['state'] = 'normal'      # normal  disabled
        # added str because of error: QXcbClipboard::setMimeData: Cannot set X11 selection owner
        data    = str( self.text_in.get( 1.0, tk.END ) )
        msg     = f"test me cb_copy_all >{data}<"
        print( msg )
        pyperclip.copy( data )
        self.text_in['state'] = 'disabled'      # normal  disabled


    # ----  actions --------

    #----------------------------------------------------------------------
    def open_about( self,  ):
        """
        what it says, read
        """
        gui_ext.about( AppGlobal.controller )

    #---------------------
    def bring_to_top( self   ):
        """
        What it says, read code
        """
        #---------------------
        gui_ext.bring_to_top( self.root )

    #---------------------
    def minimize_gui( self   ):
        """
        What it says, read code
        """
        #---------------------
        gui_ext.minimize_gui( self.root )

    #----------------------------------------------------------------------
    def show_parms(self, ):
        """
        what it says, read
        """
        msg     = f"{AppGlobal.parameters}"
        title   = "Parameters"
        #rint( msg )
        self.write_gui_wt( title, msg )

    #----------------------------------------------------------------------
    def write_gui_wt(self, title, a_string ):
        """
        write to gui with a title.
        title     the title
        a_string  additional stuff to write
        make a better function with title = ""  ??
        title the string with some extra formatting
        clear and write string to input area
        """
        self.write_gui( f" =============== {title}  ==> \n {a_string}" )
            # better format or join ??

    #----------------------------------------------------------------------
    def write_gui( self, string ):
        """
        clear and write string to display area
        leave it disabled
        perhaps should be moved to the message frame itself
        """
        text_in   =  self.message_frame.msg_text


        text_in['state'] = 'normal'      # normal  disabled
        text_in.delete( 1.0, tk.END )
        text_in.insert( tk.END, string )
        text_in['state'] = 'disabled'      # normal  disabled

    #----------------------------------------------------------------------
    def place_cmd_frame( self, frame_returning_function ):
        """
        place the frame from commands.py
        could call with the whole command object instead of just functin ??
        """
        a_frame  = frame_returning_function( self.root )
        #a_frame  = a_commander.build_gui_frame( self.gui.root )
        a_frame.grid( row        = self.gui_cmd_ix_row,
                      column     = 0,
                      columnspan = 4,
                      sticky     = tk.N + tk.S + tk.E + tk.W )


    # ----------------------------------
    def make_dir_name( self, file_name ):
        """
        what it says
        return
            tuple
                tuple[0]  name of related directory or ""
                tuple[1]  action,   -1 not found, n truncated n times ( may allow only 1 ??)
        """
        file_name   = file_name.replace("\\", "/")   # normalize name to linux

        a_bool       = os.path.isdir( file_name )
        #rint( f"make_dir_name       isdir  >>{a_bool}<<" )
        if a_bool:
            #rint( f"make_dir_name       original file is a dir" )
            return( file_name, 0 )

        file_name_parts   = file_name.split( "/" )
        #rint( f"make_dir_name  file_name_parts >>{file_name_parts}<<" )

        new_name     = "/".join( file_name_parts[:-1] )
        a_bool       = os.path.isdir( new_name )
        #rint( f"make_dir_name   isdir  >>{a_bool}<<" )
        if a_bool:
            #rint( f"make_dir_name  revised fn is a dir {new_name}" )
            return( new_name, 0 )

        #rint( f"make_dir_name       have not found dir" )
        return( "", -1 )

    #----------------------------------------------------------------------
    def get_default_dir( self,  ):
        """
        this is not out of either browse window but the main gui default

        """
        a_string         = self.default_dir_var.get(    )
        a_string, flag   = self.make_dir_name( a_string )
        #rint( f"get_default_dir  {a_string}")
        return a_string

      #----------------------------------------------------------------------
    def set_src_dest( self, a_widget, a_type, a_target ):
        """
        self.commander is dynamic hence this indirection

        """
        #rint(  f"set_src_dest", a_widget.get_text(), a_type, a_target )
        a_string  =  a_widget.get_text()
        self.commander.set_arg( a_string, a_target )

    # ----   gets and sets  --- instead inject into their own objects
    # -- all moving to tab_value_obj

    # ---------------------------------
    @property
    def copy_cmd( self ):
        ret    =   self.copy_cmd_widget.get()
        return ret

    # ---------------------------------
    @copy_cmd.setter   # looks like you should make a getter befor using a setter
    def copy_cmd( self,  arg ):
        """
        what it says !! may have to set to normal
        """
        #print( " set  list_cmd" )
        #self.list_cmd_widget.set( arg )    # does not work for entry widget
        self.copy_cmd_widget.delete(0, tk.END)
        self.copy_cmd_widget.insert(0, arg )

    # ---------------------------------
    @property    # under f for file
    def copy_src_file( self ):
        ret    =   self.copy_src_widget.get()
        return ret

    # ---------------------------------
    @property
    def copy_op( self ):
        ret    =   self.copy_op_widget.get()
        return ret

    # ---------------------------------
    @property    # under p for path
    def copy_dst_path( self ):
        ret    =   self.copy_dst_path_widget.get()
        return ret

    # ---------------------------------
    @property    # under f for file
    def copy_src_path( self ):
        ret    =   self.copy_src_path_widget.get()
        return ret

    # -------  list
    # ---------------------------------
    @property
    def list_cmd( self ):
        """
        what it says
        """
        ret    =   self.list_cmd_widget.get()
        #rint( " list_cmd has no setter really")
        return ret

    # ---------------------------------
    @list_cmd.setter   # looks like you should make a getter befor using a setter
    def list_cmd( self,  arg ):
        """
        what it says
        """
        #print( " set  list_cmd" )
        #self.list_cmd_widget.set( arg )    # does not work for entry widget
        self.list_cmd_widget.delete(0, tk.END)
        self.list_cmd_widget.insert(0, arg )

    # ---------------------------------
    @property
    def list_cmd_flag( self ):
        """
        what it says
        has to split the command on the |

        """
        ret    =   self.list_flag_widget.get()
        # this is pipe seperated but may be missing ...
        if ret != "":
            splits  = ret.split( "|" )
            ret     = splits[0]

        #rint( "list_cmd_flag" )
        return ret

    # ---------------------------------
    @property
    def list_cmd_path( self ):
        ret    =   self.list_cmd_path_widget.get()
        #rint( f"list_cmd_path is: {ret}")
        return ret

    # ---------------------------------
    @property
    def list_op( self ):
        ret    =   self.list_op_widget.get()
        # # this is pipe seperated
        # if ret != "":
        #     splits  = ret.split( "|" )
        #     ret     = splits[0]

        #print( "list_op is {ret}" )
        return ret






