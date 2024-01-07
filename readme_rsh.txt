

this file   D:\Russ\0000\python00\python3\_projects\cmd_assist\readme_rsh.txt

Developer Notes ( by rsh ) for the cmd_assist application --
     Assist in writing commands for linux and perhaps windows

these are fairly rough notes, including scratch work.  If you are not rsh, please
author your own file

Search:

        ----next
        -ver109
        -ver       or version

        ====Collaboration
        ====Links

----next
    add a command to run a python program in a conda environment
          need  conda env, default dir and program name   -- default to main.py

    put password for sudo in clipboard




--------ver109 ---------
    why: a tiny bit of cleanup for gitlab
    need to add ping, fping.... hpaing 
    
    look at stuff for arduino

--------ver108 ---------
        why:      108 delete dead code then move on
        status:   framework runs commands ** below should work if not purfectly
        !! make run also do preview
        !! on bulldog, terminal does not always come to top
        !! dd disk destroyer
        !! Qemu
    	** put command in clipboard
        ** remove excess prints
        *! auto select first command upon start -- but not left highlighted
        !! new command for network
        !! new command for process control
        !! update -- check and recheck until final review

        ** put man in help txt file -- but working through each command
        !! check ddl labels

        --- 1
        !! command test 1 -- and leave until we need a test
        ** command ls
        ** command pip
        ** command conda
        ** command system control
        ** command copy             -- sync combo ok but style a bit out of date
        ** command apt

        --- 2
        **  command edit file
        **  command misc
        **  command hw
        **  command name pass
        **  command find

        --- 3
        CommandNet
        CommandGrep
        CommandQemu

        CommandSamba    add it
        sudo xed /etc/samba/smb.conf


        !! improve short description
        !! add widget targets for files and directories ... make sure work
        ** add auto select on changed contents
        ?? make retain state ( perhaps just save the gui frame and replace )
        ?? add a reset button

        !! get set python environment working

        !! help history   ??

        !! move focus to key words ... when   ...
        !! parameters have a text to push into gui_ext  ....
        **  finish or work on gui styling -- until it comes up again

          mess with gnome-terminal and profiles
          new parameters
              !! style parameters      -- but finish gui_style first
              ** self.shell_editor      = "geany"
              !! profile for terminal
              !! options string for terminal ( profile might go there )




===================== plans and versions ===========

===================== gui plan =====================

..................... command selection ......

as it is with keyword


..................... command gui .....................

probably better documented in command_test

fields
    short help or description

    base command

    arg1 name and entry fields
        arg 1 may end in comment that will be stripped prior to run

    arg2 name and entry fields

        if arg2 depends on arg1 dropdown they will be coordinated

    short desc     {short description}
    base command   {base command possibly with comment}    may be suppressed if in arg1

    arg1 label     {arg1 possibly with comment, may be a ddl }

    arg2 label     {arg2 possibly with comment, may be a ddl }

    web reference list with go button

=============== plans and versions ===========


!! get key word working
** CommandLs works
** CommandPip works
!! get a couple of commands working
!! a round of gui detail cleanup, no new features
** default dir, arg1 arg2 on file and path all working
!! look at old gui files and incorporate
?? echo may have issues with embedded quotes need to look into it
?? issues with file... with embedded spaces   use \\x20 or similar to escape ?  -- or a late tweak ?
** add at least 2 more commands
!! reduce junk code again
** using gui_ext from rsh_lib ...
just one tab? with search interface on tab page in future
build like stuff db .. for now just single frame

!! add a cd before each command to put terminal in a particular directory use
    for all terminal commands

** make a scrolling list box or look for one in clipboard
------------------------


!!how to add a command

================ how to add a command ===============
        links
        gui plan

add
Managing Multiple Python Versions With pyenv – Real Python
https://realpython.com/intro-to-pyenv/#what-about-a-package-manager

set a path in linux

add run shell

add history of selected commands

Python Data Type: Dictionary - Exercises, Practice, Solution - w3resource
https://www.w3resource.com/python-exercises/dictionary/

next:

    !! have text_editor become a thing instead of gedit or specific editors


--------------------------


I have given up Windows for Linux, but why should you care?  Well I have an
opportunity for some of us to learn/pratice linux and python at the same time.
I have started a large app the still needs to grow a lot.  It is agraphical
app that allows you to search for a command that might be useful and then
shows you the command broken into editable parts.  You adjust the command
as you which and then the app will open a terminal and run the command.
This can be useful to learn the command or jog yor memory for a command that
you have not used in awhile.
As I learn more commands or variants of the command I add them to the app,
generally simple operation after I get the command to work.  Can I interest
any of you in collaboration ( or even informed comemt? )  You can find
it on git hub at:

Contact me if you have any problem getting it running.

( I am running it under Linux Mint, Anaconda, Spyder and Python 10.  There is nothing
  particular about the enveironmen that I am aware of. )



