#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-
# author: wangyadong
'''
name = input("name: ")
age = int(input("age: "))
job = input("job: ")
salary = input("salary: ")

info = """
---------info of %s---------
Name: %s
Age: %d
job: %s
Salary: %s
""" % (name, name, age, job, salary)
print(info)
'''

name = input("name: ")
age = int(input("age: "))
job = input("job: ")
salary = input("salary: ")

info2 = """
----- info of {_name} -----
Name: {_name}
Age: {_age}
Job: {_job}
Salary: {_salary}
""" .format(_name=name,
            _age=age,
            _job=job,
            _salary=salary)

print(info2)

info3 = '''
----- info3 of {0} -----
Name: {1}
Age: {2}
Job: {3}
Salary: {4}
'''.format(name, name, age, job, salary)

print(info3)