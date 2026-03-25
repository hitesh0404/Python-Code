class College:
    def __init__(self,name,location):
        self.name = name
        self.location = location
        self.students=[]

    def add_student(self,student:object)->bool:
        if student not in self.students:
            self.students.append(student)
            return True
        else:
            return False
    def find_student(self,student:object)->bool:
        if student in self.students:    
            return True
        else:
            False
    def show_students(self):
        print('[ ',end='' )
        for i in self.students:
            print(i,end=' ')
        print(' ]',end='' )
        print()
    def __str__(self):
        return self.name +" " +self.location