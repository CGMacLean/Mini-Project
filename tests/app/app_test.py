my_list = ['a', 'b', 'c', 'd']
my_string = ','.join(my_list)
print(my_string)
print(my_list)


def Add_to_basket():
    item_list = []
    while True:
        # DB_print(product_fieldnames)
        basket = input('Pick a products by ID or, or enter 0 only to exit:')
        item_list.append(basket)
        if basket == '0':
            print('back to menu')
            return
        elif basket == '':
            if len(item_list) == 0:
                print('No items in basket')
            else:
                # remove last enter input forcing a comma
                del item_list[-1]
                # join basket items to Items for DB
                Items = ','.join(item_list)
                print(Items)
                return Items
        else:
            print(item_list)
            print('Add another? or press enter to continue')
    
            
items = Add_to_basket()
print(items)