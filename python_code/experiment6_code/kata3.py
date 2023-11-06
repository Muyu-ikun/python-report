def shorten_number(suffixes, base):
    def shorten(value):
        try:
            value = int(value)
            if value < base:
                return str(value) + suffixes[0]
            for i in range(len(suffixes) - 1):
                suffix = suffixes[i + 1]
                divisor = base ** (i + 1)
                if value < base * base:
                    return str(int(value // base)) + suffix
                value //= base
            return f"{value:.0f}" + suffixes[-1]  # 处理最后一个单位
        except (ValueError, TypeError):
            return str(value)
    return shorten

# 示例用法
filter1 = shorten_number(['', 'k', 'm'], 1000)
print(filter1('23424234223'))  # 输出 '23424m'
print(filter1('98234324'))  # 输出 '98m'
print(filter1([1, 2, 3]))  # 输出 '[1,2,3]'

filter2 = shorten_number(['B', 'KB', 'MB', 'GB'], 1024)
print(filter2('32'))  # 输出 '32B'
print(filter2('2100'))  # 输出 '2KB'
print(filter2('pippi'))  # 输出 'pippi'
