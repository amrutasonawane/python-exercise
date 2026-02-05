class BookStore:
	noOfBooks = 0
	def __init__(self,bookName, authorName):
		self.name = bookName
		self.author = authorName
		BookStore.noOfBooks = BookStore.noOfBooks +	1

	def display(self):
		print(f"{self.name} by {self.author}. Noof books : {BookStore.noOfBooks}")

obj1 = BookStore("Let us C","Yashwant kanetkar")
obj1.display()

obj2 = BookStore("Let us Core java","Yashwant kanetkar")
obj2.display()

