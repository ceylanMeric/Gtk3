import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ListBoxWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="ListBoxWindow")
        self.set_border_width(10)                                               # To understand, put Gtk.Window
                                                                                # instead of self
        box_outher = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)   # Orientation = yönlendirme
        self.add(box_outher)                                                    # With self.add, we add box to Gtk.window

        listbox = Gtk.ListBox()                                                 # In this block code
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)                      # we say our box consist boxlist
        box_outher.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()                                                  # In this block of code
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)      # boxrow inside horizontal(yatay) box
        row.add(hbox)                                                           # inside vertical box
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        label1 = Gtk.Label("Automatic Date & Time", xalign=3)
        label2 = Gtk.Label("Requires internet access", xalign=0)
        vbox.pack_start(label1, True, True, 0)
        vbox.pack_start(label2, True, True, 0)

        switch = Gtk.Switch()
        switch.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switch, False, True, 0)

        listbox.add(row)





win = ListBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
