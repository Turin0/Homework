import unittest
import runner


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = runner.Runner(name='Усейн', speed=10)
        self.runner_2 = runner.Runner(name='Андрей', speed=9)
        self.runner_3 = runner.Runner(name='Ник', speed=3)
        self.t_list_1 = [self.runner_1, self.runner_3]
        self.t_list_2 = [self.runner_2, self.runner_3]
        self.t_list_3 = [self.runner_1, self.runner_2, self.runner_3]

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(key, value)

    @unittest.skipIf(is_frozen, 'Кейс заморожен')
    def test_t1(self):
        t1 = runner.Tournament(90, *self.t_list_1)
        t1.start()
        result = t1.finishers
        self.assertTrue(result[2] == 'Ник')
        self.all_results[1] = result

    @unittest.skipIf(is_frozen, 'Кейс заморожен')
    def test_t2(self):
        t2 = runner.Tournament(90, *self.t_list_2)
        t2.start()
        result = t2.finishers
        self.assertTrue(result[2] == 'Ник')
        self.all_results[2] = result

    @unittest.skipIf(is_frozen, 'Кейс заморожен')
    def test_t3(self):
        t3 = runner.Tournament(90, *self.t_list_3)
        t3.start()
        result = t3.finishers
        self.assertTrue(result[3] == 'Ник')
        self.all_results[3] = result
