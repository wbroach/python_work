def print_models(unprinted_designs, printed_designs):
    while unprinted_designs:
        current_print = unprinted_designs.pop()
        print("Now printing: " + current_print.title())
        printed_designs.append(current_print)
        
def show_complete(completed_designs):
    for completed_design in completed_designs:
        print(completed_design)
        
unprinted_models = ['iphone case', 'robot pendant', 'dodecahedron']
printed_models = []

print_models(unprinted_models, printed_models)

show_complete(printed_models)
