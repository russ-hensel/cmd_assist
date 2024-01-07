# -*- coding: utf-8 -*-

"""
   parameters    for  cmd_assist.py
   some junk and unimplemented parms, !! clean up
   unfortunately this is a moving target, will try to keep documentation up to date
   choose_mode is the first method as you may use it most often to change
   modes  .... start with new_user_mode, you can then mess with it or copy it
   or other parts of the parameter file to make new modes

"""


# -------- put this at top of each app file:
if __name__ == "__main__":
    import main
    main.main()

# ------------------------------------------



import logging
from   app_global import AppGlobal
import os

import running_on

# ========================================
class Parameters( object ):
    """
    manages parameter values: use like ini file but it is code
    """
    # -------
    def choose_mode( self ):
        """
        typically choose one mode and if you wish add the plus_test_mode
        if you comment all out you get the default mode which should
        run, perhaps while limping
        """
        self.new_user_mode()

        #self.millhouse_1_mode()

        #self.russ_1_mode()

        # --- add on for testing, as desired
        self.plus_test_mode()

    # -------
    def plus_test_mode( self ):
        """
        scratch mode to add tests to other modes when testing
        an add on mode
        """
        self.mode              = self.mode + " + test"  # change with care
        self.make_test_tab      = True
        self.logging_level     = logging.DEBUG
        self.poll_delta_t      = 500            # how often we poll for clip changes, in ms, think my computer works well as low as 10ms
        self.sudo              = "bulldog"
        # self.snippets_fn        = ["./snipsand/snippetts_test.txt", "./snipsand/snippetts_example.txt" ,"./snipsand/snippetts_1.txt"]
        # #self.snippets_fn        = "./snipsand/snippetts_test.txt"
        self.icon               = r"./clipboard_b.ico"

    # -------
    def new_user_mode( self ):
        """
        for a new user to customize, as shipped pretty much a copy of russ_1
        an example mode
        new users should start here for making a mode, you may want to make a copy for reference
        see .default_mode() for some documentation of the variables.
        """
        self.mode               = "New_user"

        #self.logging_level      = logging.Parameters( )DEBUG

        # ----- snip or example files
#        self.snip_file_fn       = r"snips_file_test.txt"
#        self.snip_file_fn       = r"snip_files_nov_18.txt"
#        self._read_snip_files_( self.snip_file_fn )

        # ----- snippets
        self.snippets_fn        = "./snipsand/snippetts_example.txt"
        self.snippets_sort      = True

    # ------->> More methods:  one for each mode

    # -------
    def running_on_tweaks(self,  ):
        """
        not a mode, a tweak, see documentation
        use running on tweaks as a more sophisticated  version of os_tweaks and computer name tweaks which
        may replace them
        """
        computer_id    =   self.running_on.computer_id

        if computer_id == "smithers":
            self.win_geometry       = '1450x700+20+20'      # width x height position
            self.ex_editor          =  r"D:\apps\Notepad++\notepad++.exe"
            self.db_file_name       =  "smithers_db.db"

        elif computer_id == "millhouse":
            self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"
            #self.win_geometry   = '1300x600+20+20'
            self.db_file_name       =  "millhouse_db.db"

        elif computer_id == "theprof":
            self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"
            self.db_file_name       =  "the_prof_db.db"
            #self.snip_file_path     = r"D:\Russ\0000\python00\python3\_examples"
            self.win_geometry       = '1450x700+20+20'      # width x height position

        elif computer_id == "bulldog":
            self.ex_editor          =  r"gedit"
            self.db_file_name       =  "bulldog_db.db"

        elif computer_id == "bulldog-mint-russ":
            self.ex_editor          =  r"xed"
            self.db_file_name       =  "bulldog_db.db"

        else:
            print( f"In parameters: no special settings for computer_id {computer_id}" )
            if self.running_on.os_is_win:
                self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"
            else:
                self.ex_editor          =  r"leafpad"    # linux raspberry pi maybe

    # -------
    def os_tweaks( self ):
        """
        this is an subroutine to tweak the default settings of "default_mode"
        for particular operating systems
        you may need to mess with this based on your os setup
        """
        if  self.os_win:
            pass
            self.icon               = r"./clipboard_b.ico"    #  very dark greenhouse this has issues on rasPi
            self.icon               = r"./clipboard_b_red_GGV_icon.ico"     #  looks same as clipboard_b_red_gimp.ico
