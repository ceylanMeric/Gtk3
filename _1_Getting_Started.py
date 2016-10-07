import gi
gi.require_version('Gtk', '3.0')                                        # Make sure other gtk versions not loaded
from gi.repository import Gtk

win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)                              # Make sure program terminated
win.show_all()                                                          # when user click on x button

Gtk.main()                                                              # Gtk processing loop, it finish
                                                                        # when we close window

