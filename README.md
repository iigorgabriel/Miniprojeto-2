# Sistema de Controle para Linha de Produção Industrial

Este projeto simula uma linha de produção automatizada, utilizando paralelismo com threads, semáforos e mutexes para controlar a produção e o consumo de peças em um buffer compartilhado.

## Descrição do Projeto

O sistema cria uma linha de produção onde peças são produzidas, armazenadas em um buffer e consumidas em etapas subsequentes. A sincronização é gerida por:
- **Threads**: simulam produção e consumo paralelos.
- **Semáforos e Mutexes**: controlam o acesso ao buffer, evitando conflitos e condições de corrida.

## Tecnologias Utilizadas

- **Python**
- **Bibliotecas**: `threading`, `time`, `queue`

## Estrutura do Código

- **`buffer_size`**: Capacidade máxima do buffer.
- **`produce()` e `consume()`**: Funções para produção e consumo de peças, sincronizadas com semáforos e mutexes para controle do fluxo.
  
## Como Executar o Projeto

1. Clone o repositório.
2. Ajuste `buffer_size`, `production_time`, e `consumption_time` para simular diferentes cargas.
3. Execute o script para iniciar a simulação.