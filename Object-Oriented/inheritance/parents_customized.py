''' 
Inheritance allowed us to inheritace a attribute and method in the parent class 
'''

# clas variables
class Parent:

	increse_pay = 0.07

	def __init__(self, first_name, last_name, age, salary):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.salary = salary


	def parent_detail(self):
		return '{}, {}, {}, {}'.format(self.name, self.last_name, self.age)

	def fullname(self, first_name, last_name):
		return '{} {}'.format(self.first_name, self.last_name)

	def email_address(self):
		return '{}.{}'.format(self.first_name, self.last_name) + '@' + 'gmail.com'

	def pay_raise(self):
		self.salary = int(self.salary * self.increse_pay + self.salary)


obj = Parent('Tim', 'Alan', '44', 39000)
print(obj.first_name + ' ' + obj.last_name + ' ' + obj.age)
print(obj.email_address())
print(obj.salary)
obj.pay_raise()
print(obj.salary)

print('#################################################')

class Son(Parent):
	increse_pay = 0.15

class Daughter(Parent):
	increse_pay = 0.25


daughter_1 = Daughter('Adam', 'Sophia', '25', 25000)
daughter_2 = Daughter('Adam', 'Claudia', '31', 21100)
son_1 = Son('David', 'Tom', '33', 27000)
son_2 = Son('David', 'Jeff', '29', 24500)


print(daughter_1.first_name + ' ' + daughter_1.last_name + ' ' + daughter_1.age)
print(daughter_1.email_address())
print(daughter_1.salary)
daughter_1.pay_raise()
print(daughter_1.salary)

print('#################################################')

print(daughter_2.first_name + ' ' + daughter_2.last_name + ' ' + daughter_2.age)
print(daughter_2.email_address())
print(daughter_2.salary)
daughter_2.pay_raise()
print(daughter_2.salary)

print('=============================================================')

print(son_1.first_name + ' ' + son_1.last_name + ' ' + son_1.age)
print(son_1.email_address())
print(son_1.salary)
son_1.pay_raise()
print(son_1.salary)

print('#################################################')

print(son_2.first_name + ' ' + son_2.last_name + ' ' + son_2.age)
print(son_2.email_address())
print(son_2.salary)
son_2.pay_raise()
print(son_2.salary)