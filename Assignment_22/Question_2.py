class Circle:
	PI = 3.14
	def __init__(self):
		self.Radius = 0
		self.Area = 0
		self.Circumference = 0

	def accept(self, radi):
		self.Radius = radi

	def calculateArea(self):
		self.Area = Circle.PI * self.Radius * self.Radius

	def calculateCircumference(self):
		self.Circumference = 2 * Circle.PI * self.Radius

	def display(self):
		print("Radius of circle is : ", self.Radius)
		print("Area of circle is : ", self.Area)
		print("Circumference of circle is : ", self.Circumference)

obj1 = Circle()
obj1.accept(3)
obj1.calculateArea()
obj1.calculateCircumference()
obj1.display()


