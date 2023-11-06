class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
    
    def is_worth_it(self):
        # 计算除去船员重量后的吃水深度
        effective_draft = self.draft - (self.crew * 1.5)
        
        # 判断船是否值得掠夺
        return effective_draft > 20

# 示例用法
Titanic = Ship(15, 10)
print(Titanic.is_worth_it())  # 输出 False
