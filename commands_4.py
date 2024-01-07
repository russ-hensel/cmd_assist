#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
just update file timestamp
import in commands.py  ... later make configurable

Implementation of commands
    these seem to be mostly for working with the
        copy of 3, perhaps should start over no contents yet

        --- consider launchers for file managers and text editors
        ---- include python dditors and simpler ide's

        editors

            xed
            https://phoenixnap.com/kb/best-linux-text-editors-for-coding
                xxx Sublime Text


            https://www.tecmint.com/best-open-source-linux-text-editors/
                 11. Bluefish
                 16. Notepad++
                 19. Brackets Text Editor
                 mousepad
                 21. Lite Editor    -- easy to extend in lua
CudaText is a
24. Medit Text Editor


           =  [
                    r"gedit",
                    r"xed",
                    r"leafpad",
                    r"leafpad",
                    r"mousepad",


        file managers

            my file finder ??


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
class CommandEditFiles( commands_0.CommandABC ):
    """
    what it says

atom
bluefish
brackets text editor
geany                 ide
jed editor
leafpad
lite editor
micro text editor
mousepad
nano
notepad++
notepadqq
visual studio code    ide
idle
l3afpad

    """
    def __init__( self,     ):
        """
        usual init

        sudo xed /etc/hosts
        """
        super().__init__()
        print( "CommandEditFiles.__init__()"  )
        # ----------------------+---------------------+-------
        self.name             = "CommandEditFiles      >>>>>>>>>>>>>>>lots of editors for text file editing, edit"
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
        a_file_list = ["/etc             # ",
                       "~      # home ",
                       "/home/russ/Desktop ",
                       "/home/russ/       #   " ,
                       "  # just a blank for you to optional fill",
                       ]

        a_file_list = [ "choose a file            # identify other machines",
                        "/etc/hosts               # identify other machines",
                        "/etc/samba/smb.conf      # samba config file ",
                        "/etc/sudoers             # config for sudo",
                        "/etc/dhcpcd.conf         # network ip address",
                        "/etc/network/interfaces  # config net interfaces",
                       ]

        # ---- make the drop down values -- here with values that are tracable
        arg_1       = "z"

        # ---- atom
        # -------------+-------------------------+-------
        arg_2       =  "atom               #        "
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

        # ---- leafpad     l3afpad
        # -------------+-------------------------+-------
        arg_2       =  "l3afpad               # optinally use sudo   "#no  , !
        arg_3       = a_file_list

        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,           # key 0
                                  arg_2,           # key 1
                                  arg_3 )

        # ---- mousepad similar to l3afpad
        # -------------+-------------------------+-------
        arg_2       = "mousepad                #   gui editor in l3afpad family"
        arg_3       = a_file_list

        a_sync_combo.add_to_dict( arg_1,          # key 0
                                 arg_2,           # key 1
                                 arg_3 )

        # ---- idle ligtweight python gui ide
        # -------------+-------------------------+-------
        arg_2       = "idle                #   ligtweight python gui ide"
        arg_3       = a_file_list

        a_sync_combo.add_to_dict( arg_1, arg_2, arg_3 )

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

