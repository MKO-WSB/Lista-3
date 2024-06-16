import subprocess
import json

def send_request(url):
    result = subprocess.run(['curl', '-s', url], stdout=subprocess.PIPE)
    return result.stdout

def check_status_code(response):
    try:
        response_json = json.loads(response)
        return True
    except json.JSONDecodeError:
        return False

def check_key_elements(response, keys):
    response_json = json.loads(response)
    return all(key in response_json for key in keys)

def run_tests():
    tests = [
        {
            'url': 'https://jsonplaceholder.typicode.com/posts/1',
            'keys': ['userId', 'id', 'title']
        },
        {
            'url': 'https://jsonplaceholder.typicode.com/users/1',
            'keys': ['id', 'name', 'username']
        },
        {
            'url': 'https://jsonplaceholder.typicode.com/todos/1',
            'keys': ['userId', 'id', 'title']
        }
    ]

    for i, test in enumerate(tests, start=1):
        response = send_request(test['url'])
        status_ok = check_status_code(response)
        keys_ok = check_key_elements(response, test['keys'])

        if status_ok and keys_ok:
            print(f"Test {i}: PASSED")
        else:
            print(f"Test {i}: FAILED")

if __name__ == '__main__':
    run_tests()
