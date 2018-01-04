class TestCase:
    def __init__(self, name):
        self.name = name
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            # テストケース名を示す属性を問い合わせて、
            # 返却されたオブジェクトを関数的に呼び出す。
            # Plaggable Selectorパターン
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result

class WasRun(TestCase):
    def setUp(self):
        self.log = 'setUp '
    def testMethod(self):
        self.log = self.log + 'testMethod '
    def testBrokenMethod(self):
        raise Exception
    def tearDown(self):
        self.log = self.log + 'tearDown '

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.errorCount = 0
    def testStarted(self):
        self.runCount = self.runCount + 1
    def testFailed(self):
        self.errorCount = self.errorCount + 1
    def summary(self):
        return '%d run, %d failed' % (self.runCount, self.errorCount)

class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun('testMethod')
        test.run()
        assert test.log == 'setUp testMethod tearDown '
    def testResult(self):
        test = WasRun('testMethod')
        result = test.run()
        assert result.summary() == '1 run, 0 failed'
    def testFailedResult(self):
        test = WasRun('testBrokenMethod')
        result = test.run()
        assert result.summary() == '1 run, 1 failed'
    # テストが失敗したも期待した内容が出力されるか確かめる。
    # TestResultに対するテストであることに注意する。
    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert result.summary() == '1 run, 1 failed'
    def testSuite(self):
        suite = TestSuite()
        suite.add(WasRun('testMethod'))
        suite.add(WasRun('testBrokenMethod'))
        result = suite.run()
        assert result.summary() == '2 run, 1 failed'

print(TestCaseTest('testTemplateMethod').run().summary())
print(TestCaseTest('testResult').run().summary())
print(TestCaseTest('testFailedResult').run().summary())
print(TestCaseTest('testFailedResultFormatting').run().summary())
print(TestCaseTest('testSuite').run().summary())