#------------------------------------------
class CommandManageFiles( commands_0.CommandABC ):
    """
    what it says
 nano
 atom
 Visual Studio Code    ide
 Geany                 ide
 Notepadqq
 JED Editor
 Leafpad
 Micro Text Editor
Bluefish
Notepad++
Brackets Text Editor
mousepad
Lite Editor

-- easy to extend in lua
    """
    def __init__( self,     ):
        """
        usual init

        4pane
        dolphin
        double_cmd_gtk
        konqueor
        nautilus
        nemo
        spacefm
        thunar

        """
        super().__init__()
        print( "CommandManageFiles.__init__()"  )
        # ----------------------+---------------------+-------
        self.name             = "CommandManageFiles      <<<<<<lots of file managers to manage / browse files: copy delete "
        self.build_key_words( self.name  )

        self.command_string   = "edit"
        self.short_desc       = "Manage files"

        self.info             = "This will edit text files\n"
        self.info             = f"{self.info}often used to make it executable\n"
        #self.info             = f"{self.info}......\n"
        self.web_ref          = r"http://bulldog/mediawiki/index.php/Linux_CheatSheet"
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
        a_file_list = ["/etc             # ",
                       "~      # home ",
                       "/home/russ/Desktop ",
                       "/home/russ/       #   " ,
                       "  # just a blank for you to optional fill",
                       ]

        # ---- make the drop down values -- here with values that are tracable
        arg_1       = "z"

        # ---- 4pane
        arg_2       =  "4pane               # two pannel editor "#no  , !
        arg_3       = a_file_list

        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,           # key 0
                                  arg_2,           # key 1
                                  arg_3 )

        # ---- atom
        arg_2       =  "atom               # gui editor "   #no  , !
        arg_3       = a_file_list

        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,           # key 0
                                  arg_2,           # key 1
                                  arg_3 )


        # ---- dolphin
        arg_2       =  "dolphin               #   "#no  , !
        arg_3       = a_file_list

        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,           # key 0
                                  arg_2,           # key 1
                                  arg_3 )

        # ---- double_cmd_gtk  doublecmd
        arg_2       =  "doublecmd               #   "      #no  , !
        arg_3       = a_file_list
        # -------------+-------------------------+-------
        a_sync_combo.add_to_dict( arg_1,           # key 0
                                  arg_2,           # key 1
                                  arg_3 )

        """
                # ---- konqueor
                # -------------+-------------------------+-------
                arg_2       =  "konqueor                # launch gui file manager"
                arg_3       = a_file_list

                a_sync_combo.add_to_dict( arg_1,          # key 0
                                         arg_2,           # key 1
                                         arg_3 )


        """

        # ---- konqueor -----------------------+-------
        # ------------------------------------+-------

        arg_2       = "konqueor                #  gui file manager or web browser "
        arg_3       = a_file_list

        a_sync_combo.add_to_dict( arg_1,          # key 0
                                 arg_2,           # key 1
                                 arg_3 )

        # ---- nautilus
        # ------------------------------------+-------
        arg_2       = "nautilus               #  gui file manager"
        arg_3       = a_file_list

        a_sync_combo.add_to_dict( arg_1,          # key 0
                                 arg_2,           # key 1
                                 arg_3 )


        # ---- nemo
        # ------------------------------------+-------
        arg_2       = "nemo                   #  gui file manager"
        arg_3       = a_file_list

        a_sync_combo.add_to_dict( arg_1,          # key 0
                                 arg_2,           # key 1
                                 arg_3 )
        # ---- spacefm
        # ------------------------------------+-------
        arg_2       = "spacefm                #  gui file manager"
        arg_3       = a_file_list
        a_sync_combo.add_to_dict( arg_1,  arg_2,     arg_3 )


        # ------------------------------------+-------
        arg_2       = "thunar                 #  gui file manager"
        arg_3       = a_file_list
        a_sync_combo.add_to_dict( arg_1,  arg_2,     arg_3 )

        # ----  /usr/bin/dragonfly
        # -------------+-------------------------+-------
        arg_2       = "/usr/bin/dragonfly               # gui file manager    in python"
        arg_3       = a_file_list
        a_sync_combo.add_to_dict( arg_1,  arg_2,     arg_3 )

        # ---- finish off ----------------------------
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


# # ============================================
# class CommandNetxxxx( commands_0.CommandABC ):
#     """
#     what it says

#     """
#     def __init__( self,     ):
#         """
#         usual init

#         sudo xed /etc/hosts
#         """
#         super().__init__()
#         #rint( "CommandCopy.__init__()"  )
#         # ----------------------+---------------------+-------
#         self.name             = "CommandNet 3  net network tcp ip address nmap zenmap samba config logs"
#         self.build_key_words( self.name  )

#         #self.command_string   = "edit"
#         self.short_desc       = "Work with the network"

#         self.info             = "Work with the network/n"
#         self.info             = f"{self.info}configure tcpip addresses\n"
#         #self.info             = f"{self.info}......\n"
#         self.web_ref          = r"http://bulldog/mediawiki/index.php/Linux_CheatSheet#copy_files"
#         self.set_py_env       = False

