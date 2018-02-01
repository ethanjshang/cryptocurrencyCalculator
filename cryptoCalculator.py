"""
TODO:
Add Litecoin and bitcoin
"""
import sys
"Calculator of Stock and Cryptocurrency"
print()
current_price_eth = float(input("Current price of ethereum: "))
current_price_bitcoin = float(input("Current price of bitcoin: "))
infile = open(sys.argv[1],"r")

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
class Ethereum(cryptocurrency):
	type = 'eth'
	price = current_price_eth
class Bitcoin(cryptocurrency):
	type = 'btc'
	price = current_price_bitcoin
types_of_crypto = {
	'eth' : Ethereum,
	'btc' : Bitcoin
}


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
total_spent_after_fees = 0

print()

for purchase in purchases:
	total_spent += purchase.amount_spent
	total_spent_after_fees += purchase.amount_after_fees
	purchase.weighted_gain = purchase.price / purchase.price_at_purchase  * purchase.amount_after_fees
	purchase.value_gain = purchase.weighted_gain - purchase.amount_after_fees
	total_value_gain += purchase.value_gain
	print("Change in investment value due to $" + str(purchase.amount_spent), "of", purchase.type, "bought at", purchase.price_at_purchase, ":", round(purchase.value_gain,2))
market_value = total_value_gain + total_spent_after_fees
sell_price = round(market_value - (market_value * 0.0149),2)
overall_change = round(market_value - (market_value * 0.0149)-total_spent,2)
print()
print("Total Spent Before Fees:", total_spent)
print(" Total Spent After Fees:", total_spent_after_fees)
print("     Total Value Change:", round(total_value_gain,2))
print("           Market Value:", round(market_value,2),"\n")

print("Total Absolute Change in investment value (after fees):", round(market_value-total_spent,2))
print("Total Relative Change in investment value (after fees):", round(market_value/total_spent,4))

print("\nAmount Gained if Sold (including sell fee):", sell_price)
print("                            Overall Change:", overall_change)
