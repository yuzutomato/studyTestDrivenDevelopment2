class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def run(self):
        self.setUp()
        # テストケース名を示す属性を問い合わせて、
        # 返却されたオブジェクトを関数的に呼び出す。
        # Plaggable Selectorパターン
        method = getattr(self, self.name)
        method()
        self.tearDown()
        return TestResult()

class WasRun(TestCase):
    def setUp(self):
        self.log = 'setUp '
    def testMethod(self):
        self.log = self.log + 'testMethod '
    def tearDown(self):
        self.log = self.log + 'tearDown '

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun('testMethod')
        test.run()
        assert test.log == 'setUp testMethod tearDown '
    def testResult(self):
        test = WasRun('testMethod')
        result = test.run()
        assert result.summary() == '1 run, 0 failed'

class TestResult:
    def __init__(self):
        self.runCount = 1
    def summary(self):
        return '%d run, 0 failed' % self.runCount

TestCaseTest('testTemplateMethod').run()
TestCaseTest('testResult').run()
