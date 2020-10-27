# This file for learn git


# print('Hello Git')


# def get_full_name(fname, lname):
#   return "%s %s" %(fname, lname)

# get_full_name('Amin', 'Pourzare')

# def calc_age(birth_of_date):
#   return now() - birth_of_date


# class Student:
#   first_name = ''
#   last_name = ''
#   father_name = ''
#   nationality_code = ''
#   age = None
#   student_id = None
#   majore = ''
#   entry_year = None

#   def __init__(self, first_name, last_name, father_name, nationality_code, age, student_id, majore, entery_year):
#     self.first_name = first_name
#     self.last_name = last_name
#     self.father_name = father_name
#     self.nationality_code = nationality_code
#     self.age = age
#     self.student_id = student_id
#     self.majore = majore
#     self.entery_year = entery_year

#   def get_full_name(self):
#     return "%s %s" %(self.first_name, self.last_name)



# student_1 = Student('Amin', 'Pourzare', 'Hossein', '1234', 31, 99141625, 'Computer', 1399)
# print(student_1.age)
# student_2 = Student('Ali', 'Mohammadi', 'Hassan', '3256', 20, 99141626, 'Computer', 1399)
# print(student_2.age)

# print(student_1.get_full_name())
# print(student_2.get_full_name())






class Student:

  def __init__(self, fname, lname, faname, n_code, age, sid, majore, e_year):
    self.__fname = fname
    self.__lname = lname
    self.__faname = faname
    self.__n_code = n_code
    self.__age = age
    self.__sid = sid
    self.__majore = majore
    self.__e_year = e_year

  def get_fname(self):
    return self.__fname

  def get_lname(self):
    return self.__lname

  def get_faname(self):
    return self.__faname
  
  def get_n_code(self):
    return self.__n_code

  def get_age(self):
    return self.__age

  def set_age(self, age):
    self.__age = age

  def del_age(self):
    self.__age = None
    # del self.__age

  def get_sid(self):
    return self.__sid

  def get_majore(self):
    return self.__majore

  def get_e_year(self):
    return self.__e_year



s1 = Student('Amin', 'Pourzare', 'Hossein', '1234', 31, 99141625, 'Computer', 1399)


# print(s1.get_full_name())
# print(s1.get_age())

# print(s1.get_fname())
# print(s1.get_age())
# s1.set_age(32)
print(s1.get_age())
s1.del_age()
print(s1.get_age())
s1.set_age(32)
print(s1.get_age())
# del s1
# print(s1.get_name())