#         #self.cmd_fixed        = "xed # name of editor in parameter.py"

#     # ----------------------------------
#     def build_gui_frame( self, parent ):
#         """
#         return a frame
#         Nmap Cheat Sheet and Pro Tips | HackerTarget.com
#             https://hackertarget.com/nmap-cheatsheet-a-quick-reference-guide/

#         NMAP Tutorial to Scan IP Network Range - Step-By-Step with Examples
#             https://www.networkstraining.com/nmap-scan-ip-range/

# add start and stop samba
# samba logs   nemo  /var/log/samba  # some by tcpip adr # use sudo to modify...  <filebrowse> ??

#   Unable to find the Domain Master Browser name WORKGROUP<1b> for the workgroup WORKGROUP.
#   Unable to sync browse lists in this workgroup.
# [2022/11/25 10:53:37.926923,  0] ../../source3/nmbd/nmbd_browsesync.c:354(find_domain_master_name_query_fail)
#   find_domain_master_name_query_fail:
#   Unable to find the Domain Master Browser name WORKGROUP<1b> for the workgroup WORKGROUP.
#   Unable to sync browse lists in this workgroup.

#   !! password to clipboard


#     >>sudo systemctl stop smbd
#     >> sudo systemctl enable smbd
#     >> sudo systemctl start smbd

# Running a quick NMAP scan to inventory my network | Enable Sysadmin
# https://www.redhat.com/sysadmin/quick-nmap-inventory

# Host Discovery | Nmap Network Scanning
# https://nmap.org/book/man-host-discovery.html

# Nmap Cheat Sheet and Pro Tips | HackerTarget.com
# https://hackertarget.com/nmap-cheatsheet-a-quick-reference-guide/

# How to use Nmap to scan for open ports
# https://www.techtarget.com/searchsecurity/feature/How-to-use-Nmap-to-scan-for-open-ports

# Port Specification and Scan Order | Nmap Network Scanning
# https://nmap.org/book/man-port-specification.html

# Command-line Flags | Nmap Network Scanning
# https://nmap.org/book/port-scanning-options.html

# How To Install Zenmap In Linux Mint [2021] » Nude Systems
# https://nudesystems.com/how-to-install-zenmap-in-linux-mint-20-x-2021/

# How to install Zenmap Nmap GUI on Ubuntu 20.04 LTS - Linux Shout
# https://www.how2shout.com/linux/install-zenmap-nmap-gui-on-ubuntu-20-04-lts-linux/




#         """
#         # ---- build the widget manager
#         a_sync_combo             = sync_combo.SyncCombo()
#         a_sync_combo.arg_width   = gui.ARG_WIDTH
#         a_sync_combo.set_label_text( "z", "Command:", "Command Arg:", )
#         self.a_sync_combo        = a_sync_combo
#         # -------------+-------------------------+-------
#         a_file_list = ["/etc/hosts               # identify other machines",
#                        "/etc/samba/smb.conf      # samba config file ",

#                        "/etc/network/interfaces  # config net interfaces",
#                        #"nmap  # probe network for network clients",
#                        ]
#         typically_0 = ["                         # Typically none", ]

#         # ---- make the drop down values -- here with values that are tracable
#         arg_1       = "z"   #z supresses arg_1

#         # =============+-------------------------+-------
#         arg_2       =  "ifconfig                 # show network settings"#no  , !
#         arg_3       = typically_0
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,           # key 0
#                                   arg_2,           # key 1
#                                   arg_3 )
#         #hostname [options] [new_host_name]
#         # =============+-------------------------+-------
#         arg_2       =  "hostname                 # add options here?"
#         # -------------+-------------------------+-------
#         arg_3       = ["-h                       # for help",
#                        "                         # blank to display current hostname",
#                        "{new_hostname}           # to change the hostname",
#                        ]
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,          # key 0
#                                  arg_2,           # key 1
#                                  arg_3 )

