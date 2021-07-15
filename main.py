class User:
    pass

class Server:
    pass

class LoadBalance:
    
    def __init__(self):
        self.reader
        self.writer
        self.server_total = 0
        self.server = []

def main():
    try:
        with open('input.txt', 'r') as reader, open('output.txt', 'w') as writer:
            load_balance_object = LoadBalance(reader, writer)
            User.ttask = int(reader.readline())
            Server.umax = int(reader.readline())
    except Exception as error:
        print(error)
    return 0

main()