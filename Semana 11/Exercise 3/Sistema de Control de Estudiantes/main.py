from actions import control

def main():
    control()

if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(f'An unexpected error occurred: {ex}')
