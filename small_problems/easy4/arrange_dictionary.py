def order_by_value(dct):
    def get_value(key):
        return dct[key]
    
    return sorted(dct, key=get_value)

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True