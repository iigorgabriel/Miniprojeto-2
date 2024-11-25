from buffer import Buffer
from produtores_consumidores import Produtor, Consumidor
import time

def main():
    # Parâmetros da linha de produção
    capacidade_buffer = 50
    num_produtores = 10
    num_consumidores = 10
    timesteps = 100

    # Inicializa o buffer
    buffer = Buffer(capacidade_buffer)

    # Cria os produtores e consumidores
    produtores = [Produtor(buffer, i, timesteps) for i in range(num_produtores)]
    consumidores = [Consumidor(buffer, i, timesteps) for i in range(num_consumidores)]

    # Inicia as threads
    for produtor in produtores:
        produtor.start()
    for consumidor in consumidores:
        consumidor.start()

    # Aguarda todas as threads finalizarem
    for produtor in produtores:
        produtor.join()
    for consumidor in consumidores:
        consumidor.join()

    # Relatório final
    print("\nSimulação concluída.")
    print(f"Total de itens produzidos: {num_produtores * timesteps}")
    print(f"Total de itens consumidos: {num_consumidores * timesteps}")
    print(f"Itens restantes no buffer: {len(buffer.buffer)}")

if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"Tempo total de execução: {time.time() - start_time:.2f} segundos")