#         #sudo xedit /etc/hosts
#         # =============+-------------------------+-------
#         arg_2       =  "sudo <texteditor>        # start text editor"
#         # -------------+-------------------------+-------
#         arg_3       = ["/etc/hosts               # configuration file",
#                        ]
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,          # key 0
#                                  arg_2,           # key 1
#                                  arg_3 )
#         # ---- sudo nmap   192.168.0-254



#         # =============+-------------------------+-------
#         arg_2       =  "nmap      # basic command"
#         # -------------+-------------------------+-------
#         arg_3       = ["192.168.1.1-254              # usual range of home net ports",
#                        "-h",                           # help.. long
#                        "www.testhostname.com          # Scan a host",
#                        "-F 192.168.1.1          # Fast Scan 100 most common ports (Fast)",
#                        "-sP 192.168.0.0/24     # Discover Live IPs in a subnet",
#                        "-A 192.168.0.0/24      # Detect OS and Services Running in a subnet   ",
#                        "Webhelp -- will not work - nmap prefix",]
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,          # key 0
#                                  arg_2,           # key 1
#                                  arg_3 )

#         # =============+-------------------------+-------
#         arg_2       =  "sudo systemctl    #start and stop samba"  # start samba step 1
#         # -------------+-------------------------+-------
#         arg_3       = ["enable smbd       # start samba step 1",
#                        "start smbd        # start samba step 2",
#                        "stop smbd         # stop samba",]
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,          # key 0
#                                  arg_2,           # key 1
#                           arg_3 )

#         #  <filebrowse> ??
#         # =============+-------------------------+-------
#         arg_2       =  "sudo nemo  /var/log/samba  # edit (sudo) see samba logs"  # start samba step 1
#         # -------------+-------------------------+-------
#         arg_3       = ["#lots of files, inc. one for each tcpip ",
#                        ]
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,          # key 0
#                                  arg_2,           # key 1
#                           arg_3 )

#         # =============+-------------------------+-------
#         arg_2       =  "xdg-open https://bulldog:10000/samba/?xnavigation=1  # webmin"  # start samba step 1
#         # -------------+-------------------------+-------
#         arg_3       = ["#must have webmin installed for this to work",
#                        ]
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,          # key 0
#                                  arg_2,           # key 1
#                           arg_3 )

#         # ===========================
#         # ---- finish build
#         a_frame = self.build_gui_3d_frame_from_args(
#                                        parent,
#                                        a_sync_combo     = a_sync_combo,
#                                        command_str      = None,
#                                        short_desc       = None,
#                                        arg_1_label      = "Command:",
#                                        w_type_1         = None,
#                                        arg_2_label      = "Command Arg:",
#                                        w_type_2         = None,   )

#         AppGlobal.gui.gui_style.style_frame( a_frame )

#         AppGlobal.gui.button_browse_file_src.config( state = Tk.DISABLED )   # Tk.DISABLE  Tk.NORMAL
#         AppGlobal.gui.button_browse_file_dst.config( state = Tk.DISABLED )
#         AppGlobal.gui.button_browse_dir_src.config(  state = Tk.DISABLED )
#         AppGlobal.gui.button_browse_dir_dst.config(  state = Tk.DISABLED )

#         if self.set_py_env:
#             print( "do set_py_env")

#         return a_frame

#     # ----------------------------------
#     def build_command( self, add_echo = True, add_newline = False ):
#         """
#         return a command as a single string
#         add_echo    see code
#         add_newline   see code

#         """
#         return self.build_command_1_2( add_echo = add_echo, add_newline = add_newline )

# # ============================================
# class CommandGrepxxx( commands_0.CommandABC ):
#     """
#     what it says

#     """
#     def __init__( self,     ):
#         """
#         usual init

#         sudo xed /etc/hosts
#         """
#         super().__init__()
#         #rint( "CommandCopy.__init__()"  )
#         # ----------------------+---------------------+-------
#         self.name             = "CommandGrep   find filter   just a draft for grep of commandsz"
#         self.build_key_words( self.name  )

#         #self.command_string   = "edit"
#         self.short_desc       = "grep finds things in streams, files...  "

