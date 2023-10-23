def fillable(stock, merch, n):
    if merch in stock:
        stock_quantity = stock[merch]
        return stock_quantity >= n
    else:
        return False

# 示例数据
inventory = {
    'apple': 10,
    'banana': 5,
    'orange': 3
}

product = 'apple'
quantity = 3

result = fillable(inventory, product, quantity)
print(result)  
