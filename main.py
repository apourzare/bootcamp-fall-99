# a = 10 
# print(a)
# a = "Amin" 
# print(a)

# a = True
# print(a)

# a = [1, 2, 3]
# print(a)

# a = ['Amin', 'FullStack developer', 31, 'Male', False]
# print(a)

# a = ['Amin', 'FullStack developer', 31, 'Male', False, ('Python', 'Vue', 'Nuxt', 'Bootstrap')]
# print(a)

# print('************************')

# for x in a:
#   print(type(x), x)

# print('************************')

# for x in a[5]:
#   print(x)



# print(type(a))
# print(type(a[2]))
# print(type(a[5]))
# print(type(a[5][0]))

# a = ('Amin', 'FullStack developer', 31, 'Male', False, ['Python', 'Vue', 'Nuxt', 'Bootstrap'])
# print(a)
# print(type(a))
# print(type(a[5]))
# print(type(a[5][0]))

# print('************************')
# a = ('Amin')
# print(type(a))
# print(a)
# print('************************')

# print('************************')
# a = ('Amin',)
# print(type(a))
# print(a)
# print('************************')


# print('************************')
# print('************************')
# a = {
#   'Name': 'Amin',
#   'Job': 'FullStack developer',
#   'Age': 31,
#   'Skill': ['Python', 'Vue', 'Nuxt', 'Bootstrap']
# }

# for x in a['Skill']:
#   print(x)
# print(a)
# print(type(a))
# # print(type(a[5]))
# # print(type(a[5][0]))
# print(a['Name'])
# print(a['Skill'])

# print("I'm ", a[2], 'years old')

# info = {
#   'Name': 'Amin',
#   'Job': 'FullStack developer',
#   'Age': 31,
#   'Skill': ['Python', 'Vue', 'Nuxt', 'Bootstrap']
# }

# if info['Age'] > 50:
#   print('You are .......')
# else:
#   print('You are not .......')


# if info['Age'] > 0 and info['Age'] <= 10:
#   print('You are in grade A')
# elif info['Age'] > 10 and info['Age'] <= 20:
#   print('You are in grade B')
# elif info['Age'] > 20 and info['Age'] <= 30:
#   print('You are in grade C')
# elif info['Age'] > 30 and info['Age'] <= 40:
#   print('You are in grade D')
# elif info['Age'] > 40 and info['Age'] <= 50:
#   print('You are in grade E')
# else:
#   print('You are in grade F')


# if info["Age"] <= 10:
#   print('You are in grade A')
# elif info["Age"] <= 20:
#   print('You are in grade B')
# elif info["Age"] <= 30:
#   print('You are in grade C')
# elif info["Age"] <= 40:
#   print('You are in grade D')
# elif info["Age"] <= 50:
#   print('You are in grade E')
# else:
#   print('You are in grade F')

# if info["Age"] <= 50:
#   print('You are in grade E')
# elif info["Age"] <= 40:
#   print('You are in grade D')
# elif info["Age"] <= 30:
#   print('You are in grade C')
# elif info["Age"] <= 20:
#   print('You are in grade B')
# elif info["Age"] <= 10:
#   print('You are in grade A')
# else:
#   print('You are in grade F')

# if info["Age"] > 40:
#   print('You are in grade E')
# elif info["Age"] > 30:
#   print('You are in grade D')
# elif info["Age"] > 20:
#   print('You are in grade C')
# elif info["Age"] > 10:
#   print('You are in grade B')
# elif info["Age"] > 0:
#   print('You are in grade A')
# else:
#   print('You are in grade F')


##############################################

# def hello_world():
#   # print('Hello World!')
#   msg = 'Hello Amin'
#   return msg
# 
# output = hello_world()
# print(output)

# def checkEvenOrOdd(number):
#   if number % 2 == 0:
#     result = 'Is even'
#   else:
#     result = 'Is odd'
#   return result

# print(checkEvenOrOdd(15))
# print(checkEvenOrOdd(18))


# def changeItem(index):
#   list1[index] = 0

# list1 = [10, 12, 15, 17]
# changeItem(1)
# print(list1)



# def changeItemInList(list2, index, val):
#   list2[index] = val
#   return list2

# a = [-12, 6, 15, -8]
# newList = changeItemInList(a, 3, 8)
# print(newList)


# def changeList(list):
#   list = [30, 11, -2]
#   return list

# a = [-12, 6, 15, -8]
# print(a)
# a = changeList(a)
# print(a)


# def getInfo(name, gender='Male'):
#   return 'Name: %s, Gender: %s' %(name, gender)

# # print(getInfo('Amin'))
# print(getInfo('Nafise', 'Female'))

# def get_full_name(first_name, last_name):
#   return "%s %s" %(first_name, last_name)

# print(get_full_name('Amin', 'Pourzare'))

# def getFollower(*args):
#   for arg in args:
#     print(arg)

# getFollower('Ali', 'Nasrin', 'Matin', 'Vida')

# followers = []
# def getFollower(*args):
#   for arg in args:
#     followers.append(arg)
#   return followers

# followers = getFollower('Ali', 'Nasrin', 'Matin', 'Vida')

# for follower in followers:
#   print(follower)

# def get_info(skill='developer',**kwargs):
#   for key, value in kwargs.items():
#     print("%s : %s -> %s" %(key, value, skill))

# get_info('Designer', Name='Amin', Age=31, Gender='Male')


