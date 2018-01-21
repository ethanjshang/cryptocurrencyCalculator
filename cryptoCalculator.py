"Calculator of Stock and Cryptocurrency"
print()
current_price_eth = float(input("Current price of ethereum: "))

class cryptocurrency:
	def __init__(self,amount_spent, price_at_purchase):
		self.amount_spent = amount_spent
		self.amount_after_fees = amount_spent - 2.99
		self.price_at_purchase = price_at_purchase
		self.weighted_gain = 0
		self.value_gain = 0
"""
class stock:
	def __init__(self, amount_spent, price_at_purchase,fees):
		self.amount_spent = amount_spent
		self amount_after_fees = amount_spent - 4.99

class sptl(stock):
	type = 'ETF'
class sphd(stock):
	type = 'ETF'
"""
class eth(cryptocurrency):
	type = 'Ethereum'
class btc(cryptocurrency):
	type = 'Bitcoin'

purchases = [eth(150.35,1229.10),eth(150.00, 1145.41),eth(150.00,1049.44)]

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
