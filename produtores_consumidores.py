import threading
import time
from buffer import Buffer

class Produtor(threading.Thread):
    def __init__(self, buffer, id_produtor, timesteps):
        threading.Thread.__init__(self)
        self.buffer = buffer
        self.id_produtor = id_produtor
        self.timesteps = timesteps

    def run(self):
        for t in range(self.timesteps):
            item = f"Peça_{self.id_produtor}_{t}"
            self.buffer.adicionar_item(item)
            time.sleep(1)  # Simula o tempo de produção

class Consumidor(threading.Thread):
    def __init__(self, buffer, id_consumidor, timesteps):
        threading.Thread.__init__(self)
        self.buffer = buffer
        self.id_consumidor = id_consumidor
        self.timesteps = timesteps

    def run(self):
        for t in range(self.timesteps):
            item = self.buffer.remover_item()
            time.sleep(1.5)  # Simula o tempo de consumo
