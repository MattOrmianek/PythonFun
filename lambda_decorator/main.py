from datetime import datetime

@lambda func: func()
def program_start_time() -> str:
    return f'Program started at {datetime.now()}'

print(program_start_time)