import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class WindowBoxes(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Layout Window")

        self.box = Gtk.Box(spacing=6)
        self.add(self.box)

        self.button1 = Gtk.Button(label="Button1")
        self.button1.connect("clicked", self.on_button1_clicked)
        self.box.pack_start(self.button1, True, True, 0)

        self.button2 = Gtk.Button(label="Button2")
        self.button2.connect("clicked", self.on_button2_clicked)
        self.box.pack_start(self.button2, True, True, 0)

    def on_button1_clicked(self, widget):
        print("Button1 is clicked")

    def on_button2_clicked(self, widget):
        print("Button2 is clicked")

class WindowGrid(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Grid Window")

        grid = Gtk.Grid()
        self.add(grid)

        button1 = Gtk.Button(label="Button1")
        button2 = Gtk.Button(label="Button2")
        button3 = Gtk.Button(label="Button3")
        button4 = Gtk.Button(label="Button4")
        button5 = Gtk.Button(label="Button5")
        button6 = Gtk.Button(label="Button6")

        grid.add(button1)
        grid.attach(button2, 1,0,2,1)
        grid.attach_next_to(button3, button1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(button4, button3, Gtk.PositionType.LEFT, 3, 5)
        grid.attach(button5, 3, 1, 1, 1)                                    # x ve y position go like 0,1,2,3
                                                                            # last two are x ve y width
        # grid.attach_next_to(button6, button5, Gtk.PositionType.RIGHT, 1, 1)

# win = WindowBoxes()
win = WindowGrid()
win.connect("delete-event", Gtk.main_quit)
win.show_all()

Gtk.main()


