import re
# a simple function that finds patterns in txt documents
def grades():
    with open ("grades.txt", "r") as file:
        grades = file.read()
        g = re.findall('([\w ]+)(?=\: B)',grades)
        return grades
    
grades()  
    
