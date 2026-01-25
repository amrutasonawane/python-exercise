#Write a lambda function using filter which accepts a list of strings and returns a list of strings having length greater than 5.
data = ["Pune","Mumbai","Sambhajinagar","Dharashiv","Nashik","Ahilyanagar"]
print("originaldata is : ",data)
filterData = list(filter((lambda city : len(city)>5),data))
print("List if city having length greater than 5 is : ",filterData)