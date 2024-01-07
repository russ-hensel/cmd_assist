# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 17:21:23 2020

now instance but better class or module


"""
#local
from app_global import AppGlobal


class OSValues( object ):
    """
    current plan is to create in AppGlobal so could just pas in which os
    why not do one os then overwrite
    """
    # ----------------------------------------
    def __init__(self, ):


       AppGlobal.os_values  = self

       if AppGlobal.parameters.os_win:    # new object to hold all these inc valid tabs
           msg    = "os is windows"
           print( msg )
           self.path_sep     = "\\"
           self.list_cmd    = "dir"
           self.copy_cmd    = "copy"
           self.del_cmd     = "del"

       else:
           self.path_sep     = "/"

           self.list_cmd    = "ls"
           self.copy_cmd    = "cp"
           self.del_cmd     = "del"


       if AppGlobal.parameters.os_win:
           print( "!! should have different setup or in parameters ?? ")  # move to os_values

           self.path_sep              = "\\"


           self.list_cmd_flag_values   = [ " | none",
                                            "-a -h | generally useful  ",
                                            "-a | show hidden",
                                            "-h | human readable",
                                            "-a | show hidden",

                                           ]

           self.file_list        = [  "*.*", "*.xyz", "*.txt", "*.pdf" ]

           self.path_list        = [ "",
                                      r"D:\Russ",     # do not end with / it is auto put in ( but !! we should fix that )
                                      "D:\\Russ\\0000\\",     # do not end with / it is auto put in ( but !! we should fix that )
                                      r"\bin",
                                      r"\etc",   r"\etc\mysql",
                                      r"\media", r"\media\russ",   ]

           self.cc_value_list   = [ "ifconfig | info on network",
                                            "sudo apt-get update | keep up to date 1  ",
                                            "sudo apt-get upgrade  | keep up to date 2",
                                            "htop | human readable",
                                            "-a | show hidden",
                                           ]


       else:

           self.path_sep              = "/"

           self.list_cmd_flag_values   = [ " | none",
                                            "-a -h | generally useful  ",
                                            "-a | show hidden",
                                            "-h | human readable",
                                            "-a | show hidden",

                                           ]


           self.cc_value_list   = [ "ifconfig | info on network",
                                            "sudo apt-get update | keep up to date 1  ",
                                            "sudo apt-get upgrade  | keep up to date 2",
                                            "htop | human readable",
                                            "-a | show hidden",
                                           ]




           self.file_list        = [  "*.*", "*.txt", "*.pdf" ]

           self.path_list        = [ "",
                                      "~",     # do not end with / it is auto put in ( but !! we should fix that )
                                      "/bin",
                                      "/etc",   "/etc/mysql",
                                      "/media", "/media/russ",   ]



# =======================================


if __name__ == "__main__":
    #----- run the full app
    import cmd_assist
    cmd_assist.main()
    # app  = clip_board.App( None, None )

