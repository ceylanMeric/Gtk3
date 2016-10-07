import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):                                                 # Inherit from Gtk.Window

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")                      # Start init for superclass
        self.button = Gtk.Button(label="Click Here")                        # Create button
        self.label = Gtk.Label(label="Hello World", angle=25,
                               halign=Gtk.Align.END)

        # widget = Gtk.Box()
        # print(dir(widget.props))                                            # Visible properties

        self.button.connect("clicked", self.on_button_clicked)              # Connect button and function action for clicking.
        self.add(self.button)                                               # Add button to window
#        self.add(self.label)

    def on_button_clicked(self, widget):
        print("Hello World")

win = MyWindow()                                                            # Create window with class
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
