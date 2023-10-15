def disemvowel(s):
    vowels = "aeiouAEIOU"
    result = ""

    for char in s:
       
        if char not in vowels:
            result += char

    return result


# 测试示例
input_string = "This website is for losers LOL!"
output_string = disemvowel(input_string)
print(output_string)