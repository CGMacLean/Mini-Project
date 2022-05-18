import csv

Product_dict = [{'Product': 'COKE', 'Price': '1.2'},
                {'Product': 'PEPSI', 'Price': '1.2'}]
fields = ['Product', 'Price']
filename = "product_list.csv"
with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(Product_dict)


with open(filename, 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
