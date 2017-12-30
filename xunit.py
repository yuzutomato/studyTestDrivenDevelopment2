class WasRun:
    def __init__(self, name):
        self.wasRun = None
        self.name = name
    def run(self):
        # テストケース名を示す属性を問い合わせて、
        # 返却されたオブジェクトを関数的に呼び出す。
        # Plaggable Selectorパターン
        method = getattr(self, self.name)
        method()
    def testMethod(self):
        self.wasRun = 1

test = WasRun('testMethod')
print(test.wasRun)
test.run()
print(test.wasRun)