#         self.info             =  self.short_desc
#         #self.info             = f"{self.info}configure tcpip addresses\n"
#         #self.info             = f"{self.info}......\n"
#         self.web_ref          = r"http://bulldog/mediawiki/index.php/Linux_CheatSheet#copy_files"
#         self.set_py_env       = False

#         #self.cmd_fixed        = "xed # name of editor in parameter.py"

#     # ----------------------------------
#     def build_gui_frame( self, parent ):
#         """
#         return a frame
#         Nmap Cheat Sheet and Pro Tips | HackerTarget.com
#             https://hackertarget.com/nmap-cheatsheet-a-quick-reference-guide/

#         NMAP Tutorial to Scan IP Network Range - Step-By-Step with Examples
#             https://www.networkstraining.com/nmap-scan-ip-range/


# Grep Command in Unix with Simple Examples
# https://www.softwaretestinghelp.com/grep-command-in-unix/

# 15 Practical Grep Command Examples In Linux / UNIX
# https://www.thegeekstuff.com/2009/03/15-practical-unix-grep-command-examples/

# networking - Getting strange IP Address from router - Super User
# https://superuser.com/questions/704637/getting-strange-ip-address-from-router

# networking - arp is displaying weird IP addresses in the 169 range - Ask Ubuntu
# https://askubuntu.com/questions/912020/arp-is-displaying-weird-ip-addresses-in-the-169-range


# tp-link Deco Whole-Home Wi-Fi System Instruction Manual - Manuals+
# https://manuals.plus/tp-link/deco-whole-home-wi-fi-system-manual#how_do_i_set_up_my_deco

# 656692.pdf
# https://www.bhphotovideo.com/lit_files/656692.pdf


#         """
#         # ---- build the widget manager
#         a_sync_combo             = sync_combo.SyncCombo()
#         a_sync_combo.arg_width   = gui.ARG_WIDTH
#         a_sync_combo.set_label_text( "z", "Command:", "Command Arg:", )
#         self.a_sync_combo        = a_sync_combo
#         # -------------+-------------------------+-------
#         # what does file list do doc in early command_n
#         a_file_list = ["/etc/hosts               # identify other machines",
#                        "/etc/samba/smb.conf      # samba config file ",

#                        "/etc/network/interfaces  # config net interfaces",
#                        #"nmap  # probe network for network clients",
#                        ]
#         typically_0 = ["                         # Typically none", ]


#         # you need 2 top level dict items to get a 3d drop down
#         # ---- make the drop down values -- here with values that are tracable
#        # arg_1       = "z"   #z supresses arg_1

#         # >>>>>>>>>>>>>>>>>>>>>>
#         arg_1       = "grep                      # the basic command"      # the basic command

#         # =============+-------------------------+-------
#         arg_2       =  "\"is\"                   # text to search for, note quotes "
#         arg_3       = ["/media_id.txt            # name of file to search",
#                        "/*.txt                   # pattern for file"]
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,           # key 0
#                                   arg_2,           # key 1
#                                   arg_3 )


#         arg_1       = "grep                      # the basic command"      # the basic command

#         # =============+-------------------------+-------
#         arg_2       =  "-i \"is\"                  # -i case insensitive text  "
#         arg_3       = ["/media_id.txt             # name of file to search",
#                        "\"*.txt\"                  # pattern for file"]
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,           # key 0
#                           arg_2,           # key 1
#                           arg_3 )


#         # >>>>>>>>>>>>>>>>>>>>>>
#         arg_1       = "grep  -i                    # the basic command"      # the basic command

#         # =============+-------------------------+-------
#         arg_2       =  "\"{a regular exp}\"                  # ? at most 1,* 0 to N, {N} exactly N "
#         arg_3       = ["/media_id.txt            # name of file to search",
#                        "/*.txt                   # pattern for file"]
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,           # key 0
#                           arg_2,           # key 1
#                           arg_3 )

#         arg_1       = "grep                      # the basic command"      # the basic command

#         # =============+-------------------------+-------
#         arg_2       =  "\"i*"                    # ? at most 1,* 0 to N, {N} exactly N "
#         arg_3       = ["/media_id.txt            # name of file to search",
#                        "/*.txt                   # pattern for file"]
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,           # key 0
#                           arg_2,           # key 1
#                           arg_3 )
#         # ---- hostname [options] [new_host_name]


