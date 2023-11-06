class Block:
    def __init__(self, dimensions):
        self.width, self.length, self.height = dimensions

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.width * self.length * self.height

    def get_surface_area(self):
        return 2 * (self.width * self.length + self.length * self.height + self.height * self.width)

# 示例用法
b = Block([2, 4, 6])
print(b.get_width())  # 输出 2
print(b.get_length())  # 输出 4
print(b.get_height())  # 输出 6
print(b.get_volume())  # 输出 48
print(b.get_surface_area())  # 输出 88
