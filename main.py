from environment import Environment

def main():
    environment = Environment(1000, 600)
    while True:
        environment.update()
        
if __name__ == "__main__":
    main()