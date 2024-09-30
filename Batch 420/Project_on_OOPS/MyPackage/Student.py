class Student:
    college='Mumbai'
    def __init__(self, name, age, grade,game):
        self.name = name
        self.age = age
        self.grade = grade
        self.game= game
    def study(name='python'):
        print(f"let's study {name}")

    def play(self):
        print(f"let's play {self.game}")

    def sleep(time='8 Hour'):
        print(f"sleep for {time}")

    def practice(duration='15 Min'):
        print(f"practice for {duration}")



if __name__=='__main__':
    student1 = Student('John', 20, 'A', 'basketball')
    student1.study('math')
    student1.play()
    student1.sleep()
    student1.practice()
    