----------------------

To initialize your shell, run

    $ conda init <SHELL_NAME>

Currently supported shells are:
  - bash
  - fish
  - tcsh
  - xonsh
  - zsh
  - powershell


=====Collaboration

Collaboration:

I am looking for collaborators for a GUI ( tkinter ) application I have worked on for some time
and have partly working. This might be an opportunity to:

    * Learn more python.
    * Learn more linux
    * Help create a useful application.

Application Purpose:

    GUI application to issue commands for the linux terminal so that you do not
    have to remember the details of the commands.
    Can also be used as a application launcher.

    I will limit my post to this, for more info:

        Russell Hensel / cmd_assist · GitLab
        *>url  https://gitlab.com/russhensel/cmd_assist

I will be posting this on a couple of different sites.  Contact me if interested.

Status:

    Generally works.  Coverage of linux very incomplete.  Repository is for developers
    to download and run as if a work in progress, no pip install.....

Some Features:

    * Search for commands based on key words.
    * Commands come in sets which are logically grouped.
    * Commands are fully editable.
    * Commands are issued to the terminal ( or to preview, or to clipboard, or file ).

Some Command Details:

    * Commands are organized both around the purpose ( like list files ) and
      syntax ( like ls )

    * Commands are broken into several parts each of which is editable, and may
      have a comment.  The parts appear in dropdown lists for easy selection.

    * When commands are run the parts are assembled, comments removed, and the
      full command is passed to a terminal to be run.

Run the Code.

    * Download the repository into your python environment ( I use conda/spyder )
    * Run main.py and install dependencies until errors end.
          ( know ones include: pyperclip ... )

Some Remarks on the code:

    * App does not have a specification so it evolves as ideas occur and is actually used.
      Some ideas are tried and abandoned
    * Code is populated with dubious comments and dead or incomplete code.  but
      app mostly works.
    * I usually treat code as a learning experience in python so the code reflects that.
    * I often refactor, but only as time an inclination allow.  Plans tend to
      evolve faster than I can implement.
    * About 250K of .py files
    * Work most needed restricted to files of about 30k, high similarity with
      existing code.
    * I format with much more white space then pep8 and like it, any new work
      could be done with a similar formatting or, say, black.  I do not want to
      reformat old code unless it needs to be substantially changed.
    * Tests are good, but currently I do not use very much.
    * I am a duck typer, not a type hints sort of coder.

Contributing:

    * I am open to any help the is helpful.  Which means?
    * A start might be to extend to new linux commands and functional areas.  I
      usually work on it as I am in the process of doing something new ( to me )
      in Linux ( nothing recently, windows is my most often used os ).
    * I do not really use git for control, just keep the code there.  This
      could change.
    * A good place to start would be with a new command module ( similar to commands_1.py
      say commands_8.py ).
    * I can help you get started, we could meet on zoom.
    * Addition of tests if that is your interest.
    * Extend to work on windows with powershell?.

    * Contributions not currently important ( to me ).
        * Reformatting
        * Type hints ( but fine in new code )
        * Minor changes that do not extend the application.


I will be posting this on a couple of different sites.  Contact me if interested, Russ.




=====================links  ==========
*'''[https://itsfoss.com/apt-command-guide/ Using apt Commands in Linux [Complete Guide] - It's FOSS ]'''
*'''[https://www.2daygeek.com/linux-check-system-hardware-manufacturer-model-serial-number/ Checking Linux system hardware manufacturer info | 2DayGeek ]'''
-------------------------- terminal


Command line options
    *>url  http://www.fifi.org/doc/gnome-terminal/html/gnome-terminal/C/options.html

Terminal
    *>url  https://help.gnome.org/users/gnome-terminal/stable/

Ubuntu Manpage: gnome-terminal — is a terminal emulation application.
    *>url  https://manpages.ubuntu.com/manpages/bionic/man1/gnome-terminal.1.html

gnome-terminal - man pages section 1: User Commands
    *>url  https://docs.oracle.com/cd/E88353_01/html/E37839/gnome-terminal-1.html

gnome terminal what to use instead of --command deprecated - Google Search
    *>url  https://www.google.com/search?q=gnome+terminal+what+to+use+instead+of+--command+depricated&client=firefox-b-1-d&sxsrf=ALeKk01OIIwjGngPgPZ_AJYVr20rK6JMEw%3A1627776584847&ei=SOYFYZqPM6S6gge1o7OIAQ&oq=gnome+terminal+what+to+use+instead+of+--command+depricated&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsANKBAhBGABQrMwBWKDkAWCh5gFoAXACeACAAWWIAZgGkgEEMTEuMZgBAKABAcgBCMABAQ&sclient=gws-wiz&ved=0ahUKEwia0_OoxI7yAhUkneAKHbXRDBEQ4dUDCA0&uact=5

