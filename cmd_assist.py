# -*- coding: utf-8 -*-
###! /usr/bin/python3
#!python3
# above for windows ??
#     /usr/bin/python


"""
this is the main module for the cmd_assist app
built on clipboard app
some of lefover junk, clean as you go

"""

# put this at top of each app file:
# ------------------------------------------
if __name__ == "__main__":
    import main
    main.main()

# ------------------------------------------

import os
import logging
import sys
#import traceback
import importlib
import time
import datetime


#----- local imports
sys.path.append( "../rshlib" )     # ok in win and linux but only for development

sys.path.append("/media/sf_0000/python00/python3/_projects/rshlib" ) # for virt box mint
print( "remove sys.path.append, and copy over contents" )
#import line_style
import parameters
import gui
import os_values
from   app_global import AppGlobal


# ============================================
class App( ):
    """
    this class is the "main" or controller for the whole app
    to run see end of this file
    sort of the controller of an mvc app
    """
    def __init__( self,  q_to_splash, q_from_splash  ):
        """
        usual init for main app
        splash not working as desired, disabled
        splash screen which is of not help unless we sleep the init
        """
        self.app_name          = "Command Assistant 2"
        self.version           = "Ver 110: 2023 11 26.0"
        self.app_version       = self.version                 # this should be the name
        # clean out dead
        self.app_url           = None
        AppGlobal.controller   = self
        self.gui               = None

        self.q_to_splash       = q_to_splash

        self.restart( )

    # ----------------------------------
    def restart(self ):
        """
        use to restart the app without ending it
        this process can be very quick -- much quicker than a cold start
        this code is also an extension of __init__
        """
        print( "========= restart =================" ) # not logged until logging is turned on
        if not( self.gui is None ):
            self.gui.root.destroy()
            importlib.reload( parameters )    # should work on python 3 but sometimes does not

        # else:
        #     #self.q_to_splash
        #     pass

        self.parameters     = parameters.Parameters( )
            # open early as may effect other parts of code
        self.os_values      = os_values.OSValues( )

        #if  self.parameters.set_default_path_here:
             # Now change the directory to location of this file
