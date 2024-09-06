import time
from decorators_module import retry

@retry(retries=4, delay=1)
def connect() -> None:
    time.sleep(1)
    raise Exception('Could not connect')


if __name__ == '__main__':
    connect()