gnome terminal - how can I open a extra console and run a program in it with one command? - Ask Ubuntu
    *>url  https://askubuntu.com/questions/974756/how-can-i-open-a-extra-console-and-run-a-program-in-it-with-one-command

command line - Open a new terminal and source scripts - Ask Ubuntu
    *>url  https://askubuntu.com/questions/965828/open-a-new-terminal-and-source-scripts/967720#967720

command line - Start Specific Terminal on Startup - Ask Ubuntu
    *>url  https://askubuntu.com/questions/965681/start-specific-terminal-on-startup/968541#968541

best air purifiers - Neeva
    *>url  https://neeva.com/search?q=best%20air%20purifiers&c=All&src=InternalSearchLink#

Termination Shock: A Novel - Kindle edition by Stephenson, Neal. Literature & Fiction Kindle eBooks @ AmazonSmile.
    *>url  https://smile.amazon.com/dp/B08WLWC6GZ?pd_rd_i=B08WLWC6GZ&pd_rd_w=L9xjU&pf_rd_p=13a52819-8981-44ba-b78d-7f8162352729&pd_rd_r=b62c8201-fdfe-43fe-8413-3912939288ea&pd_rd_wg=ZecDj&ref_=pe_24562050_597543700_ssub

AmazonSmile: Solip:System (Hardwired Series) eBook: Williams, Walter Jon: Kindle Store
    *>url  https://smile.amazon.com/dp/B006UP5CD4?pd_rd_i=B006UP5CD4&pd_rd_w=XBrnp&pf_rd_p=168701ac-af6b-4e9a-a453-71c0e33bd02e&pd_rd_r=b62c8201-fdfe-43fe-8413-3912939288ea&pd_rd_wg=ZecDj&ref_=pe_24562050_597543700_ssub

AmazonSmile: Wormhole (The Rho Agenda Book 3) eBook: Phillips, Richard: Kindle Store
    *>url  https://smile.amazon.com/dp/B007TBSLR2?pd_rd_i=B007TBSLR2&pd_rd_w=XBrnp&pf_rd_p=168701ac-af6b-4e9a-a453-71c0e33bd02e&pd_rd_r=b62c8201-fdfe-43fe-8413-3912939288ea&pd_rd_wg=ZecDj&ref_=pe_24562050_597543700_ssub

TheProf | Syncthing
    *>url  http://127.0.0.1:8384/#


==================== links for gnome-terminal

https://docs.oracle.com/cd/E88353_01/html/E37839/gnome-terminal-1.html
http://multignometerm.sourceforge.net/web/doc/options.html
http://manpages.ubuntu.com/manpages/xenial/man1/gnome-terminal.1.html
https://askubuntu.com/questions/75222/how-can-i-start-gnome-terminal-at-a-particular-directory
https://unix.stackexchange.com/questions/407831/how-can-i-launch-gnome-terminal-remotely-on-my-headless-server-fails-to-launch
https://stackoverflow.com/questions/8247706/start-script-when-gnome-starts-up
https://help.gnome.org/users/gnome-terminal/stable/
https://docs.oracle.com/cd/E88353_01/html/E37839/gnome-terminal-1.html
https://www.systutorials.com/docs/linux/man/1-gnome-terminal/
https://en.wikipedia.org/wiki/GNOME_Terminal

================ how to add a command ===============

see commands_n.py   where n is constantly increasing

    make a new child class

commands.py

    add to commands dict

================= scratch ========


# ============================================
class CommandConda( commands_0.CommandABC ):
    """
    think it used to work but not now conda not found for some reason
         terminal not initialized
         works manually in terminal later
    what it says
    no sudo !!

    You need to run those commands on a console
         with administrative rights, in windows,
         or with a sudo before them on linux.

    I tend to run these three lines in order every time I need to update:

    conda update conda -y
    conda update --all -y
    conda update qt pyqt spyder -y

    -----
    Updating Spyder

    If you installed Spyder through Anaconda (recommended),
    WinPython, MacPorts, or your system package manager,
    update using those same methods. With Anaconda,
    just run (in Anaconda Prompt if on Windows,
              otherwise in your system terminal):

    conda update anaconda
    conda update spyder
    conda -V # conda version
    update install
        >> conda update conda # to update conda and other stuff

    Environments

    Create a virtual environment for your project

        In the terminal client enter the following where yourenvname is the name
        you want to call your environment, and replace x.x with the
         Python version you wish to use. (To see a list of available
         python versions first, type conda search "^python$" and press enter.)

    conda create -n yourenvname python=x.x anaconda

    * >> conda remove -n yourenvname -all   # delete env = yourenvname

    >> conda info --envs # list environments, * for current
    >> conda activate environment_name
    >> conda remove -n environment_name -all # delete env = environment_name


    """
    def __init__( self,     ):
        """
        usual init

        """
        super().__init__()

        self.name             = "CommandConda conda python install module, enviroment"
  ..... see code