#            self.icon               = r"./clipboard_b_red2.gif"  #  looks same as clipboard_b_red_gimp.ico
            self.icon               = r"./clipboard_b_red_gimp.ico"    # pretty visible

            #self.icon              = None                    #  default gui icon

        else:
            pass

        self.gui_style          = "linux"

    # -------
    def computer_name_tweaks( self ):
        """
        this is an subroutine to tweak the default settings of "default_mode"
        for particular computers.  Put in settings for you computer if you wish
        these are for my computers, add what you want ( or nothing ) for your computes
        !! use computer name or id ??
        """
        #rint( f"computer_name_tweaks {self.computername}", flush = True )

        if self.computername == "smithers":
            self.win_geometry       = '1250x700+20+20'      # width x height position
            self.ex_editor          =  r"c:\apps\Notepad++\notepad++.exe"    # russ win 10 smithers

        elif self.computername == "millhouse":
            self.ex_editor          =  r"C:\apps\Notepad++\notepad++.exe"    # russ win 10 millhouse
            self.win_geometry       = '1300x700+50+5'          # width x height position
            self.pylogging_fn       = "cmd_assist.py_log"   # file name for the python logging
            #self.snip_file_fn       = r"C:\Russ\0000\python00\python3\_projects\clipboard\Ver3\snips_file_auto.txt"
            # need to associate with extension -- say a dict
            #self.snip_file_command  = r"C:\apps\Notepad++\notepad++.exe"  #russwin10   !! implement

        elif self.computername  == "theprof":
            self.ex_editor          =  r"c:\apps\Notepad++\notepad++.exe"    # russ win 10 smithers

    # -------
    def __init__( self, ):
        """
        Init for instance, usually not modified, except perhaps debug stuff ( if any )... but use plus_test_mode()
        may be down in listing because it should not be messed with.
        """
        AppGlobal.parameters       = self   # register for global access
        self.default_mode()
        self.os_tweaks()
        self.running_on_tweaks()
        self.choose_mode()

        #rint( "from __init__ of parameters:")
        #rint( self ) # for debugging

    # ------->> default mode, always call
    # -------
    def default_mode( self ):
        """
        sets up pretty much all settings
        documents the meaning of the modes
        call first, then override as necessary
        good chance these settings will at least let the app run
        """
        self.mode              = "default"  # name your config, so it will show in app tilte, may be changed later

        #--------------- automatic settings -----------------
        self.running_on   = running_on.RunningOn
        self.running_on.gather_data()

        # some of the next all?? should be moved over to RunningOn
        self.running_on.log_me( logger       = None,
                                logger_level = 10,
                                print_flag   = False )

        self.py_path                   = self.running_on.py_path   # this is the path to the main.py program

        self.set_default_path_here     = True  # to make app location the default path in the app, Think True may always be best.
        # above may be tricky to reset, but we may have the original dir in running on
        # no easy way to ovride this ??
        if  self.set_default_path_here:     # Now change the directory to location of this file

            py_path    = self.running_on.py_path

            print( f"Directory: (  >>{os.getcwd()}<< switch if not '' to >>{py_path}<<")
            if py_path != "":
                os.chdir( py_path )

        self.our_os             = self.running_on.our_os          # so we know our os  could be "linux" or our_os == "linux2"  "darwin"....
        self.os_win             = self.running_on.os_win          # boolean True if some version of windows
        self.computername       = self.running_on.computername    # a name of the computer if we can get it
        self.opening_dir        = self.running_on.opening_dir     # directory where app was opened, not where it resides

        self.platform           = self.our_os           # sometimes it matters which os but this value is redundant

        # ---- appearance
        self.icon               = r"clipboard_c.ico"    # icon for running app -- not used in linux
        self.icon               = r"gsd-xrandr.png"
        self.id_color           = "blue"                # to id the app - not implemented yet
        self.default_scroll     = True              # message area auto scrolls

        self.win_geometry       = '1500x800+20+20'      # size, position  of app on opening
        self.win_geometry       = '1200x800+20+20'      # width x height position  x, y
        self.win_geometry       = '1600x800+20+20'      # width x height position  x, y
        self.gui_style          = "linux"

        self.pylogging_fn       = "cmd_assist.py_log"   # file name for the python logging
        self.logging_level      = logging.DEBUG        # logging level DEBUG will log all captured text ! or logging.INFO
        #self.logging_level      = logging.INFO
        self.logger_id          = "cmd_assist"         # id of app in logging file

        # ---- new for cmd_assist -------------------

        self.defaut_key_words   = 'testpython'   #  "test"   #"python"

        self.make_test_tab      = False        # if True make the test tab else not
        self.db_file_name       = "default_db.db"

        self.default_dir        = "./"
        self.default_file       = "a_file.txt"

        self.file_initialdir    = "./"
        self.file_title         = "Select a file",
        self.file_filetypes     = (("all files","*.*"),("jpg","*.jpg"),)     # (("database files","*.db"),("all files","*.*"))

        self.dir_initialdir     = "./"
        self.dir_title          = "Select a directory",
        self.dir_filetypes      = (("all files","*.*"),("jpg","*.jpg"),)

        self.py_env_with        = "conda"   # will need other vaiables

        # ---- subs
        self.conda_fn           = "/home/russ/anaconda3/bin/conda"
        self.pip_fn             = "/home/russ/anaconda3/bin/pip"    #   "/usr/bin/pip"
        self.subsution_list     =  [ ( "<conda>",       self.conda_fn ),
                                     ( "<pip>",         self.pip_fn ),
                                     ( "<nautilus>",    "/usr/bin/nautilus" ),
                                     # ( "<texteditor>",  "leafpad" ),
                                     ( "<texteditor>",  "leafpad" ),

                                    ]                          # ?? also consider dict
        # ---- file names

        #self.snip_editor       = r"C:\apps\Anaconda3\Scripts\thonny.exe"  # editor used for opening snip files pick one that ->
                                                                          # will open file form command line

        # this is the name of a program: its executable with path info.
        # to be used in opening an external editor
        self.ex_editor         =  r"D:\apps\Notepad++\notepad++.exe"    # russ win 10

        # if we are writing scratch files to run in a shell or similar.
        self.scratch_bat       =  r"scratch.bat"   # rel filename
        self.scratch_py        =  r"scratch.py"    # rel filename

        self.shell_editor      = "geany"
        self.shell_file_name   = "cmd_shell.sh"

        self.run_py            =  r"python.exe"    # program to run *>py commands  !! not yet implemented
        self.readme_fn         = "readme_rsh.txt"
        self.gui_text_log_fn   = "gui.py_log"
        # extensions of files for text editing
        self.text_extends = [  ".txt",  ".rsh", ".ino", ".py", ".h" , ".cpp", ".py_log", ".log", ]  # include the dot!

        # ========================= buttons initial state  ======================

        #------------------------- default the named check box's see gui.py  ---------------
        # not really implemented now... in process
        self.cmd_on            = 1     # 1 is checked or on else 0
        self.auto_url_on       = 0
        self.star_cmd_on       = 0
        self.exe_file_on       = 0
        #... not all may be named see gui.py

        #------------------------- default the named radio buttons see gui.py  ---------------
        #self.rb_num_on          = 0      # which radio button on, number is not nice, but easy !! is working ???
        #... not all may be named see gui.py

        #self.include_wiki_buttons  = True    # experimental flag, leave True

        # may not be best for text help file
        # help file can be web ( open with browser ), or txt ( open with self.editor ) or anything else ( will try to shell out may or may not work )
        self.help_file       =  "help.txt"   #  >>. this is the path to our main .py file self.py_path + "/" +
        self.help_file       =  "https://opencircuits.com/index.php?title=Command_Assistant_Help_File"   # can be url or a local file -- change for clipboard !!
        self.help_file       =  "http://bulldog/mediawiki/index.php/Command_Assistant_Help_File #copy_files"
        self.txt_help_flag      = True

        self.dev_notes_fn       = "readme_rsh.txt" # or None name of text file

        self.command_help       =  "http://bulldog/mediawiki/index.php/Linux_CheatSheet"
        self.help_fn            = self.help_file    # old phase out

        self.help_path          = f".{os.sep}help{os.sep}"    # for local text file include trailing /

        # #---------------------------------------------------

        #self.transform         = "off"       #["","",]  !! is what

        self.poll_delta_t      = 200            # how often we poll for clip changes, in ms, think my computer works well as low as 10ms

        #------------- -------------------------------
        self.venv_enviroments   = [   ]                            # path to environment

