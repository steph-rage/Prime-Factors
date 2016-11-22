from tkinter import *
from tkinter import ttk


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


root = Tk()
root.title("Prime Factorization")

canvas = Canvas(root)
canvas.grid(column = 0, row = 0, sticky = (N, W, E, S))
canvas.create_oval(10, 10, 50, 50)

mainframe = ttk.Frame(root, padding = "3 3 12 12")		
mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))			
mainframe.columnconfigure(0, weight = 1)							
mainframe.rowconfigure(0, weight = 1)	

my_number = StringVar()
my_prime_factors = StringVar()

number_entry = ttk.Entry(mainframe, width = 10, textvariable = my_number)
number_entry.grid(column = 2, row = 1, sticky = (W, E))

ttk.Label(mainframe, textvariable = my_prime_factors).grid(column = 2, row = 3, sticky = (W, E))       
ttk.Button(mainframe, text = "Factorize!", command = factorize).grid(column = 3, row = 5, sticky = W)

ttk.Label(mainframe, text = "Pick an integer: ").grid(column = 1, row = 1, sticky = W)
ttk.Label(mainframe, text = "Prime Factors: ").grid(column = 1, row = 3, sticky = W)



for child in mainframe.winfo_children(): child.grid_configure(padx = 5, pady = 5)		
number_entry.focus()

root.bind('<Return>', factorize)				

root.mainloop()			
