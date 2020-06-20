import sys
import os
import datetime

contact_list1 = [] # create empty list





name = input('enter the first and last name of your contact: ')
contact_list1.insert(0, name)
phone_number = int(input('enter the phone number for you contact: '))
contact_list1.insert(1, phone_number)
email = input('enter the email address for your contact: ')
contact_list1.insert(2, email)
address = input('enter the address of your contact: ')
contact_list1.insert(3, address)
website = input('enter the wesbite if your contact has one: ')
contact_list1.insert(4, website)

print(contact_list1)