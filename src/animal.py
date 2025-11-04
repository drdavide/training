import sys

def default():
    print("Hello, world!")

def cat():
    print("meow")

def main():
    if sys.argv[1] == 'cat':
        cat()
    else:
        default()

if __name__ == "__main__":
    main()