import json
class Assertutil:
    def __init__(self):
        pass
    def assert_in_body(self, body, expected_body):
        try:
            body = json.dumps(body)
            expected_body = json.dumps(expected_body)
            assert expected_body in body
            return True
        except:
            raise