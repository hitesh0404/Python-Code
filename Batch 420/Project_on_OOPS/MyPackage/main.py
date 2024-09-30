from Student import *
import math as m




def main():
    print('we are executing this main.py file')
    harsh = Student()    #constructor
    rohan = Student()
    harsh.name = 'Harsh'
    harsh.age = 20
    harsh.game = 'BGMI'
    harsh.play()
    rohan.name = 'Rohan'
    rohan.age = 21
    rohan.game = 'FreeFire'
    rohan.play()
    student001_name= 'Harsh'
    student002_name = 'Rohan'
    student001__age = 12
    student002_age = 14
    # study()
    # play('COD')
    # sleep()
    # print('we are done')
    # practice()
    print(m.pow(2,3),m.sqrt(625),m.pi)

if __name__ =='__main__':
    main()