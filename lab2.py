products = ["t-shirt", "mug", "hat", "book", "keychain"]
inventory = {}
customer_orders = set()

for product in products:
    x = int(input(f"Input the quantity of {product}'s available: "))
    inventory[product]= x
for y in range(3):
    while True:
        prdname = input(f"Enter product name #{y+1} from the list {products}")
        if prdname in products:
            if prdname in customer_orders:
                print("already ordered")
            else:
                customer_orders.add(prdname)
                break
        else:
            print("not in products")
print(customer_orders)

TPO = len(customer_orders)
PPO = (TPO/len(products))*100
order_status = (PPO,TPO)
print(f"Total Products Ordered: {order_status[1]}")
print(f"Percentage of Products Ordered: {order_status[0]}%")

for orderedprd in customer_orders:
    inventory[orderedprd] = inventory[orderedprd] - 1
for product, x in inventory.items():
    print(f"{product} : {x}")