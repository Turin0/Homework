import runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Кейс заморожен')
    def test_walk(self):
        runner_1 = runner.Runner(name='Vas')
        for _ in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen, 'Кейс заморожен')
    def test_run(self):
        runner_2 = runner.Runner(name='Soul')
        for _ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen, 'Кейс заморожен')
    def test_challenge(self):
        runner_1 = runner.Runner(name='Vas')
        runner_2 = runner.Runner(name='Soul')
        for i in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)
