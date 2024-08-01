import logging
import unittest
import runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Кейс заморожен')
    def test_walk(self):
        try:
            runner_1 = runner.Runner(name='Vas', speed=-1)
            for _ in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
            logging.info('"test_walk", выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Кейс заморожен')
    def test_run(self):
        try:
            runner_2 = runner.Runner(name=3)
            for _ in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
            logging.info('"test_run", выполнен успешно')
        except:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)

    @unittest.skipIf(is_frozen, 'Кейс заморожен')
    def test_challenge(self):
        runner_1 = runner.Runner(name='Vas')
        runner_2 = runner.Runner(name='Soul')
        for i in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)
