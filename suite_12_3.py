import unittest
import Test_runner_12_3
import Test_Tournament_12_3

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_Tournament_12_3.TournamentTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(Test_runner_12_3.RunnerTest))

run = unittest.TextTestRunner(verbosity=2)
run.run(runnerST)