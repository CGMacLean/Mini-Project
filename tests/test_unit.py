from source.File_functions import *
from unittest.mock import Mock


# didn't work must return different to visual display

def test_print_list():
    item_list_1 = ['customer_name', 'product_name']
    expected = (0, 'customer_name')(1, 'product_name')
    # print(expected)
    actual = print_list(item_list_1)
    # print(actual)
    assert expected == actual


test_print_list()

#     picked oder = [a,b,c]

#     a= 1
#     exected = [1,a]
#    actual = uppdate_function()
#    assert expected == actual


test_print_list()

# def add_1(a, b):
#     return a+b


# def test_add():

#     a = 1
#     b = 2
#     expected = 3
#     result = add_1(a, b)
#     assert expected == result


# test_add()

# edit value of key in dict
# def pick_order(order_list):
#     print_list(order_list)
#     order_index = int(input('pick the number of the order:'))
#     picked_order = order_list[order_index]
#     return picked_order


# def test_edit_order_status(picked_order):

#     mock_edit_status = Mock()
#     mock_edit_status.return_value = ['a', 'b']
#     expected = 5
#     print(f'"status":{picked_order["status"]}')
#     status_options = ['preparing', 'out for delivery', 'complete']
#     print_list(status_options)
#     picked_status = int(
#         input('press the number of the update you want to apply:'))
#     status_value = status_options[picked_status]
#     picked_order["status"] = status_value
#     print(f'Status has now changed to \n"status":{status_value}')
#     time.sleep(3)
#     refresh_screen()
#     return picked_order

# # test_print_list()


# def test_get_random_number():
#     # Arrange
#     mock_randint = Mock()
#     mock_randint.return_value = 5
#     expected = 5

#     # Act
#     actual = get_random_number(mock_randint)

#     # Assert
#     assert expected == actual
