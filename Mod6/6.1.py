import random

def noppa():
     return random.randint(1,6)
def main():
    luku= 0
    while luku !=6:
        luku= noppa()
        print(f"Nopan luku on: {luku}")
if __name__ == "__main__":
    main()
