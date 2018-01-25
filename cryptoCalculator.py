"""
TODO:
Clarify distinction between amount_spent and amount_after fees
Add test cases to make sure this program is working correctly
"""
"Calculator of Stock and Cryptocurrency"

import sys
class cryptocurrency:
	def __init__(self,amount_spent, price_at_purchase):
		self.amount_spent = amount_spent
		if (amount_spent <= 200):	
			self.amount_after_fees = amount_spent - 2.99
		else:
			self.amount_after_fees = amount_spent - (amount_spent * 0.0149)
		self.price_at_purchase = price_at_purchase
		self.weighted_gain = 0
		self.value_gain = 0
"""
class Stock:
	def __init__(self, amount_spent, price_at_purchase,fees):
		self.amount_spent = amount_spent
		self.amount_after_fees = amount_spent - 4.99
	def update_amount(self,new_amount):
		self.amount_spent = new_amount
class ETF(Stock):
	type = ''

"""
class Ethereum(Cryptocurrency):
	type = 'eth'
class Bitcoin(Cryptocurrency):
	type = 'btc'
types_of_crypto = {
	'eth' : Ethereum,
	'btc' : Bitcoin
}

print()
current_price_eth = float(input("Current price of ethereum: "))
infile = open(sys.argv[1],"r")
#Reading in info from the file
line_info = []
for line in infile:
	line_info.append(line[:-1].split(" "))
	print(line_info)

#Storing info into classes
purchases = []

for line in line_info:
	type_of_crypto = line[0]
	amount_spent = float(line[1])
	price_at_purchase = float(line[2])
	purchases.append(types_of_crypto[type_of_crypto](amount_spent, price_at_purchase))
num_purchases = len(purchases)
total_value_gain = 0
total_spent = 0

print()

for purchase in purchases:
	total_spent += purchase.amount_spent
	purchase.weighted_gain = current_price_eth / purchase.price_at_purchase  * purchase.amount_after_fees
	purchase.value_gain = purchase.weighted_gain - purchase.amount_after_fees
	total_value_gain += purchase.value_gain
	print("Change in investment value due to $" + str(purchase.amount_spent), "of", purchase.type, "bought at", purchase.price_at_purchase, ":", round(purchase.value_gain,2))
print("\nCost Basis  :", total_spent)
print("Market Value:", round(total_value_gain + total_spent,2))
print("Total Absolute Change in investment value (including fees):", round(total_value_gain,2))
print("Total Relative Change in investment value (including fees):", round((total_value_gain+total_spent)/total_spent,4))

