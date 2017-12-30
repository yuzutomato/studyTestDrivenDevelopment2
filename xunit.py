class TestCase:
    def __init__(self, name):
        self.name = name
    def run(self):
        # テストケース名を示す属性を問い合わせて、
        # 返却されたオブジェクトを関数的に呼び出す。
        # Plaggable Selectorパターン
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = None
        super().__init__(name)
    def testMethod(self):
        self.wasRun = 1

test = WasRun('testMethod')
print(test.wasRun)
test.run()
print(test.wasRun)
