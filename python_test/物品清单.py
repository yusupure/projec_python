stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def stufftest(stuffnum):
    total=0
    for i,k in stuffnum.items():
        print(str(k)+' '+i)
        total+=k
    print (str(total))

#tufftest(stuff)

def addToInventory(inventory, addedItems):
    for i in range(len(addedItems)):
        if addedItems[i] not in inventory:
            inventory.setdefault(addedItems[i],1)
        else:
            inventory[addedItems[i]]+=1
    return inventory
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
stufftest(inv)