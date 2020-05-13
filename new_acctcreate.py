
import db
from datetime import date
import mysql.connector
from mysql.connector import errorcode
import logging
import getpass as p


def createAccount():
	user_account = db.query_db(db.check_account_data)
	#check_account_data = ("SELECT account_number FROM atm.account;")
	user_name = db.query_db(db.check_customer_username)
	#check_customer_username = ("SELECT username FROM atm.customer;")

	acc_id = []

	acc_num = int(input('Enter your account number: '))
	while acc_num in user_account:
		print('Account number already exist. Please enter a new number.')
		acc_num = int(input('Enter your account number: '))

	balance = int(input('Enter your opening balance: '))

	account_type = input('Enter account type,"SAVINGS" or "CURRENT": ').upper()

	fullname = input('Enter your fullname: ').title()

	username = input('Enter a unique login username: ')
	while username in user_name:
		print('Not available! use another name')
		username = input('Enter a unique login username again: ')

	password = p.getpass(prompt='Enter a login password:')

	gender = input('Gender! Enter either "M" or "F" only: ').upper()

	email = input('Enter a valid email address: ')

	date_of_birth = int(input('Enter dte of birth in this format YYYY-MM-DD: '))
	date_of_birth = date(date_of_birth)

    
	print(db.query_db(db.insert_account_data_query, acc_id, acc_num, balance, account_type))
	print(db.query_db(db.insert_cusomer_data_query,fullname, username, password, gender, email, date_of_birth))
	print('Welcome to WONDER BANK'.center(60))
#db.query_db("INSERT INTO atm.account (_, acc_num, balance, account_type) VALUES (account_vals)")
#db.query_db("INSERT INTO atm.customer (fullname, username, password, gender, email, date_of_birth) VALUES (customer_vals)")

createAccount()
