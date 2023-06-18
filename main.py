Items = {
    'potato': [20, 3],
    'plushie': [34,15],
    'Pencil pack': [2,20],
    'Lemonade Bottles': [60,2.75]
}
def add():
    Item = input("Please item")
    Quantity = int(input("Please Quantity"))
    Price = int(input("Please price"))
    Items[Item] = [Quantity,Price]
def StockerRemover():
    for i in Items:
        nums = Items[i]
        nums[0] = 0
        print(nums)
        Items[i] = nums
def GoodsChanging():
    Goodie = input("Please your item")
    if Goodie  in Items:
        Quantity = int(input("Please Quantity"))
        Price = int(input("Please price"))
        Items[Goodie] = [Quantity,Price]
    else:
        print("Item hasnt been found")
def ItemsShower():
    for i in Items:
        QandP = Items[i]
        print("Item: ",i)
        print(" -->  Quantity: ",QandP[0])
        print(" -->  Price: ",QandP[1])
def ItemsInStock():
        for i in Items:
            QandP = Items[i]
            if QandP[0] != 0:
                print("Item: ",i)
def HighestPrice():
    max_price = 0
    max_price_product = ''

    for product, details in Items.items():
        price = details[1]
        if price > max_price:
            max_price = price
            max_price_product = product

    print(max_price)
    print(max_price_product)
def StockChanger():
    Product = input("Please product")
    if Product in Items:
        nums = Items[Product]
        Stock = input("Please new stock")
        nums[0] == Stock
        Items[Product] = nums
while True:
    print("Add to add a item")
    print("Stock to change stock")
    print("StockRemove to remove all stocks")
    print("GoodsChange to change quantity and price of a item")
    print("HighPrice to see the highest priced item")
    print("ItemStocked to see the items that are in stock")
    print("ShowItems to see all items with theyre price and quantity")
    print("Stop to stop the program")
    command = input("Please command")
    if command == "Add":
        add()
    elif command == "Stock":
        StockChanger()
    elif command == "StockRemove":
        StockerRemover()
    elif command == "GoodsChange":
        GoodsChanging()
    elif command == "HighPrice":
        HighestPrice()
    elif command == "ItemStocked":
        ItemsInStock()
    elif command == "ShowItems":
        ItemsShower()
    elif command == "Stop":
        break
    else:
        print("Command not found")
    
