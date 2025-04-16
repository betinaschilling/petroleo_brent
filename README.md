# Projeto de Previsão Ndo Petróleo Brent

Este projeto realiza uma previsão naive para o preço do petróleo Brent.

## Organização:

- `1_data/`: Dados brutos, processados e previsões.
- `2_notebook/`: Análise exploratória inicial.
- `3_src/`: Scripts de processamento e modelo naive.
- `4_models/`: Diretório para modelos treinados (não utilizado no modelo naive).
- `5_reports/`: Documentação e relatórios do projeto.

## Como executar:

```bash
conda activate base
python 3_src/data_processing.py
python 3_src/modeling.py