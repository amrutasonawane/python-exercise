#9. What will happen if indentation is not maintained properly? Explain with a small code snippet.
#Logical errors
for i in range(3):
    print("Adding...")
    print("Finished") # Indented incorrectly!
    
for i in range(3):
    print("Adding...")
print("Finished") # Indented correctly!

#IndentationError
#def sayhello():
#print("Hello!") # This is giving IndentationError

def sayhello():
	print("Hello!")
    



