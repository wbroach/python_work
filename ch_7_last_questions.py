sandwich_orders = ['pastrami', 'tuna', 'turkey', 'pastrami', 'ham', 'pastrami', 'veggie']
finished_sandwiches = []

print("The deli is out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop()
    print("I made your " + current_order.title() + " sandwich.")
    finished_sandwiches.append(current_order)
    

print("\nHere are all the sandwiches that were made today:")
for sandwich in finished_sandwiches:
    print("\t" + sandwich.title())
