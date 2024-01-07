"""
Abstract base class for all commands
    commands are not implemented here
    see header of each file....


    how about a launcher for all my python programs


"""


# ---- main ------------------------------------------
if __name__ == "__main__":
    import main
    main.main()
# ------------------------------------------

import sys
import os
from   tkinter import ttk
import tkinter as Tk
import pyperclip


# ------- local
import gui_ext
from   app_global import AppGlobal
import data


STD_BUTTON_HEIGHT   = 1 # gui.STD_BUTTON_HEIGHT

# ============================================
class CommandABC(  ):
    """
    will become an abstract base class
    """
    def __init__( self,     ):
        """
        usual init

        """
        # actually set some of these in gui construct
        #rint( "CommandABC.__init__()"  )
        self.name               = "CommandABC"
        self.key_word_str       = "cp copy File"
        self.key_words          = [ "word 1",  ] # now made by function
        self.command_string     = "ls"
        self.short_desc         = "short desc"
        self.shell_fn           = ""
        self.info               = "This will list the files in your current directory\n"
        self.info               = f"{self.info}or any other directory you specify\n"
        self.info               = f"{self.info}the Linux command is ls\n"

        self.set_py_env         = False
        self.set_def_dir        = True

        self.cmd_fixed          = None   # this is for a fixed part of the command
        self.cmd_fixed_widget   = None   # defined in build_gui ?
        self.arg_1_var          = None   # src
        self.arg_1_widget       = None
        self.short_desc_widget  = None   # defined in build_gui ?

        self.arg_2_var          = None    # dst
        self.arg_2_widget       = None
        self.arg_1_ddl_dict     = None    # may be list, or for "nesting to arg2 a dict"
        self.arg_2_values       = None    # not needed
        self.nest_arg_1_2       = False   # true if args are nested

        self.a_sync_combo       = None    # created later for triple drop down lists

        self.command_help       = AppGlobal.parameters.command_help

        self.run_function       = self.run_command_1    # but normally set in each command

    #----------------------------------
    def get_ddl_args( self, ):
        """
        get the 3 args and make any <> substutions
        read the code
        return list  of 3 ddl values
        """
        #rint( "==============================================================")
        args   = self.a_sync_combo.get_3_args()

        args   = [ self.substitute_into_string( arg ) for arg in args ]
                 # tuple completion not a thing get a generator

        #rint( f"!!!!!!!!!!!!!!!get_3_args args{args}")
        return args

    #----------------------------------
    def build_gui_3d_frame_from_args( self,
                                       parent,
                                       a_sync_combo     = None,
                                       command_str      = None,
                                       short_desc       = None,
                                       arg_1_label      = None,
                                       w_type_1         = None,
                                       arg_2_label      = None,
                                       w_type_2         = None,   ):
        """

        args
            parent     the root frame, will probably be gui.root but use parent
            a_sync_combo   an instance of SyncCombo
            ..... may be changing
            arg_1_lable  should be the label for arg_1 ... or in the a_sync_combo ??
            w_type_1 = None default "entry" or "combo"
        return a frame  ... may be placed by gui.place_cmd_frame
            use these: !!out of date
            self.arg_1_widget.get()
            self.arg_1_var.get()
        """
        #rint( parent, type( parent ) )
        a_frame     = Tk.Frame( parent,  bg   = "gray", )
        placement   = gui_ext.PlaceInGrid(  99, False )

        b_frame      = self.build_gui_buttons( a_frame )
        placement.place( b_frame )

        #rint( a_sync_combo )
        b_frame      = self.build_gui_3d_cmd_from_args(    a_frame,
                                        a_sync_combo     = a_sync_combo,
                                        command_str      = command_str,
                                        short_desc       = short_desc,
                                        arg_1_label      = arg_1_label,
                                        w_type_1         = w_type_1,
                                        arg_2_label      = arg_2_label,
                                        w_type_2         = w_type_2,   )
        AppGlobal.gui.gui_style.style_frame( b_frame )
        placement.place( b_frame )

        return a_frame

    # ----------------------------------
    def build_gui_3d_cmd_from_args(  self,
                                   parent,
                                   a_sync_combo     = None,
                                   command_str      = None,
                                   short_desc       = None,
                                   arg_1_label      = None,
                                   w_type_1         = None,
                                   arg_2_label      = None,
                                   w_type_2         = None,   ):
        """
        what it says

        specific gui for a particular command, not the buttons which are in build_gui_buttons
        w_type_1 = None default "entry" or "combo"
        arguments:
            should these just use the instance var, or be free of them
        return
            a frame for placement
        later use these:
            self.arg_1_widget.get()
            self.arg_1_var.get()
        """
        #rint( a_sync_combo )

        a_frame     = Tk.Frame( parent,  bg   = "gray", )
        placement   = gui_ext.PlaceInGrid(  99, False )

        a_sync_combo.make_ddls( a_frame )

        arg_width  = 100 # !! auto in a_sync_combo

        # ---- short desc with label
        a_widget   =  Tk.Label( a_frame, text = "Short desc:",
                                justify       = Tk.LEFT,
                                anchor        = Tk.E,
                                borderwidth   = 5, )
        AppGlobal.gui_style.style_label( a_widget )
        placement.place( a_widget, sticky = Tk.E )

        a_widget   =  Tk.Label( a_frame, text = self.short_desc,
                                justify       = Tk.LEFT,
                                anchor        = Tk.W,
                                borderwidth   = 5,
                                width         = arg_width,    )

        self.short_desc_widget   = a_widget
        AppGlobal.gui_style.style_label( a_widget )
        placement.place( a_widget, sticky = Tk.W )

        # ---- command_str cmd_fixed_widget
        if command_str is not None:

            placement.new_row()

            a_widget   =  Tk.Label( a_frame, text = "Command ( base ):",
                                    justify       = Tk.LEFT,
                                    anchor        = Tk.E,
                                    borderwidth   = 5, )

            AppGlobal.gui_style.style_label( a_widget )
            placement.place( a_widget, sticky = Tk.E )

            a_widget   =  Tk.Label( a_frame, text = command_str,
                                    justify       = Tk.LEFT,
                                    anchor        = Tk.W,
                                    borderwidth   = 5,
                                    width         = arg_width,    )

            self.cmd_fixed_widget   = a_widget
            AppGlobal.gui_style.style_label( a_widget, )
            placement.place( a_widget, sticky = Tk.W )

        if  a_sync_combo.is_3d():

            # ---- arg_1 ddl_0
            placement.new_row()

            a_widget   = a_sync_combo.get_label_widget( 0, a_frame )
            AppGlobal.gui_style.style_label( a_widget )
            placement.place( a_widget, sticky = Tk.E )

            # self.arg_1_var         = Tk.StringVar()

            a_widget    = a_sync_combo.ddl_widgets[0]
            AppGlobal.gui_style.style_combobox( a_widget )
            self.arg_1_widget      = a_widget
            placement.place( a_widget, sticky = Tk.W )

        # ---- arg 2 ddl_1
        placement.new_row()

        a_widget   = a_sync_combo.get_label_widget( 1, a_frame )
        AppGlobal.gui_style.style_label( a_widget )
        placement.place( a_widget, sticky = Tk.E )

        a_widget    = a_sync_combo.ddl_widgets[1]
        placement.place( a_widget )
        AppGlobal.gui_style.style_combobox( a_widget )
        self.arg_2_widget      = a_widget

        # ---- arg 3 ddl_2
        placement.new_row()

        a_widget    = a_sync_combo.get_label_widget( 2, a_frame )
        AppGlobal.gui_style.style_label( a_widget )
        placement.place( a_widget, sticky = Tk.E )

        a_widget    = a_sync_combo.ddl_widgets[2]
        placement.place( a_widget )
        AppGlobal.gui_style.style_combobox( a_widget )
        self.arg_3_widget      = a_widget

        return a_frame

    # ----------------------------------
    def build_gui_frame_from_argsxxxxx( self, parent,
                                   command_str      = None,
                                   short_desc       = None,
                                   arg_1_label      = None,
                                   w_type_1         = None,
                                   arg_2_label      = None,
                                   w_type_2         = None,   ):
        """
        what it says
        parent     the root frame, will probably be gui.root but use parent
        args
            w_type_1 = None default "entry" or "combo"
        return a frame  ... may be placed by gui.place_cmd_frame
            use these:
            self.arg_1_widget.get()
            self.arg_1_var.get()
        """
        a_frame     = Tk.Frame( parent,  bg         = "gray", )
        placement   = gui_ext.PlaceInGrid(  99, False )

        b_frame      = self.build_gui_buttons( a_frame )
        placement.place( b_frame )

        b_frame      = self.build_gui_cmd_from_args(       a_frame,
                                        command_str      = command_str,
                                        short_desc       = short_desc,
                                        arg_1_label      = arg_1_label,
                                        w_type_1         = w_type_1,
                                        arg_2_label      = arg_2_label,
                                        w_type_2         = w_type_2,   )

        placement.place( b_frame )

        return a_frame

    # ----------------------------------
    def build_gui_cmd_from_argsxxxxxx(  self, parent,
                                   command_str      = None,
                                   short_desc       = None,
                                   arg_1_label      = None,
                                   w_type_1         = None,
                                   arg_2_label      = None,
                                   w_type_2         = None,   ):
        """
        what it says

        specific gui for a particular command, not the buttons which are in build_gui_buttons
        w_type_1 = None default "entry" or "combo"
        arguments:
            should these just use the instance var, or be free of them
        return
            a frame for placement
        later use these:
            self.arg_1_widget.get()
            self.arg_1_var.get()
        """
        a_frame     = Tk.Frame( parent,  bg   = "gray", )
        placement   = gui_ext.PlaceInGrid(  99, False )

        # a_frame      = self.build_gui_buttons( parent )
        # placement.place( a_frame )

        arg_width  = 100

        # ---- short desc
        a_widget   =  Tk.Label( a_frame, text = "Short desc:",
                                justify       = Tk.LEFT,
                                anchor        = Tk.E,
                                borderwidth   = 5, )
        AppGlobal.gui_style.style_label( a_widget )
        placement.place( a_widget, sticky = Tk.E )

        a_widget   =  Tk.Label( a_frame, text = self.short_desc,
                                justify       = Tk.LEFT,
                                anchor        = Tk.W,
                                borderwidth   = 5,
                                width         = arg_width,    )

        self.short_desc_widget   = a_widget
        AppGlobal.gui_style.style_label( a_widget )
        placement.place( a_widget, sticky = Tk.W )

        # ---- command_str cmd_fixed_widget
        if command_str is not None:

            placement.new_row()

            a_widget   =  Tk.Label( a_frame, text = "Command ( base ):",
                                    justify       = Tk.LEFT,
                                    anchor        = Tk.E,
                                    borderwidth   = 5, )

            AppGlobal.gui_style.style_label( a_widget )
            placement.place( a_widget, sticky = Tk.E )

            a_widget   =  Tk.Label( a_frame, text = command_str,
                                    justify       = Tk.LEFT,
                                    anchor        = Tk.W,
                                    borderwidth   = 5,
                                    width         = arg_width,    )

            self.cmd_fixed_widget   = a_widget
            AppGlobal.gui_style.style_label( a_widget, )
            placement.place( a_widget, sticky = Tk.W )

        # ---- new field
        placement.new_row()

        if arg_1_label is None:
            return a_frame

        # ---- arg_1
        a_widget   =  Tk.Label( a_frame, text = arg_1_label,
                                justify       = Tk.LEFT,
                                anchor        = Tk.E,
                                borderwidth   = 5, )

        AppGlobal.gui_style.style_label( a_widget )
        placement.place( a_widget, sticky = Tk.E )

        self.arg_1_var         = Tk.StringVar()
        if   w_type_1 is None or w_type_1 == "entry":
            a_widget    = Tk.Entry( a_frame ,
                                   width = arg_width,
                                   text = "cmdabc default arg_1 entry widget",
                                   textvariable = self.arg_1_var )

            self.arg_1_widget      = a_widget
            #self.arg_1_var.set( "arg 1 var set ")
            AppGlobal.gui_style.style_entry( a_widget )

        else: # w_type_1 == "combo"
            # list done elswhere
            a_widget = ttk.Combobox( a_frame, width = arg_width,
                                       state = "normal",
                                       textvariable  = self.arg_1_var  )

            if  type( self.arg_1_ddl_dict ) == dict:
                values              = list( self.arg_1_ddl_dict.keys() )
                a_widget.configure( values = values )
                a_widget.set( next(iter(self.arg_1_ddl_dict))   )  # gets first key from dict
                a_widget.bind( "<<ComboboxSelected>>", self.sync_arg_1_arg_2  )
                # perhaps assigne values[0] to list

            else: # check for list
                print( "need to implement list" )

            AppGlobal.gui_style.style_combobox( a_widget )
            self.arg_1_widget      = a_widget

        placement.place( a_widget, sticky = Tk.W )

        # ---- arg_2
        if arg_2_label is None:
            return a_frame
        placement.ix_row   +=1
        placement.ix_col   -=2

        a_widget   =  Tk.Label( a_frame, text = arg_2_label,
                                justify       = Tk.LEFT,
                                anchor        = Tk.W,
                                borderwidth   = 5, )

        AppGlobal.gui_style.style_label( a_widget )
        placement.place( a_widget, sticky = Tk.E )

        self.arg_2_var         = Tk.StringVar()
        if   w_type_2 is None or w_type_2 == "entry":
            a_widget               = Tk.Entry( a_frame ,
                                               width         = arg_width,
                                               text          = "cmd abc default arg_2 entry widget",
                                               textvariable  = self.arg_2_var )
            AppGlobal.gui_style.style_entry( a_widget )
            self.arg_2_widget      = a_widget
            # self.arg_2_var.set( "arg 2 var set ")

        else: # w_type_1 == "combo"
            # list done elswhere
            a_widget = ttk.Combobox( a_frame,
                                        width = arg_width,
                                        state = "normal",
                                        textvariable  = self.arg_2_var  )

            AppGlobal.gui_style.style_combobox( a_widget )
            self.arg_2_widget      = a_widget

            self.sync_arg_1_arg_2( None )   # argument ignore
        #AppGlobal.gui_style.style_entry( a_widget )
            # !! probably should be specialized currently fails
        placement.place( a_widget, sticky = Tk.W )

        return a_frame

    # ----------------------------------
    def build_gui_buttons( self, parent ):
        """
        return a frame
        """
        a_frame    = Tk.Frame( parent,      bg  = "red", )

        # ---- runit
        placement   = gui_ext.PlaceInGrid(  99, by_rows = True )

        a_button = Tk.Button( a_frame ,
                              width     = 10,
                              height    = STD_BUTTON_HEIGHT,
                              text      = "RunIt",
                              relief    = Tk.RAISED,
                              command   = self.run_command )
        placement.place( a_button )
        AppGlobal.gui_style.style_button( a_button )

        # ---- preview
        # placement.new_row()
        placement.ix_col   = 0  # is this the right loc if do not have goth args ??
        a_button = Tk.Button( a_frame , width=10,
                             height     = STD_BUTTON_HEIGHT,
                             text       = "Preview",
                             relief = Tk.RAISED,
                             command = self.preview_command )
        AppGlobal.gui_style.style_button( a_button )
        placement.place( a_button )

        # ---- shell script
        placement.new_row()
        a_button = Tk.Button( a_frame , width=10,
                             height     = STD_BUTTON_HEIGHT,
                             text       = "Script",
                             relief     = Tk.RAISED,
                             command    = self.shell_file_for_command )
        AppGlobal.gui_style.style_button( a_button )
        placement.place( a_button )

        # ---- to clipboard
        placement.new_row()
        a_button = Tk.Button( a_frame , width=10,
                             height     = STD_BUTTON_HEIGHT,
                             text       = "Cpy ClipB",
                             relief     = Tk.RAISED,
                             command    = self.clipboard_for_command )
        AppGlobal.gui_style.style_button( a_button )
        placement.place( a_button )

        placement.new_column()   # is this what we want

        # ---- Web Help
        a_button = Tk.Button( a_frame ,
                              width   = 10,
                              height  = STD_BUTTON_HEIGHT,
                              text    = "Web Help",
                              relief  = Tk.RAISED,
                              command = self.get_cmd_help )
        AppGlobal.gui_style.style_button( a_button )
        placement.place( a_button )

        # ---- Txt Help
        a_button = Tk.Button( a_frame ,
                              width=10,
                              height    = STD_BUTTON_HEIGHT,
                              text      = "Txt Help",
                              relief    = Tk.RAISED,
                              command   = AppGlobal.controller.open_txt_help )
        AppGlobal.gui_style.style_button( a_button )
        placement.place( a_button )


        return a_frame

    # ----------------------------------
    def build_gui_frame( self, parent ):
        """
        return a frame
        think a dummy and each command has its own
        that will build the specic gui for the command
        """
        a_frame    = Tk.Frame( parent,   bg  = "red", )
        return a_frame

    # ----------------------------------
    def build_key_words( self, key_word_str ):
        """
        what it says read the code ??refactor
        still need camel case processing
        still need remove plurals
        move outside of this object, into commandsDict or ??
        Returns
            mutates self.key_words
        """
        key_word_str          = key_word_str.lower()
        key_words_input       = key_word_str.split( )
        key_words_output      = []
        # if last letter is an s, remove it
        for i_word in key_words_input:
            if i_word[ -1] == "s":
                i_word = i_word[ : -1 ]
            key_words_output.append( i_word )
        self.key_words  = key_words_output

        #rint( f"build_key_words self.key_words  {self.key_words}" )

    # ----------------------------------
    def build_prefix( self,  ):
        """
        prefix for command,
           * default dir and
           * python environment
        if not enpty then a nl on the end
        """
        cmd_list = []

        if self.set_def_dir:
            a_dir      = AppGlobal.gui.get_default_dir()  # possible test for existance !!
            cmd_list.append( f"cd {a_dir}" )

        if self.set_py_env:
            py_env_with = AppGlobal.parameters.py_env_with
            if py_env_with == "conda":
                # conda activate myenv
                env    = AppGlobal.gui.python_env_var.get()
                #cmd_list    = add_nl(cmd)
                cmd_list.append( f"conda activate {env}" )  # or source, old or new
            else:
                print( "python enviroment error not conda " )

        cmd_list.append( "pwd" )
        #rint( f"build_prefix >>{cmd_list}<<" )

        return cmd_list

     # ----------------------------------
    def build_suffix( self,  ):
        """
        what it says, eval at build time -- or not
        """
        return[ "echo 'suffix'" ]

    # ----------------------------------
    def edit_args( self,  ):
        """
        what it says,
        is edit check for ok ?
        """
        return True

    # ----------------------------------
    def build_echo(self, input_list ):
        """
        add echo commands except to echo commands
        and for now remove comments from the command part

        """
        new_list      = []
        for i_item in input_list:
            if i_item.startswith( "echo" ):
                new_list.append( i_item )
            else:
                new_list.append( f"echo '{i_item}'")
                # now look for command part comment
                splits     = i_item.split( "#" )
                i_item     = splits[0]     # combine lines for clean
                new_list.append( i_item )

        return new_list

    # ----------------------------------
    def build_command( self, add_echo = True, add_newline = False ):
        """
        this is an abstract version
        return command
        """
        ret    = "this is default abc build_commmand, should have been overiden"
        return ret

    # ----------------------------------
    def build_command_1_2( self, add_echo = True, add_newline = False ):
        """
        build command from arg1 and arg2
        self.build_command_1_2
        ex:
        return self.build_command_1_2( add_echo = add_echo, add_newline = add_newline )

        ! need a 0 1 2 version and a generalized one see commands 3 for vert which seems to do it
        """
        print( "build_command_1_2" )
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

    # ----------------------------------
    def build_command_1_2_3( self, add_echo = True, add_newline = False ):
        """
        return a command as a single string
        add_echo    see code
        add_newline   see code
        takes 3 inputs

        """
        # return self.build_command_1_2( add_echo = add_echo, add_newline = add_newline )
        # build command from arg1 and arg2
        # self.build_command_1_2
        # ex:
        # return self.build_command_1_2( add_echo = add_echo, add_newline = add_newline )

        print( "build_command_0_1_2" )
        args        = self.get_ddl_args()

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

    # ----------------------------------
    def build_shell_script( self,  ):
        """
        ??
        return none
        """
        pass

    # ----------------------------------
    def run_command( self,  ):
        """
        run command ...
        runtime reassigned to run_command_1 look ... yes usually is
        """
        self.run_function( )

    # ----------------------------------
    def run_command_1( self,  ):
        """
        run command

        is implemented I think see gui -- forwarded from run_command
        """
        #rint( f"\nrun_command_1 default_dir >>{self.get_default_dir()}<<" )

        full_cmd   = self.build_command()
        #rint( full_cmd )

        gui    = AppGlobal.gui
        if  gui.minimize_var.get( ):
            gui.minimize_gui()

        if "sudo " in full_cmd:
            #rint( "sudo command" )
            get_pass  = gui.sudo_pass_var.get( )
            if get_pass:
                pwd   = data.get_data( AppGlobal.parameters.sudo )
                pyperclip.copy( pwd )

        print( f"run_command_1 full_cmd   = {full_cmd}" )

        result = os.system( full_cmd  )
        print( f"result = os.system >>{result}<<")

    # ----------------------------------
    def preview_command( self,  ):
        """
        what it says
        command to gui
        """
        cmd        = self.build_command( add_echo = False, add_newline = True )
        #rint( f"preview_command >{cmd}<" )
        AppGlobal.gui.write_gui( cmd )

    # ----------------------------------
    def shell_file_for_command( self,  ):
        """
        what it says
         os_open_sh_file
        """
        a_line     = self.build_command( add_newline = True )
        file_name  = AppGlobal.parameters.shell_file_name
        with open( file_name, "w" ) as a_file:
            a_file.write (a_line )

        AppGlobal.os_open_sh_file( file_name  )

    # ----------------------------------
    def clipboard_for_command( self,  ):
        """
        what it says

        """
        a_line     = self.build_command( add_newline = True )
              # posibbly add_echo = False,
        print( f"clipboard_for_command {a_line}"  )
        pyperclip.copy( a_line )

    # ----------------------------------
    def get_cmd_help( self,  ):
        """
        what it says
        use command name .txt in a help directory
        or web address, or buttons for both ??
        """
        #AppGlobal.os_open_txt_file( ( f"./help/{self.name}.txt") )
        AppGlobal.os_open_help_file( self.command_help )

    # ----------------------------------
    def get_web_help( self,  ):
        """
        what it says

        """
        pass

    # ----------------------------------
    def get_3_argsxxxxx( self ):
        """
        phase out for 3 synced ddl
        what it says, read
        see call in build_command
        clears out the # if present ( comment )
        Returns
            tuple

        """
        if self.cmd_fixed is not None:
            splits     = self.cmd_fixed.split("#")
            cmd_ffixed = splits[0]
            cmd_ffixed = f"{cmd_ffixed.strip()} "
        else:
            cmd_ffixed = ""

        arg_1   = self.get_arg_or_none( self.arg_1_var )
        arg_2   = self.get_arg_or_none( self.arg_2_var )

        return ( cmd_ffixed, arg_1, arg_2 )

    # ------------------------------------
    def get_arg_or_none( self,  a_var  ):
        """
        ??
        arg:
            a_var   a tk variable
        """
        if a_var is None:
            msg   = ( f"sget_arg_if_not_none for None trying to get for {a_var}" )
            #rint( msg )
            return None
        #self.arg_2_widget.configure( text = a_string )
        else:
            #ret          =  a_var.get(  )
            splits       = a_var.get(  ).split("#")
            # cmd_ffixed   = splits[0]
            ret     = f"{splits[0].strip()} "  # strip except final " "
            #return splits[0]
            return ret

    # ------------------------------------
    def set_arg_if_not_none( self, a_string, a_target, a_var  ):
        """
        safety set for set_arg
        """
        if a_var is None:
            msg   = ( f"set_arg for None trying to set {a_string} into arg {a_target}" )
            print( msg )
        #self.arg_2_widget.configure( text = a_string )
        else:
            a_var.set( a_string )

    # ------------------------------------
    def set_arg( self, a_string, a_target,  ):
        """
        what it says
        need to do dynamically as target changes  ?? keep that widget around and fixed ??
        self.set_arg(   "a_string", "src",  )  "src" "dst"

        """
        #a_string   = a_widget.get_text()
        if   a_target in [ "src", "arg_1" ]:
            #self.arg_1_var.set( a_string )
            self.set_arg_if_not_none( a_string, a_target, self.arg_1_var  )
        else:
            #self.arg_2_var.set( a_string )
            self.set_arg_if_not_none( a_string, a_target, self.arg_2_var  )

    # ----------------------------------
    def get_default_dir( self,  ):
        """
        what it says
        consider clean up and check for existance !!
        """
        return  AppGlobal.gui.get_default_dir()

    # ----------------------------------
    def sync_arg_1_arg_2xxxxx( self, event  ):
        """
        what it says
        bind to    from self.arg_1_widget
            a_widget.bind( "<<ComboboxSelected>>",
                          self.sync_arg_1_arg_2  )
        ?? this has a fixed widget -- so get rid of event so we can call from elsewher !!
        arg:
            event -- not used
        """
        print( f"sync_arg_1_arg_2 begins" )
        if self.arg_1_ddl_dict is None:
            print( f"sync_arg_1_arg_2 dict is None" )
            return

        #rint( f"sync_arg_1_arg_2  event.widget {event.widget}" )

        #a_widget    = event.widget
        a_widget    = self.arg_1_widget

        #rint( f"a_widget.get() {a_widget.get()}" )

        # some cases might need find index or try.....
        dict_index  = a_widget.get()
        values      = self.arg_1_ddl_dict[ dict_index ]

        print( f"configure arg_2 with {values}" )
        self.arg_2_widget.configure( values = values )

        print( f"set value combb_2 {values[0]} type = {type(values[0])}")
        self.arg_2_widget.set( values[0] )

        #rint( event.widget.var.get() ) # you might inject

        # varname = str( a_widget.cget("variable") )  # unknow option
        #rint(  a_widget.getvar( varname ) )

        # works using text variable
        # print( self.comb_1_var.get( ) )

        # print( a_widget.current() )       # index of current from 0

    # ----------------------------------------
    def substitute_into_string( self, a_string,  ):
        """
        seems ok
        but want to split on comment and explain

        """
        #rint( AppGlobal.parameters.subsution_list )
        for i_sub in AppGlobal.parameters.subsution_list:
            a_string  = a_string.replace( *i_sub )   # !! even if not found

        return a_string

# ---- eof




