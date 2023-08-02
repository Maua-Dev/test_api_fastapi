from src.app.main import read_root, get_history, withdraw, deposit


class Test_App:
    def test_read_root(self):
        resp = read_root()

        assert resp == {
            "name": "Vitor Soller",
            "agency": "7777",
            "account": "69420-7",
            "current_balance": 1000.0
        }

    def test_get_history(self):
        resp = get_history()

        assert resp == {
            'all_transactions' : [
                {
                    "type" : "deposit",
                    "value" : 100.0,
                    "current_balance": "1000.0",
                    "timestamp" : 1690482853890
                },
            ]
        }
        
    def test_withdraw(self):
        resp = withdraw({
            "200": 1,
            "100": 1,
            "50": 1,
            "20": 1,
            "10": 1,
            "5": 1,
            "2": 1
        })

        assert type(resp) == dict
        assert resp['type'] == 'withdraw'
        assert resp['current_balance'] == 613.0
        assert resp['value'] == 387.0
        assert type(resp['timestamp']) == float
        
    def test_deposit(self):
        resp = deposit({
            "200": 1,
            "100": 1,
            "50": 1,
            "20": 1,
            "10": 1,
            "5": 1,
            "2": 1
        })

        assert type(resp) == dict
        assert resp['type'] == 'deposit'
        assert resp['current_balance'] == 1000
        assert resp['value'] == 387.0
        assert type(resp['timestamp']) == float