#         # # ---- finish build
#         # a_frame = self.build_gui_3d_frame_from_args(
#         #                                parent,
#         #                                a_sync_combo     = a_sync_combo,
#         #                                command_str      = None,
#         #                                short_desc       = None,
#         #                                arg_1_label      = "Command:",
#         #                                w_type_1         = None,
#         #                                arg_2_label      = "Command Arg:",
#         #                                w_type_2         = None,   )

#         # ---- finish build copy from copy
#         a_frame = self.build_gui_3d_frame_from_args(
#                                        parent,
#                                        a_sync_combo     = a_sync_combo,
#                                        command_str      = None,
#                                        short_desc       = None,
#                                        arg_1_label      = None,
#                                        w_type_1         = None,
#                                        arg_2_label      = "label for arg_2",
#                                        w_type_2         = None,   )

#         AppGlobal.gui.gui_style.style_frame( a_frame )

#         AppGlobal.gui.button_browse_file_src.config( state = Tk.DISABLED )   # Tk.DISABLE  Tk.NORMAL
#         AppGlobal.gui.button_browse_file_dst.config( state = Tk.DISABLED )
#         AppGlobal.gui.button_browse_dir_src.config(  state = Tk.DISABLED )
#         AppGlobal.gui.button_browse_dir_dst.config(  state = Tk.DISABLED )

#         if self.set_py_env:
#             print( "do set_py_env -- grep probably not ")

#         print( ">>>>>> check sync", self.a_sync_combo.check() )

#         print( self.a_sync_combo )

#         return a_frame

#     # ----------------------------------
#     def build_command( self, add_echo = True, add_newline = False ):
#         """
#         return a command as a single string
#         add_echo    see code
#         add_newline   see code

#         """
#         return self.build_command_1_2_3( add_echo = add_echo, add_newline = add_newline )

# # ============================================
# class CommandQemuxxx( commands_0.CommandABC ):
#     """
#     what it says

#     """
#     def __init__( self,     ):
#         """
#         usual init -- register commands.py  CommandsDict __init__


#         """
#         super().__init__()
#         #rint( "CommandCopy.__init__()"  )
#         # ----------------------+---------------------+-------
#         self.name             = "CommandQemu      virtual virt machine box qemu"
#         self.build_key_words( self.name  )

#         #self.command_string   = "edit"
#         self.short_desc       = "Work with virtual machines"

#         self.info             = "Work with virtual machines\n"
#         self.info             = f"{self.info}configure tcpip addresses\n"
#         #self.info             = f"{self.info}......\n"
#         self.web_ref          = r"http://bulldog/mediawiki/index.php/Linux_CheatSheet#copy_files"
#         self.set_py_env       = False

#         #self.cmd_fixed        = "xed # name of editor in parameter.py"

#     # ----------------------------------
#     def build_gui_frame( self, parent ):
#         """
#         return a frame
#     * >> sudo systemctl status libvirtd.service   #

#     * >>  sudo virsh net-list --all   # check status  -- network ??
#     export an ova
#     import an ova
#         tar -xvf <image-name>.ova
#         qemu-img convert <image-name>-disk001.vmdk <image-name>.qcow2 -O qcow2


#     create
#     launch



#         """
#         # ---- build the widget manager
#         a_sync_combo             = sync_combo.SyncCombo()
#         a_sync_combo.arg_width   = gui.ARG_WIDTH
#         a_sync_combo.set_label_text( "z", "Command:", "Command Arg:", )
#         self.a_sync_combo        = a_sync_combo
#         # -------------+-------------------------+-------
#         # a_file_list = ["/etc/hosts               # identify other machines",
#         #                "/etc/samba/smb.conf      # samba config file ",

#         #                "/etc/network/interfaces  # config net interfaces",
#         #
#         typically_0_str  = " # Typically none"
#         typically_0_list = [typically_0_str, ]


#         # ---- make the drop down values -- here with values that are tracable
#         arg_1       = "sudo systemctl"

