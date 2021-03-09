import Tasks


class TestTasks:
    def test_fizz(self):
        assert Tasks.fizzbuzz(3) == 'Fizz'

    def test_fizzbuzz_buzz(self):
        assert Tasks.fizzbuzz(5) == 'Buzz'

    def test_fizzbuzz_fizzbuzz(self):
        assert Tasks.fizzbuzz(15) == 'FizzBuzz'


class TestTaskSquareEquation:
    def test_square_equation(self):
        assert Tasks.square_equation(1, 0, -1) == 2
