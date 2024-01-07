#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of commands
    these seem to be mostly for working with the
        edit
        names and passwords
        hardware
        file finding

"""

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


# ============================================
class CommandEditFile( commands_0.CommandABC ):
    """
    what it says

    """
    def __init__( self,     ):
        """
        usual init

        sudo xed /etc/hosts
        """
        super().__init__()
        #rint( "CommandCopy.__init__()"  )
        # ----------------------+---------------------+-------
        self.name             = "CommandEditFile      edit config file configuration hosts"
        self.build_key_words( self.name  )

        self.command_string   = "edit"
        self.short_desc       = "edit important system and application files"

        self.info             = "This will edit important system and application files\n"
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
        # -------------+-------------------------+-------
        a_file_list = ["/etc/hosts               # identify other machines",
                       "/etc/samba/smb.conf      # samba config file ",
                       "/etc/sudoers             # config for sudo",
                       "/etc/dhcpcd.conf         # network ip address",
                       "/etc/network/interfaces  # config net interfaces",
                       ]

        # ---- make the drop down values -- here with values that are tracable
        arg_1       = "z"

        # -------------+-------------------------+-------
        arg_2       =  "sudo gedit               # may want to pick another editor"#no  , !

        arg_3       = a_file_list

        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,           # key 0
                                  arg_2,           # key 1
                                  arg_3 )

        # -------------+-------------------------+-------
        arg_2       =  "sudo nemo                # launch nemo gui file manager"
        arg_3       = a_file_list

        a_sync_combo.add_to_dict( arg_1,          # key 0
                                 arg_2,           # key 1
                                 arg_3 )

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

# ============================================
class CommandMisc( commands_0.CommandABC ):
    """
    what it says
    >> cat – You can view and add to a text file with this command.
    >> cd – Change to your home directory with this command. Appending a space and a
    name will switch you to the named directory.
        Appending two periods will bring you to the current directory’s
        parent directory.
    >> du – This command displays disk space usage of files in a directory.
    >> chmod – This command is used to change the read, write and execute file permissions.
    >> history – Using this command you can see a list of the recently
        executed commands entered through the command line.
    >> locate – Find a file’s location by name with this command.
    >> more – This is a very helpful command that displays multiple
            pages of information one screen at a time. Hitting enter will show you the next screen.
    >> man – Short for manual, this command displays the reference manual
            pages for a specified command. Entering man ls will show what the manual has on the ls command.
    >> passwd – This command allows you to create or update passwords for user accounts.
    >> pwd # The current working directory is displayed with this command.
    >> mkdir – You can create a new directory with this command as long as
                    none already exist with the selected name.
    >> mv – Rename or move files and directories with this command.
    >> sudo – This is a very powerful command that allows an authorized
                    user to execute commands as the root user of the system.
    >> touch – You can create a file that does not already exist with this command.
                    If the file exists, the timestamp is updated, but the contents remain unchanged.

    """
    def __init__( self,     ):
        """
        usual init

        sudo xed /etc/hosts
        """
        super().__init__()
        #rint( "CommandCopy.__init__()"  )
        self.name             = "CommandMisc  Miscalenous misc commands"
        self.build_key_words( self.name )   # must be here after rest of init

        self.command_string   = ""
        self.short_desc       = "misc commands"
        #self.cmd_list          = None # put in build cmd with fstring ...
        #   !! local variable should be fine

        #self.shell_fn         = ""
        self.info             = "Misc commands \n"
        self.info             = f"{self.info}often used to make it executable\n"
        #self.info             = f"{self.info}......\n"
        self.web_ref          = r"http://bulldog/mediawiki/index.php/Linux_CheatSheet#copy_files"
        self.set_py_env       = False

    # ----------------------------------
    def build_gui_frame( self, parent ):
        """
        return a frame
        """
        # ---- build the widget manager
        a_sync_combo             = sync_combo.SyncCombo()
        a_sync_combo.arg_width   = gui.ARG_WIDTH
        a_sync_combo.set_label_text( "Command", "Source", "Target", )
        self.a_sync_combo  = a_sync_combo

        # -------------+-------------------------+-------
        a_file_list = ["tbd",
                       "tbd",
                       "tbd",
                       ]
        typically_0 = ["                         # Typically none", ]
        # ---- make the drop down values -- here with values that are tracable
        arg_1 = "z"

        # =============+-------------------------+-------
        arg_2       =  "pwd                      # Current working directory"#no  , !
        arg_3       = typically_0

        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,   # key 0
                                  arg_2,           # key 1
                                  arg_3 )

        # -------------+-------------------------+-------
        arg_2       =  "man                      # Display manual ( in arg 2 )"
        arg_3       = ["                         # The command",
                       ]

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

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
        return a command as a single string
        add_echo    see code
        add_newline   see code

        """
        args = self.get_ddl_args()
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

