# class Student:
#     def __init__(s):
#         s.name=input("Enter the Name")
#         s.usn=input("Enter the usn")
#         s.s1=int(input("enter the subject1 marks"))
#         s.s2=int(input("enter the subject2 marks"))
#         s.s3=int(input("enter the subject3 marks"))
#         s.s4=int(input("enter the subject4 marks"))
#         s.s5=int(input("enter the subject5 marks"))
#     def get(s):
#         print("Name: ",s.name)
#         print("USN: ",s.usn)
#         s.per=float((s.s1+s.s2+s.s3+s.s4+s.s5)/5)
#         print("Percentage: ",round(s.per,2))
#         if s.per<=100 and s.per>=90:
#             print("Grade is: O")
#         elif s.per<=90 and s.per>=80:
#             print("Grade is: A")
#         elif s.per<80 and s.per>=60:
#             print("Grade is B")
#         elif s.per<60 and s.per>=45:
#             print("Grade is: C")
#         elif s.per<45:
#             print("Grade is: F")
#         else:
#             print("marks is outof range")


# o=Student()
# o.get()

# class student:
#     def __init__(s,n,u):
#         s.name=n
#         s.usn=u
#         s.s1=int(input("enter the subject1 marks"))
#         s.s2=int(input("enter the subject2 marks"))
#         s.s3=int(input("enter the subject3 marks"))
#         s.s4=int(input("enter the subject4 marks"))
#         s.s5=int(input("enter the subject5 marks"))
# o=student(input("Enter the Name"),input("Enter USN"))
# print("Name: ",o.name)
# print("USN: ",o.usn)
# per=float((o.s1+o.s2+o.s3+o.s4+o.s5)/5)
# print("Percentage: ",round(per,2))
# if per<=100 and per>=90:
#     print("Grade is: O")
# elif per<=90 and per>=80:
#     print("Grade is: A")
# elif per<80 and per>=60:
#     print("Grade is B")
# elif per<60 and per>=45:
#     print("Grade is: C")
# elif per<45:
#     print("Grade is: F")
# else:
#     print("marks is outof range")

# class Student:
#     def __init__(self):
#         self.usn=None
#         self.Name=None
#         self.marks=None
#         self.percentage=None
#         self.Grade=None

#     def copy(self):
#         self.name=input("Enter the name: ")
#         self.usn=input("Enter the usn: ")
#         for i in range(0,5):
#             self.marks=int(input(f"Enter the subject {i+1}"))
#     def print_Details(self):
#         print("Name: ",self.name)
#         print("USN: ",self.usn)
#         for inti in range(0,5):
#             print(f"subject {i+1} : {self.marks}")
#         print("Percentage: ",self.percentage)
#     def cal_percentage(self):
#         sum=0
#         for i in self.marks:
#             sum+=i
#             self.percentage=(sum%500)*100

# ob=Student()
# ob.copy()
# ob.print_Details()

class Std:
    def __init__(self): 
        self.__USN = None
        self.__Name = None
        self.__Marks = []
        self.__Percentage = None
        self.__Grade = None

    def Std_Input(self):
        self.__Name = input("Enter your Name: ")
        self.__USN = input("Enter Your USN: ")
        for i in range (0,5):
            marks = input(f"Enter Your Marks in Sub{i+1} : ")
            self.__Marks.append(marks)

    def calc_percentage (self):
        sum = 0
        for i in self.__Marks:
            sum = sum + int(i)
        self.__Percentage = (sum/500)*100

    def calc_Grade(self):
        per = float(self.__Percentage)
        if per<=100 and per >=80:
            self.__Grade = "A"
        elif per<80 and per >=60:
            self.__Grade = "B"
        elif per<60 and per >=40:
            self.__Grade = "C"
        elif per<40 and per >=0:
            self.__Grade = "D"
        else: 
            self.__Grade = "Inavlid"

    def print_details(self):
        print("Name: ",self.__Name)
        print("USN : ",self.__USN)
        print("Marks in Five Subject are :")
        for i in range(0,5):
            print(f"Subject {i+1} = {self.__Marks[i]}")
        print("Percentage : ", self.__Percentage)
        print("Grade : ", self.__Grade)

    def convert_list(self):
        st_list = [self.__USN,self.__Name,self.__Marks,self.__Percentage,self.__Grade]
        return st_list

    # def covert_ob(self,stu_list):
    #     self.__USN = stu_list[0]
    #     self.__Name = stu_list[1]
    #     self.__Marks = stu_list[2]
    #     self.__Percentage = stu_list[3]
    #     self.__Grade = stu_list[4]



st1 = Std()

print(type(st1))

st1.Std_Input()

st1.calc_percentage()
st1.calc_Grade()

st1.print_details()

with open("student.txt",'wb') as File:
    L=st1.convert_list()
    data = f"{L[0]}|{L[1]}|{L[2][0]},{L[2][1]},{L[2][2]},{L[2][3]},{L[2][4]}|{L[3]}|{L[4]}\n"
    File.write(data.encode())
    File.close()

with open("student.txt",'a') as File:
    L=st1.convert_list()
    data = f"{L[0]}|{L[1]}|{L[2][0]},{L[2][1]},{L[2][2]},{L[2][3]},{L[2][4]}|{L[3]}|{L[4]}\n"
    File.append(data.encode())
    File.close()

