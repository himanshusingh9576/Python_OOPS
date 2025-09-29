"""
marks = [87, 64, 33, 95, 76]
print(marks[3])
marks[3] = 0
print(marks[3])
print(marks)
print(marks[1:3])
"""
## List Method
"""
list = [1, 7, 2, 3]
print(list.append(4))

list.sort()   
print(list)
list.reverse()
print(list)
list.insert(0, 9)
print(list) """
# WAP to ask the user to enter names of their 3 favorite movie and store them in a list
movie1 = input("Enter Your first movie: - ")
movie2 = input("Enter Your second movie:- ")
movie3 = input("Enter Your third movie:- ")
list = []
list.append(movie1)
list.append(movie2)
list.append(movie3)
print(list)