# ============================================
class CommandHW( commands_0.CommandABC ):
    """
    Commands to discover hardware
    """
    def __init__( self,     ):
        """
        usual init
        """
        super().__init__()
        #rint( "CommandCopy.__init__()"  )
        self.name             = "CommandHW discover hardware hw hard drives devices usb launch nemo gparted gnome disks"

        self.build_key_words( self.name )   # must be here after rest of init

        self.command_string   = ""
        self.short_desc       = "HW related commands"
        #self.shell_fn         = ""
        self.info             = "HW related commands \n"
        self.info             = f"{self.info}often used to make it executable\n"
        #self.info             = f"{self.info}......\n"
        self.web_ref          = r"http://bulldog/mediawiki/index.php/Linux_CheatSheet#find_usb"
        self.set_py_env       = False

    # ----------------------------------
    def build_gui_frame( self, parent ):
        """
        return a frame
        http://bulldog/mediawiki/index.php/Linux_CheatSheet#find_usb

        """
        # ---- build the widget manager
        a_sync_combo            = sync_combo.SyncCombo()
        a_sync_combo.set_label_text( "Command", "Source", "Target", )
        a_sync_combo.arg_width  = gui.ARG_WIDTH
        self.a_sync_combo       = a_sync_combo

        # -------------+-------------------------+-------
        typically_0 = ["                         # Typically none", ]
        arg_needed  = ["                         # Arg needed", ]
        # ---- make the drop down values -- here with values that are tracable
        arg_1       = "z"

        # =============+-------------------------+-------
        arg_2       =  "sudo fdisk -l            # terminal   -> detailed disk info including usb"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "lsblk                    # terminal   -> summary of disks"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "gparted                  # gui launch -> disk partition manager"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "gnome-disks              # gui launch -> disk inspector"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "nemo                     # gui launch -> file manager"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "df -h                    # shows disk space in human-readable format"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "du -s                    # disk space used by a particular file or directory"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "inxi --basic             # Basic output, short form"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "inxi --audio             # Audio/sound card(s), driver, sound server."#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "inxi --battery           # System battery info"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "dmesg | grep tty         # Serial port info"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )
        # =============+-------------------------+-------
        arg_2       =  "uname -a                 # Kernal Infolots of info with different flags"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "ifconfig                 # Show ip address... "#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

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


        """
        args = self.get_ddl_args()
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

# ============================================
class CommandNamesPass( commands_0.CommandABC ):
    """
    Commands to define names users and passwords id
    """
    def __init__( self,     ):
        """
        usual init
        """
        super().__init__()
        #rint( "CommandCopy.__init__()"  )
        self.name             = "CommandNamesPass names passwords pass words users computer id"

        self.build_key_words( self.name )   # must be here after rest of init

        self.command_string   = ""
        self.short_desc       = "Just starting implementation Names and passwords.... "
        #self.cmd_list          = None # put in build cmd with fstring ... !! local variable should be fine

        #self.shell_fn         = ""
        self.info             = self.short_desc
        self.info             = f"{self.info}\ncomputer name .... "
        #self.info             = f"{self.info}......\n"
        self.web_ref          = r"http://bulldog/mediawiki/index.php/Linux_CheatSheet#find_usb"
        self.set_py_env       = False
        self.cmd_fixed        = "# various commands in dropdown"

    # ----------------------------------
    def build_gui_frame( self, parent ):
        """
        return a frame
        http://bulldog/mediawiki/index.php/Linux_CheatSheet#find_usb
            fdisk -l    # usb info
            lsblk      # usb info

            gparted may have info as well

        """
        # ---- build the widget manager
        a_sync_combo            = sync_combo.SyncCombo()
        a_sync_combo.set_label_text( "Command", "Source", "Target", )
        a_sync_combo.arg_width  = gui.ARG_WIDTH
        self.a_sync_combo       = a_sync_combo

        # -------------+-------------------------+-------
        typically_0 = ["                         # Typically none", ]
        arg_needed  = ["                         # Arg needed", ]
        # ---- make the drop down values -- here with values that are tracable
        arg_1         = "z"  # hidden single value


        # =============+-------------------------+-------
        arg_2       =  "cinnamon-settings-users  # gui for user/password management"#no ,
        # -------------+-------------------------+-------
        arg_3       = typically_0

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "sudo adduser             # arg_2 is name of user"#no ,
        # -------------+-------------------------+-------
        arg_3       = ["{user name}              # ?????? ",
                       ]

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "who                      # who is logged on no arg_2"#no  , !
        # -------------+-------------------------+-------
        arg_3       =  typically_0

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "xed /etc/passwd          # who are user via password file, sudo to change"#no  , !
        # -------------+-------------------------+-------
        arg_3       = typically_0

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
class CommandFind( commands_0.CommandABC ):
    """
    Commands to find files and perhaps other stuff
    see help text

    """
    def __init__( self,     ):
        """
        usual init
        """
        super().__init__()
        self.name             = "CommandFind find where whereis locate"

        self.build_key_words( self.name )   # must be here after rest of init

        self.command_string   = ""
        self.short_desc       = "Just starting implementation of this name ... "

        self.info             = self.short_desc
        self.info             = f"{self.info}\ncomputer name .... "
        #self.info             = f"{self.info}......\n"
        self.web_ref          = r"http://bulldog/mediawiki/index.php/Linux_CheatSheet#xxxx"
        self.set_py_env       = False

    # ----------------------------------
    def build_gui_frame( self, parent ):
        """
        see ABC
        return a frame

            ?? expand to finding other stuff, disks usb.....
        """
        # ---- build the widget manager
        a_sync_combo            = sync_combo.SyncCombo()
        a_sync_combo.set_label_text( "Command", "Source", "Target", )
        a_sync_combo.arg_width  = gui.ARG_WIDTH
        self.a_sync_combo       = a_sync_combo

        # -------------+-------------------------+-------
        # typically_0 = ["                         # Typically none", ]
        # arg_needed  = ["                         # Arg needed", ]
        fn_or_pat   = ["                         # File name or pattern", ]
        # ---- make the drop down values -- here with values that are tracable
        arg_1       = "z"  # hidden single value

        # =============+-------------------------+-------
        arg_2       =  "find                     #  -> pattern to match"#no  , !
        # -------------+-------------------------+-------
        arg_3       = fn_or_pat

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "whereis                  #  -> program_name (not file name)"#no  , !
        # -------------+-------------------------+-------
        arg_3       = fn_or_pat

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "locate                   #  -> program_name (not file name)"#no  , !
        # -------------+-------------------------+-------
        arg_3       = fn_or_pat

        a_sync_combo.add_to_dict( arg_1,         # key 0
                                  arg_2,         # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "nemo                     # gui launch of file manager has search   "#no  , !
        # -------------+-------------------------+-------
        arg_3       = fn_or_pat

        a_sync_combo.add_to_dict( arg_1,       # key 0
                                  arg_2,       # key 1
                                  arg_3 )

        # =============+-------------------------+-------
        arg_2       =  "sudo nemo                # gui launch of file manager has search   "#no  , !
        # -------------+-------------------------+-------
        arg_3       = fn_or_pat

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

# ---- eof ==============================




