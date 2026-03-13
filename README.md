# Projeto IoT, Big Data e Inteligência Artificial com Docker

## Descrição

Este projeto acadêmico demonstra a integração de tecnologias modernas utilizadas no desenvolvimento de soluções baseadas em dados. A aplicação simula sensores de Internet das Coisas (IoT), realiza o processamento de dados e utiliza um modelo simples de Inteligência Artificial para gerar previsões.

Toda a aplicação foi containerizada utilizando Docker, garantindo portabilidade e facilidade de execução em diferentes ambientes.

## Tecnologias utilizadas

- Python
- Pandas
- Scikit-learn
- Docker
- GitHub Codespaces

## Estrutura do projeto

iot-bigdata-ai-project

app.py → aplicação principal  
requirements.txt → dependências Python  
Dockerfile → configuração do container  
README.md → documentação do projeto  

## Funcionamento da aplicação

1. Sensores IoT simulados geram dados de temperatura e umidade.
2. Os dados são armazenados em um dataset utilizando a biblioteca Pandas.
3. Um modelo de Machine Learning é treinado para identificar padrões entre temperatura e umidade.
4. O modelo realiza uma previsão baseada em novos dados de temperatura.

## Containerização

O projeto utiliza Docker para empacotar a aplicação e suas dependências em um container executável.

### Construção da imagem
docker build -t iot-ai-app .

### Executar o container

docker run -p 8501:8501 iot-ai-app

## Dashboard

Após executar o container, o dashboard poderá ser acessado na porta:

http://localhost:8501

## Exemplo de saída

Dados coletados dos sensores IoT  
Temperatura: 26  
Umidade: 62  

Previsão de umidade para temperatura de 30°C: 60.25