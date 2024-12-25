import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_1 = runner.Runner('Danil')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = runner.Runner('Alex')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        runner_1 = runner.Runner('Danil')
        runner_2 = runner.Runner('Alex')
        for i in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

if __name__ == '__main__':
    unittest.main()
