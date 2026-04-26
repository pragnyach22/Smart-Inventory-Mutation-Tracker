import copy

def create_inventory():
    inventory=[
        {
            "item": "Laptop",
            "details":{
                "price":50000,
                "stock":10,
                "supplier":{ "name":"Dell", "rating":4.5}
            }
        },
        {
            "item": "Phone",
            "details":{
                "price":20000,
                "stock":25,
                "supplier":{ "name":"Samsung", "rating":4.2}
            }
        }
    ]
    return inventory

def apply_discount(data,roll_number):
    length=len(data)
    index_to_modify=roll_number%length

    for i in range(len(data)):
        old_price=data[i]["details"]["price"]
        data[i]["details"]["price"]=int(old_price*0.9)

        if i==index_to_modify:
            data[i]["details"]["stock"]+=5

def compare_data(original,modified):
    changed=0
    unchanged=0

    print("\n Differences Observed")
    for i in range(len(original)):
        if original[i]!=modified[i]:
            changed+=1
            print(f"Item changes: {original[i]['item']}")
        else:
            unchanged+=1

    return changed, unchanged

def main():
    roll_number=642
    original_inventory=create_inventory()
    shallow_copy=copy.copy(original_inventory)
    deep_copy=copy.deepcopy(original_inventory)
    apply_discount(shallow_copy,roll_number)
    apply_discount(deep_copy,roll_number)
    print("Original Inventory:")
    for item in original_inventory:
        print(item)

    print("\nShallow Copy Inventory:")
    for item in shallow_copy:
        print(item)

    print("\nDeep Copy Inventory:")
    for item in deep_copy:
        print(item)

    print("\nComparing Original and Shallow Copy:")
    shallow_result=compare_data(original_inventory,shallow_copy)

    print("\nComparing Original and Deep Copy:")
    deep_result=compare_data(original_inventory,deep_copy)

    print("\nSummary Tuple (shallow copy):",shallow_result)
    print("Summary Tuple (deep copy):",deep_result)

    print("\nExplanation")
    print("shallow copy shares inner dictionaries with original.")
    print("so when nested values(price,stock) are modified, original also changes")
    print("deep copy creates completly independent data.")
    print("so modifications in deep copy do not affect original")
