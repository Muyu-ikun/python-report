def get_count(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count


print(get_count("hello")) # 2
print(get_count("world")) # 1
print(get_count("Python")) # 1
print(get_count("I love Python")) # 4