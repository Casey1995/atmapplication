import db
import dashBoard as dbod
import login


def cashDep(username,password):
	account_number, balance, __ = db.query_db(db.display_customer_data_query,username,password)[0]
	amt = int(input('Enter amount to deposit: '))
	final_amt = int(balance) + amt
	db.query_db(db.transfer_to_query,amt,account_number)
	print('Deposit of',amt,'Successful! Available balance is:',final_amt)
	return True
	#("UPDATE atm.account SET balance = balance + %s WHERE account_number = %s")
	#db.query_db(db.insert_account_data_query,'2', '2000', '4500000', 'Savings')

def cashWdr(username,password):
	account_number, balance, __ = db.query_db(db.display_customer_data_query,username,password)[0]
	amt = int(input('Enter amount to withdraw: '))
	if amt <= int(balance):
		final_amt = int(balance) - amt
		db.query_db(db.transfer_from_query,amt,account_number)
		print('Withdrawal successful! available balance is:',final_amt)
		return True
	else:
		print('Insufficient account balance.')
		return False

def acctTrans(username,password):
	account_number, balance, __ = db.query_db(db.display_customer_data_query,username,password)[0]
	ben_name = input('Enter beneficiary name: ')
	ben_acct = int(input('Enter beneficiary account number: '))
	accounts = db.query_db(db.check_account_data)
	for account in accounts:
		account = list(account)
		#print(account)
		if ben_acct in account:
			#account_number, balance, ben_name, email = db.query_db(db.account_info_query,ben_acct)[0]
			#print(ok)
			Print('You are transfering to',ben_name)
			trf_amt = int(input('Enter transfer amount: '))
			if trf_amt <= int(balance):
				final_amt = int(balance) - trf_amt
				db.query_db(db.transfer_from_query,trf_amt,account_number)
				db.query_db(db.transfer_to_query,trf_amt,ben_acct)
				print('You have successfully transfered',trf_amt,'to',ben_name)
				return True
			else:
				print('Insufficient account balance.')
				return False
	else:
		print('The account number entered does not exist! verify and try again')

#acctTrans('okey','okey')	
	#account_info_query = ("SELECT account_number, balance, fullname, email FROM atm.account join atm.customer on (atm.account.customer_id = atm.customer.id) where account_number = %s")
	#Send a mail notifying the recipient of the successful transfer
