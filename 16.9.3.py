class Client :
    def __init__(self, name, purse):
        self.name = name
        self.purse = purse

    def getClient(self):
        return f"Клиент: {self.name} , Баланс: {self.purse} рублей."

client_1 = Client("Янис Петров", 50)

print(client_1.getClient())