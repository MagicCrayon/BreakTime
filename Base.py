#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk

class Base:
    
    def __init__(self):

	self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.set_title("BreakTime")
        self.window.set_border_width(10)
        self.window.set_size_request(600,400)
        
        
        self.window.connect("destroy", self.destroy)
        self.button = gtk.Button("Time To Take a Break!")
        self.button.connect("clicked", self.destroy, None)
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
        self.window.add(self.button)
        
        self.button.show()
        self.window.show()
      
    def destroy(self, widget, data=None):
      gtk.main_quit()
 

    def main(self):
        gtk.main()


