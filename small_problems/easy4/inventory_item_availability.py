def transactions_for(item_id, lst):
    return [transaction for transaction in lst if transaction['id'] == item_id]


def is_item_available(item_id, lst):
    lst_transactions = transactions_for(item_id, lst)
    quantity = 0
    for transaction in lst_transactions:
        if transaction['movement'] == 'in':
            quantity += transaction['quantity']
        else:
            quantity -= transaction['quantity']
    
    return quantity > 0




transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True