# -----------------------------------
    def __str__( self,   ):
        """
        sometimes it is hard to see where values have come out this may help if printed.
        not complete, add as needed -- compare across applications and code above
        """
        a_str = f">>>>>>>>>>* parameters (some) *<<<<<<<<<<<<"
        a_str = f"{a_str}\n   mode                {self.mode}"

        a_str = f"{a_str}\n   logger_id           {self.logger_id}"
        a_str = f"{a_str}\n   logging_level       {self.logging_level}"
        a_str = f"{a_str}\n   pylogging_fn        {self.pylogging_fn}"

        # a_str = f"{a_str}\n   snippets_fn         {self.snippets_fn}"
        # a_str = f"{a_str}\n   snippets_sort       {self.snippets_sort}"

        # a_str = f"{a_str}\n   snip_file_fn        {self.snip_file_fn}"
        # a_str = f"{a_str}\n   snip_file_sort      {self.snip_file_sort}"
        # a_str = f"{a_str}\n   snip_file_command   {self.snip_file_command}"


        #a_str = f"{a_str}\n   snip_editor         {self.snip_editor}"
        a_str = f"{a_str}\n   scratch_bat         {self.scratch_bat}"
        a_str = f"{a_str}\n   scratch_py          {self.scratch_py}"
        a_str = f"{a_str}\n   run_py              {self.run_py}"
        a_str = f"{a_str}\n   ex_editor           {self.ex_editor}"
        #---------------------+-------------------+-----------------------------
        a_str = f"{a_str}\n   scratch_bat         {self.scratch_bat}"
        a_str = f"{a_str}\n   scratch_py          {self.scratch_py}"

        a_str = f"{a_str}\n   win_geometry        {self.win_geometry}"
        a_str = f"{a_str}\n   computername        {self.computername}"
        a_str = f"{a_str}\n   our_os              {self.our_os}"
        a_str = f"{a_str}\n   os_win              {self.os_win}"

        #---- sort
        a_str = f"{a_str}\n   computer_id         {self.running_on.computer_id}"
        a_str = f"{a_str}\n   ex_editor           {self.ex_editor}"
        a_str = f"{a_str}\n   icon                {self.icon}"
        a_str = f"{a_str}\n   gui_style           {self.gui_style}"
        a_str = f"{a_str}\n   py_path             {self.py_path}"
        a_str = f"{a_str}\n   set_default_path_here   {self.set_default_path_here}"

        a_str = f"{a_str}\n   id_color             {self.id_color}"
        # a_str = f"{a_str}\n   search_many_list     {self.search_many_list}"
        a_str = f"{a_str}\n   poll_delta_t         {self.poll_delta_t}"

        a_str = f"{a_str}\n   and so much more... \n\n"
        return a_str

# =================================================
if __name__ == "__main__":

    # ------------------------------------------

    #----- run the full app
    import cmd_assist
    cmd_assist.main()
    # app  = clip_board.App( None, None )

# =================== eof ==============================



