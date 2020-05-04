#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 12:34:37 2018

@author: sathisanvannadil
"""
import pprint

class Employee:
    """
    Employee Class
    """
    empCount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print("Total Employee :", Employee.empCount)
            
    def displayEmployee(self):
        print("Name :", self.name)
        print("Salary :", self.salary)
         
emp1 = Employee("Zen", 5000)
emp2 = Employee("Nina", 7800)

emp1.displayEmployee()
emp2.displayEmployee()

#emp1.displayCount()

print(Employee.empCount)
print("*"*10)

print(Employee.__doc__)             # doc string
print(Employee.__name__)            # Class name
pprint.pprint(Employee.__dict__)    # Class's namespace
print(Employee.__module__)          # Module name in which class is defined
print(Employee.__base__)            # base class

              

        
        