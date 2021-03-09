import Tasks


class TestTasksProfit:
    def test_profit(self):
        assert Tasks.profit({
          "cost_price": 32.67,
          "sell_price": 45.00,
          "quantity": 1200
        }
        ) == 14796
