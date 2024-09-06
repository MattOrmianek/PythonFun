import atexit

@atexit.register
def exit_handler() -> None:
    print("We're exiting now!")

def main() -> None:
    for i in range(10):
        print(i*i)

if __name__ == '__main__':
    main()