#        if True:
#            py_path    = self.parameters.running_on.py_path
#
#            # retval = os.getcwd()
#            # print( f"Directory now            {retval}")
#
#            print( f"Directory now ( sw if not ''  {os.getcwd()} change to >>{py_path}<<")
#            if py_path != "":
#                os.chdir( py_path )

        self.config_logger()
        self.prog_info()
       # could combine with above ??

        self.gui            = gui.GUI( )  # gui references cmd processor and controller
        msg                 = ( "Error messages may be in log file, check it if "
                                 "problems -- check parmeters.py for logging level " )
        # print( msg )
        AppGlobal.print_debug( msg )
        self.logger.log( AppGlobal.fll, msg )
        self.polling_delta  = self.parameters.poll_delta_t

        self.starting_dir   = os.getcwd()    # or perhaps parse out of command line

        #msg       = "Now not turning on polling, code may be in place "
        #rint( msg )
        #AppGlobal.print_debug( msg )
        self.gui.bring_to_top( )
        self.gui.root.after( self.polling_delta, self.polling )

        msg       = "mainloop..."
        print( msg )
        AppGlobal.print_debug( msg )

        # ---- default command -- put where
        self.gui.activate_command_by_key( "CommandCopy"  )  # default command to open

        self.gui.root.mainloop()

        msg       = ".... mainloop done"
        print( msg )

    # ------------------------------------------
    def config_logger( self, ):
        """
        configure the python logger
        return change of state
        """
        #AppGlobal.logger_id     = "cmd_assist"                # wrong
        AppGlobal.logger_id     = self.parameters.logger_id
        logger                  = logging.getLogger( AppGlobal.logger_id )

        logger.handlers         = []

        logger.setLevel( self.parameters.logging_level )

        # create the logging file handler
        fh = logging.FileHandler( self.parameters.pylogging_fn )

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        # add handler to logger object -- want only one add may be a problem
        logger.addHandler(fh)
        msg  = "pre logger debug -- did it work"
        AppGlobal.logger.debug( msg )

        logger.info( "Done config_logger .. next AppGlobal msg" )
        #print( "configed logger", flush = True )
        self.logger      = logger   # for access in rest of class?
        AppGlobal.set_logger( logger )

        msg  = ( f"Message from AppGlobal.print_debug >> "
                 f"logger level in App = {self.logger.level} will show at level 10" )
        AppGlobal.print_debug( msg )

    # --------------------------------------------
    def prog_info( self,  ):
        """
        record info about the program to the log file
        """
        #logger_level( "util_foo.prog_info"  )
        fll         = AppGlobal.force_log_level
        logger      = self.logger
        logger.log( fll, "" )
        logger.log( fll, "============================" )
        logger.log( fll, "" )
        title       =  ( f"Application: {self.app_name} in "
                        f"mode {AppGlobal.parameters.mode} and version  "
                        f"{self.version}" )
        logger.log( fll, title )
        logger.log( fll, "" )

        if len( sys.argv ) == 0:
            logger.info( "no command line arg " )
        else:

            for ix_arg, i_arg in enumerate( sys.argv ):
                msg = f"command line arg + {str( ix_arg ) }  =  { i_arg })"
                logger.log( AppGlobal.force_log_level, msg )

        msg     = f"current directory {os.getcwd()}"
        logger.log( fll, msg  )

        start_ts     = time.time()
        dt_obj       = datetime.datetime.utcfromtimestamp( start_ts )
        string_rep   = dt_obj.strftime('%Y-%m-%d %H:%M:%S')
        logger.log( fll, "Time now: " + string_rep )
        # logger_level( "Parameters say log to: " +
        # self.parameters.pylogging_fn )
        # parameters and controller not available can ge fro logger_level

    # ----------------------------------
    def polling( self,  ):
        """
        poll for now delegate to build cmd
        protect with a try so polling does not crash the entire application -- "no matter what"
        """
        print( "polling defeated as intended" )

    # -----------------------------------
    def print_list( self, a_list  ):
        """
        what it says, just a little utility, read it.
        """
        for i_item in a_list:
            print( i_item )

    # ----------------- button call backs from gui
    def cb_about( self, ):
        """
        what it says -- about box
        """
        AppGlobal.about()

    # ----------------- button call backs from gui
    def cb_test( self, ):
        """
        what it says
        """
        print( "cb_test" )
        #a_commander   = commands.CommandTest_1()
        #a_commander   = commands.CommandLs()
        #self.gui.place_cmd_frame( a_commander.build_gui_frame )
        # pass this off to the gui

    # ----------------- button call backs from gui
    def cb_install_cmd_gui( self, a_commander ):
        """
        what it says
        ?? do we need this call
        """
        print( "cb_install_cmd_gui what for" )
        self.commander       = a_commander
        self.gui.commander   = a_commander
        self.gui.place_cmd_frame( a_commander.build_gui_frame )

    # ----------------------------------------------
    def os_open_logfile( self,  ):
        """
        used as callback from gui button
        """
        AppGlobal.os_open_txt_file( self.parameters.pylogging_fn )

    # ----------------------------------------------
    def os_open_dev_notes( self,  ):
        """
        used as callback from gui button
        """
        AppGlobal.os_open_txt_file( self.parameters.dev_notes_fn )

    # ----------------------------------------------
    def os_open_readme( self,  ):
        """
        used as callback from gui button !! change to use appglobal
        """
        AppGlobal.os_open_txt_file( AppGlobal.parameters.readme_fn  )

    # ----------------------------------------------
    def os_open_gui_log( self,  ):
        """
        used as callback from gui button !! change to use appglobal
        """
        AppGlobal.os_open_txt_file( AppGlobal.parameters.gui_text_log_fn  )


    # ----------------------------------------------
    def os_open_help( self,  ):
        """
        used as callback from gui button !! change to use appglobal
        """
        AppGlobal.os_open_help_file( AppGlobal.parameters.help_file )

    # ----------------------------------------------
    def open_txt_help( self,  ):
        """
        used as callback from gui button
        better in comman_0?
        """
        # self.commander       = a_commander
        file_name  = self.commander.name.split( " " )[0]
        file_name  = f"./help/{file_name.lower()}.txt"
        # name needs to be shortend to class name
        #rint( f"open_txt_help {file_name}")
        AppGlobal.os_open_help_file( file_name )

    # ----------------------------------------------
    def os_open_parmfile( self,  ):
        """
        used as callback from gui button  !! change to use appglobal
        """
        AppGlobal.os_open_txt_file( "parameters.py" )

# ------------------------------------------
def main():
    """
    we all know what this does
    """
    # a_app =
    App( None, None )

# ------------------------------------------
# if __name__ == "__main__":

#     #try:
#         #a_app = App( None, None )
#         main()
#     #except Exception as exception:
#        msg   = "exception in __main__ run the app -- it will end"
#        a_app.logger.critical( msg )
#        a_app.logger.critical( exception,  stack_info=True )
#            just where I am full trace back most info
#        raise
#
#    #finally:
#        print( "here we are done with clipboard" )
#        sys.stdout.flush()
#
# ======================= eof =======================






