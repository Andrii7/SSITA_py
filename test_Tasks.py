import Tasks

class TestTasks:
    def test_fizz(self):
        assert Tasks.fizzbuzz(3) == 'Fizz'

    def test_fizzbuzz_buzz(self):
        assert Tasks.fizzbuzz(5) == 'Buzz'

    def test_fizzbuzz_fizzbuzz(self):
        assert Tasks.fizzbuzz(15) == 'FizzBuzz'



