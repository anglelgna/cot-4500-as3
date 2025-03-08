# Angelina Alderman
# COP 4500
# Programming Assignment 3a

# Euler's Method

def slope(x,y):
	return x - y**2

def eulers(x0, x, n, counter = 0):
	w0 = 1
	h = (x - x0) / n
	while counter < n :
		w0 = w0 + h * slope(x0,w0)
		x0 = x0 + h
		counter += 1
	print(w0)
	return

# Runge-Kutta Method

def runge_kutta(x0, x, n, counter = 0):
	w0 = 1
	h = (x - x0) / n
	while counter < n :
		k1 = h * slope(x0,w0)
		k2 = h * slope(x0 + (h/2),w0 + (k1/2))
		k3 = h * slope(x0 + (h/2),w0 + (k2/2))
		k4 = h * slope(x0 + h, w0 + k3)
		w0 = w0 + (k1 + 2*k2 + 2*k3 + k4)/6
		x0 = x0 + h
		counter += 1
	print(w0)
	return

def main():
	eulers(0,2,10)
	print()
	runge_kutta(0,2,10)

if __name__ == "__main__":
	main()