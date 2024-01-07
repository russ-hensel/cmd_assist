#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 18:36:55 2020

@author: russ
"""
    # ------------------------------------------
    def _make_test_tab( self, parent_frame,  ):
        """
        frame that contains radio buttons etc that control transformations
        may go to application.transform( self, in_text,  ):
        """

        #self.install_tab_values  = tab_values.InstallTabValues()
        self.test_tab_values  = tab_value_obj.AdamTabValues()
        tab_values               = self.test_tab_values # shorter faster ref

        a_frame          = Tk.Frame( parent_frame, bg = "green" ,  borderwidth = 2, relief = "solid" )
        #a_frame.grid_columnconfigure( 0, weight = 1, ) # sticky = "uniform"    ) #sticky = Tk.W + Tk.E )
        a_frame.grid_columnconfigure( 0, weight=1, uniform="fred")
        a_frame.grid_columnconfigure( 1, weight=1, uniform="fred")
        a_frame.grid_columnconfigure( 2, weight=1, uniform="fred")
        a_frame.grid_columnconfigure( 3, weight=1, uniform="fred")

        ix_col  = 0
        ix_row  = 0

        # lables to define grid
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

        #   path
        a_widget = Tk.Label( a_frame, text = "Path:",  anchor="w" ) #   relief = RAISED,  )
        a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W ) #rowspan = 2, columnspan = 2 )
        ix_col   += 1

        values        = AppGlobal.os_values.path_list
        a_widget      = Tk.ttk.Combobox( a_frame, values = values, state = 'normal', width = 90 )
        a_widget.set( values[0] )

        tab_values.src_path_widget = a_widget    # if just one use src
        a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W    ) # rowspan = 2, columnspan = 2 )
        ix_col   += 1

        #  files
        a_widget = Tk.Label( a_frame, text = "File:",  anchor = "w" ) #   relief = RAISED,  )
        a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W ) #rowspan = 2, columnspan = 2 )
        ix_col   += 1
        values    = AppGlobal.os_values.file_list
        #source_file_list        = ["", "*.*", "*.txt", "*.pdf" ]
        a_widget      = Tk.ttk.Combobox( a_frame, values = values, state = 'readonly' )
        self.install_cmd_file_widget   = a_widget
        tab_values.src_file_widget = a_widget   # if just one use src
        a_widget.set( values[0] )
        a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W    ) # rowspan = 2, columnspan = 2 )
        ix_col   += 1

        ix_row   += 1
        ix_col   = 0

        a_widget = Tk.Label( a_frame, text = "Cmd Flags:",  anchor="w" ) #   relief = RAISED,  )
        a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W ) #rowspan = 2, columnspan = 2 )
        ix_col   += 1

        a_widget      = Tk.ttk.Combobox( a_frame, values = self.list_cmd_flag_values, state = 'readonly' )
        self.install_flag_widget   = a_widget   # ?? this stuff might go in a control dict
        tab_values.op_flag_widget  = a_widget

        a_widget.set( self.list_cmd_flag_values[0] )
        a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W    ) # rowspan = 2, columnspan = 2 )
        ix_col   += 1

        ix_row   += 1
        ix_col   = 0

        # --=== command
        a_widget = Tk.Label( a_frame, text = "Cmd",  anchor="w", ) #   relief = RAISED,  )
        a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W ) #rowspan = 2, columnspan = 2 )
        ix_col   += 1
        # wrong self.list_cmd_widget   = a_widget

        a_widget      = Tk.Entry( a_frame,   state = 'normal',  width = 100, )
        a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W    ) # rowspan = 2, columnspan = 2 )

        tab_values.cmd_widget    = a_widget

        ix_col   += 1

        ix_row   += 1
        ix_col   = 0

        # --------
        #
        a_widget = Tk.Label( a_frame, text = "Operation:",  anchor = "w" ) #   relief = RAISED,  )
        a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W ) #rowspan = 2, columnspan = 2 )
        ix_col   += 1

        a_widget      = Tk.ttk.Combobox( a_frame, values = self.list_ops, state = 'readonly' )
        # self.install_op_widget   = a_widget
        a_widget.set( self.list_ops[0] )
        tab_values.op_widget    = a_widget
        a_widget.grid( row = ix_row, column = ix_col, sticky = Tk.W    ) # rowspan = 2, columnspan = 2 )
        ix_col   += 1

        a_widget = Tk.Button( a_frame , width = 10, height = 1, text = "List..." )
        self.intsall_op_button  = a_widget
        tab_values.op_button    = a_widget
        a_widget.config( command = AppGlobal.build_cmd.do_list_cmd )
        a_widget.grid( row = ix_row, column = ix_col, rowspan = 1, sticky = Tk.E + Tk.W + Tk.N + Tk.S )
        ix_col   +=  1

        return a_frame

