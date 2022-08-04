

from pydoc import describe
from unicodedata import name
from django.forms import SelectDateWidget

from django.db import connections
class StudentAdd:
    def __init__(self,id='',fullname='',email=''):
        self.id=id
        self.fullname=fullname
        self.email=email
    
    def addStudent(self):
        
        #database connection to the app
        db_cursor=connections['default'].cursor()
        
        #Sql Query for student add
        db_cursor.execute("INSERT INTO University_studentlist (id,fullname,email) VALUES('"+self.id+"','"+self.fullname+"','"+self.email+"')")
        
    

