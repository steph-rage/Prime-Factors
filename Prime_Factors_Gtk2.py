import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def factorize(*args):
	factors = []
	try:
		number = int(my_number.get())		
		def find_factors(n):
			max_check = max(int(n**0.5), 2)
			test = 0
			for i in range(2, max_check+1):
				if n%i == 0:
					factors.append(i)
					test = 1
					if n != i:
						find_factors(int(n/i))
					break
			if test == 0:
				factors.append(n)
		find_factors(number)
		my_prime_factors.set(factors)
	except ValueError:
		pass



class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title = "Prime Factorization")

        self.button = Gtk.Button(label = "Find Factors")
        self.button.connect("clicked", self.on_button_clicked)
        self.add(self.button)

    def on_button_clicked(self, widget):
        print("Hello World")

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()