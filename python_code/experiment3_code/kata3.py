def valid_braces(s):
    stack = []
    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] != '(':
                return False
            if char == ']' and stack[-1] != '[':
                return False
            if char == '}' and stack[-1] != '{':
                return False
            stack.pop()
    return not stack