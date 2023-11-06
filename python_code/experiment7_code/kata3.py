class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return (len(self.collection) + self.items_per_page - 1) // self.items_per_page

    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1
        elif page_index == self.page_count() - 1: 
            
            # 如果是6%4，那么最后一页就是2
            # 如果是8%4，那么最后一页就是0，说明最后一页是满的，应该返回4
            last_page = self.item_count() % self.items_per_page
            
            return self.items_per_page if last_page == 0 else last_page
        
        # 其他页
        else:
            return self.items_per_page
    def page_index(self, item_index):
        if item_index < 0 or item_index >= len(self.collection):
            return -1
        return item_index // self.items_per_page

# 示例用法
helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
print(helper.page_count())  # 输出 2
print(helper.item_count())  # 输出 6
print(helper.page_item_count(0))  # 输出 4
print(helper.page_item_count(1))  # 输出 2
print(helper.page_item_count(2))  # 输出 -1
print(helper.page_index(5))  # 输出 1
print(helper.page_index(2))  # 输出 0
print(helper.page_index(20))  # 输出 -1
print(helper.page_index(-10))  # 输出 -1
