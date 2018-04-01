import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class CalendarWindow(Gtk.Window):
	grid = Gtk.Grid()
	calendar = Gtk.Calendar()
	day = Gtk.ListStore(str)

	def on_day_selected(self, calendar):
		year, month, day = calendar.get_date()
		month = month + 1
		print("Date selected: %i%i%i" % (year, month, day))
		calendar.hide()
		# day.show()

	def on_day_selected_double_click(self, calendar):
		print("Double click")

	def initialize_calendar(self):
		print("in init")
		self.calendar.connect("day-selected", self.on_day_selected)
		self.calendar.connect("day-selected-double-click", self.on_day_selected_double_click)
		self.grid.add(self.calendar)

	def initialize_event_list(self):
		self.day.append(["No Events to Show"])
		listView = Gtk.TreeView(self.day)
		renderer = Gtk.CellRendererText()
		column = Gtk.TreeViewColumn("Events", renderer, text=0)
		listView.append_column(column)
		self.grid.attach(listView, 1, 0, 1, 1)

	def __init__(self):
		# initialize window
		Gtk.Window.__init__(self, title="Calendar")
		self.connect("destroy", Gtk.main_quit)

		# initialize container for the layout
		self.add(self.grid)

		# initialize the calendar that is displayed
		self.initialize_calendar()

		# initialize the event list
		self.initialize_event_list()

win = CalendarWindow()
win.show_all()

Gtk.main()
