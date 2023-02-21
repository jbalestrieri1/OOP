import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1': ['2/15/2023', 'The Lone Patty', 17, 569],
        'trans2': ['2/15/2023', 'The Octobreakfast', 18, 569],
        'trans3': ['2/15/2023', 'The Octoveg', 16, 570],
        'trans4': ['2/15/2023', 'The Octoburger', 20, 570],
        }

order_total = 0

customer = fc.Customer(570, 'Danni Sellyar', '97 Mitchell Way Hewitt Texas 76712',
                       'dsellyarft@gmpg.org', '254-555-9362', False)
customer1 = fc.Customer(569, 'Aubree Himsworth', '1172 Moulton Hill Waco Texas 76710',
                        'ahimsworthfs@list-manage.com', '254-555-2273', True)

transaction1 = []
transaction2 = []

for i, x in dict.items():
    date, item, cost, customerid = x
    transaction = fc.Transaction(date, item, customerid, cost, customerid)

    if customerid == 570:
        transaction1.append(transaction)
    elif customerid == 569:
        transaction2.append(transaction)

order_total1 = 0

for transaction in transaction1:
    order_total1 += transaction.get_cost()

if customer.get_member_status():
    discount1 = order_total1*.2
else:
    discount1 = 0

total1 = order_total1 - discount1

order_total2 = 0

for transaction in transaction2:
    order_total2 += transaction.get_cost()
if customer1.get_member_status():
    discount2 = order_total2*.2
else:
    discount2 = 0

total2 = order_total2 - discount2

print(f"Name: {customer.get_name()}")
print(f"Phone: {customer.get_phone()}")

for transaction in transaction1:
    print(
        f"Order Item:\t{transaction.get_item()}\tPrice:\t${transaction.get_cost():.2f}")

print(f"Total Cost: ${order_total1:.2f}")
print(f"Member Discount: ${discount1:.2f}")
print(f"Total: ${total1:.2f}")
print()

print(f"Name: {customer1.get_name()}")
print(f"Phone: {customer1.get_phone()}")

for transaction in transaction2:
    print(
        f"Order Item:\t{transaction.get_item()}\tPrice:\t${transaction.get_cost():.2f}")

print(f"Total Cost: ${order_total2:.2f}")
print(f"Member Discount: ${discount2:.2f}")
print(f"Total: ${total2:.2f}")