#         # =============+-------------------------+-------
#         arg_2       =  "status                #"  # , !
#         arg_3       = [ "libvirtd.service    # status of what "   ]
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,           # key 0
#                                   arg_2,           # key 1
#                                   arg_3 )
#         #hostname [options] [new_host_name]
#         # =============+-------------------------+-------
#         arg_1       =  "sudo virsh net-list --all   # check status  -- network"
#         arg_2       =  typically_0_str
#         # -------------+-------------------------+-------
#         arg_3       = typically_0_list
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,          # key 0
#                                  arg_2,           # key 1
#                                  arg_3 )

#         # =============+-------------------------+-------
#         arg_1       =  "#import an ova"
#         arg_2       =  typically_0_str
#         # -------------+-------------------------+-------
#         arg_3       = typically_0_list
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,          # key 0
#                                  arg_2,           # key 1
#                                  arg_3 )

#         # =============+-------------------------+-------
#         arg_1       =  "#create"
#         arg_2       =  typically_0_str
#         # -------------+-------------------------+-------
#         arg_3       = typically_0_list
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,          # key 0
#                                  arg_2,           # key 1
#                                  arg_3 )


#         # ---- launch ..
#         # =============+-------------------------+-------
#         arg_1       =  "#launch"
#         arg_2       =  typically_0_str
#         # -------------+-------------------------+-------
#         arg_3       = typically_0_list
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,          # key 0
#                                  arg_2,           # key 1
#                                  arg_3 )

#         #sudo xedit /etc/hosts
#         # =============+-------------------------+-------
#         arg_1       =  "#xxx"
#         arg_2       =  "sudo <texteditor>        # start text editor"
#         # -------------+-------------------------+-------
#         arg_3       = ["/etc/hosts               # configuration file",
#                        ]
#         # -------------+-------------------------+-------
#         a_sync_combo.add_to_dict( arg_1,          # key 0
#                                  arg_2,           # key 1
#                                  arg_3 )
#         # ---- finish build
#         a_frame = self.build_gui_3d_frame_from_args(
#                                        parent,
#                                        a_sync_combo     = a_sync_combo,
#                                        command_str      = None,
#                                        short_desc       = None,
#                                        arg_1_label      = "Command:",
#                                        w_type_1         = None,
#                                        arg_2_label      = "Command Arg:",
#                                        w_type_2         = None,   )

#         AppGlobal.gui.gui_style.style_frame( a_frame )

#         AppGlobal.gui.button_browse_file_src.config( state = Tk.DISABLED )   # Tk.DISABLE  Tk.NORMAL
#         AppGlobal.gui.button_browse_file_dst.config( state = Tk.DISABLED )
#         AppGlobal.gui.button_browse_dir_src.config(  state = Tk.DISABLED )
#         AppGlobal.gui.button_browse_dir_dst.config(  state = Tk.DISABLED )

#         if self.set_py_env:
#             print( "do set_py_env")

#         return a_frame

#     # ----------------------------------
#     def build_command( self, add_echo = True, add_newline = False ):
#         """
#         return a command as a single string
#         add_echo    see code
#         add_newline   see code

#         """
#         # return self.build_command_1_2( add_echo = add_echo, add_newline = add_newline )
#         # build command from arg1 and arg2
#         # self.build_command_1_2
#         # ex:
#         # return self.build_command_1_2( add_echo = add_echo, add_newline = add_newline )

#         print( "build_command_0_1_2" )
#         args        = self.get_ddl_args()

#         cmd_prefix  = self.build_prefix()

#         cmd_list    = cmd_prefix + [ f"{args[0]} {args[1]} {args[2]}",
#                                      "exec bash",
#                                      ]

#         if add_echo:
#             cmd_list    = self.build_echo( cmd_list )

#         if add_newline:
#             cmd_str     = "\n".join( cmd_list )   # may still want to stip exec bash  !!

#         else:
#             cmd_str     = ";".join( cmd_list )
#             cmd_str     = f'gnome-terminal -- bash -c "{cmd_str}"'

#         #rint( cmd_str )
#         #rint( cmd_list )

#         return cmd_str




# ---- =================== eof ==============================

