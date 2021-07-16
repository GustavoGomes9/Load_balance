class LimitException(Exception):
    pass

class User:
    ttask = 0

    def __init__(self):
        self.ttask_left = User.ttask
    
    @staticmethod #porque usar static ?????
    def check_ttask():
        if User.ttask < 1 or User.ttask > 10:
            raise LimitException("ttask não corresponde formula '1 < ttask < 10'")
        return 0

    def remove_tick(self):
        self.ttask_left -= 1
        if self.ttask_left < 0:
            raise Exception("Ocorreu um erro!")
        return self.ttask_left

class Server:
    umax = 0 

    def __init__(self, users):
        self.users = users

    @staticmethod
    def check_umax():
        if Server.umax < 1 or Server.umax > 10:
            raise LimitException("umax não corresponde formula '1 < umax < 10'")

    def check_if_available(self):
        if len(self.users) < Server.umax:
           return True
        else:
            return False
    
    def remove_tick_users(self):
        self.users[:] = [user for user in self.users if user.remove_tick()]
        return self.usuarios

class LoadBalance:
    
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer
        self.server_total = 0
        self.servers = []

    def make_balance(self):
        input_line = False
        while self.servers or not input_line:
            new_users = self.read_tick()
            if new_users is False and input_line is False:
                input_line = True
            elif new_users is not False:
                self.create_new_users(new_users) 

            self.server_cost += len(self.servers)
            self.start_write_exit()
            self.remove_tick_server()
        self.write_end()
    
    def read_tick(self):
        line = self.reader.readline() # atribui a leitura da primeira linha do documento 'input.txt' a variavel
        if line: 
            return int(line)
        else:
            return False
        
    def create_new_users(self, new_users):
        for range in (new_users):
            user_in_space = False
            for server in self.servers:
                if server.check_if_available(): 
                    server.user.append(User()) 
                    user_in_space = True
                elif user_in_space is False:
                    self.servers.append(Server([User()]))
    
    def start_write_exit(self):
        exit = ''
        for i, server in enumerate(self.servers):

            if i + 1 == len(self.servers):
                exit += '%s\n' % len(server.users)
            else:
                exit += '%s,' % len(server.users)

        self.writer.write(exit)
        return exit
    
    def remove_tick_server(self):
        self.servers[:] = [server for server in self.servers if server.remove_tick_users()]

    def online_user(self):
        count = 0
        for server in self.servers:
            count += len(server.users)
        return count
    
    def write_end(self):
        self.writer.write(str(
            self.online_user()) + '\n')  # Usuários ativos ao termino da execução das tarefas, que deve ser 0 nesse ponto
        self.writer.write(str(self.server_total))


def main():
    try:
        with open('input.txt', 'r') as reader, open('output.txt', 'w') as writer:
            start_balance_object = LoadBalance(reader, writer)
            User.ttask = int(reader.readline())
            Server.umax = int(reader.readline())
            User.check_ttask()# verificação de valores ttask
            Server.check_umax()# verificação de valores umax
            start_balance_object.make_balance()
            
    except Exception as error:
        print(error)
    return 0

main()