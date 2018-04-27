def displayInventory(inventory):
    inventory_items = inventory.items()
    count = 0
    for key, num in inventory_items:
        count += num
        print(key + ': ' + str(num))
    print('Totol: ' + str(count))
def addInventory(inventory, items):
    count = len(items)
    for i in range(count):
        name = items[i]
        oldNum = inventory.get(name, 0)
        inventory[name] = oldNum + 1
    print('Add: ' + str(count))    

inventory = {
    'rope': 12,
    'coin': 200,
    'dagger': 4,
    'arrow': 3
}
displayInventory(inventory)
print('----------')
addInventory(inventory, ['coin', 'coin', 'boots', 'arrow', 'coin', 'rope'])
print('----------')
displayInventory(inventory)