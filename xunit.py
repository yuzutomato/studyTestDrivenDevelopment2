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
        self.log = 'setUp '
    def testMethod(self):
        self.log = self.log + 'testMethod '

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun('testMethod')
    def testTemplateMethod(self):
        self.test.run()
        assert("setUp testMethod " == self.test.log)

TestCaseTest('testTemplateMethod').run()
