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
    self.fname = fname
    self.lname = lname
    self.faname = faname
    self.n_code = n_code
    self.age = age
    self.sid = sid
    self.majore = majore
    self.e_year = e_year
  
  def get_full_name(self):
    return "%s %s" %(self.fname, self.lname)

  def get_age(self):
    return self.age


s1 = Student('Amin', 'Pourzare', 'Hossein', '1234', 31, 99141625, 'Computer', 1399)


print(s1.get_full_name())
print(s1.get_age())