

def read_file(file_location):
    try:
        with open(file_location, 'r') as file:
            file_line = [line.rstrip() for line in file]
            for i, product in enumerate(file_line):
                print(f'{i}:{product}')
                # return print_lines

    except:
        print('error has occurred')
    # finally:
        # file.close()


item_list = read_file('Product_list.txt')

print(item_list)

# file = open("hello.txt", "r")
# contents = file.read()
# print(contents)
# file = open("people.txt", "r")
# lines = file.readlines()
# for line in line:
# print(line)

# def write_file(file_location):
#     try:
#         with open(file_location, 'w') as file:
#             for line in lines:
#                 file.write(item + '\n')
#                 return lines
#     except:
#         print('error has occurred')

# write_file('Product_list.txt')

# items = ['apple', 'grapes', 'orange', 'banana']
# with open('people.txt', 'w') as items_file:
#     for item in items:
#         items_file.write(item + '\n')

# def add_product():
#     file = open('Product_list.txt', 'a+')
#     products_file = []
#     product = input("type a product:")
#     file.write(f'{product}\n')
#     products_file.append(product)
#     file.close()

# add_product()

# edit version 1
# def edit_product():
#     file = open('Product_list.txt', 'r+')
#     product_list = file.read()
#     user_edit = input('what do you want to edit?')
#     user_replace = input('what do you want to replace with?')
#     product_list = product_list.replace(user_edit, user_replace)
#     file.close()

#     file = open('Product_list.txt', 'w+')
#     file.write(product_list)
#     file.close()

# edit_product()


# context managers

# version 2


# fin = open("data.txt", "r+")
# #read file contents to string
# data = fin.read()
# #replace all occurrences of the required string
# data = data.replace('pyton', 'python')
# #close the input file
# fin.close()
# #open the input file in write mode
# fin = open("data.txt", "w+")
# #overrite the input file with the resulting data
# fin.write(data)
# #close the file
# fin.close()
