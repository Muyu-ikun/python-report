import math

class Vector:
    def __init__(self, components):
        self.components = components

    def __str__(self):
        return f"({','.join(map(str, self.components))})"

    def equals(self, other):
        return self.components == other.components

    def add(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vector dimensions must match for addition")
        result = [x + y for x, y in zip(self.components, other.components)]
        return Vector(result)

    def subtract(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vector dimensions must match for subtraction")
        result = [x - y for x, y in zip(self.components, other.components)]
        return Vector(result)

    def dot(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vector dimensions must match for dot product")
        result = sum(x * y for x, y in zip(self.components, other.components))
        return result

    def norm(self):
        return math.sqrt(sum(x ** 2 for x in self.components))

# 示例用法
a = Vector([1, 2, 3])
b = Vector([3, 4, 5])
c = Vector([5, 6, 7, 8])

print(a.add(b))  # 输出 Vector([4, 6, 8])
print(a.subtract(b))  # 输出 Vector([-2, -2, -2])
print(a.dot(b))  # 输出 26
print(a.norm())  # 输出 sqrt(14)
a.add(c)  # 抛出异常
