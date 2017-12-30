class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def run(self):
        self.setUp()
        # テストケース名を示す属性を問い合わせて、
        # 返却されたオブジェクトを関数的に呼び出す。
        # Plaggable Selectorパターン
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def setUp(self):
        self.wasRun = None
        self.wasSetUp = 1
    def testMethod(self):
        self.wasRun = 1

class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun('testMethod')
        test.run()
        assert(test.wasRun)
    def testSetUp(self):
        test = WasRun('setUp')
        test.run()
        assert(test.wasSetUp)

TestCaseTest('testRunning').run()
TestCaseTest('testSetUp').run()
