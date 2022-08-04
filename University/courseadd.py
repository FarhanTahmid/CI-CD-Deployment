

from pydoc import describe
from unicodedata import name
from django.forms import SelectDateWidget

from django.db import connections
class CourseAdd:
    def __init__(self,id='',name='',description=''):
        self.id=id
        self.name=name
        self.description=description
    def addCourse(self):
        #print(f"Course Name: {self.name}, Course ID: {self.id}, Description: {self.description}")
        
        #database connection to the app
        db_cursor=connections['default'].cursor()
        
        #Sql Query for course add
        db_cursor.execute("INSERT INTO University_offeredcourse (id,name,description) VALUES('"+self.id+"','"+self.name+"','"+self.description+"')")
    
    def deleteCourse(self):
        #database connection to the app
        db_cursor=connections['default'].cursor()
        
        #Sql Query for course add
        db_cursor.execute("DELETE FROM University_offeredcourse WHERE id='"+self.id+"'")
        
        
    

