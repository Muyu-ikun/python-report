def count_developers(lst):
    count = 0  # 用于记录来自欧洲的JavaScript开发者数量

    for developer in lst:
        if developer['continent'] == 'Europe' and developer['language'] == 'JavaScript':
            count += 1

    return count

# 示例数据
lst1 = [
  { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
  { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
  { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
  { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
]

result = count_developers(lst1)
print(result)  # 输出 1
