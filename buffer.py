import threading

class Buffer:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.buffer = []
        self.mutex = threading.Lock()  # Garante que só uma thread acessa o buffer por vez
        self.espaco_disponivel = threading.Semaphore(capacidade)  # Inicializa com capacidade máxima
        self.itens_disponiveis = threading.Semaphore(0)  # Inicializa com zero itens disponíveis

    def adicionar_item(self, item):
        self.espaco_disponivel.acquire()  # Espera por espaço no buffer
        with self.mutex:  # Bloqueia o buffer para acesso único
            self.buffer.append(item)
            print(f"Item {item} adicionado. Buffer: {len(self.buffer)} itens.")
        self.itens_disponiveis.release()  # Notifica que há um item disponível

    def remover_item(self):
        self.itens_disponiveis.acquire()  # Espera por um item disponível no buffer
        with self.mutex:  # Bloqueia o buffer para acesso único
            item = self.buffer.pop(0)
            print(f"Item {item} removido. Buffer: {len(self.buffer)} itens.")
        self.espaco_disponivel.release()  # Notifica que há espaço disponível
        return item
