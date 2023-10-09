def ball_bounce(h, bounce, window):
    # 检查条件是否满足
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
        return -1
    
    # 初始下落次数为1
    count = 1
    # 计算球的下一次弹起高度
    h = h * bounce
    
    # 当球的高度大于窗户高度时，继续计算下一次弹起高度并增加次数
    while h > window:
        count += 2  # 每次下落和弹起都算一次
        h = h * bounce
    
    return count

print(ball_bounce(10, 0.6, 2)) # 5
print(ball_bounce(20, 0.5, 5)) # -1
print(ball_bounce(30, 0.8, 10)) # 7