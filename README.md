# Dashboard de Temperaturas IoT

Projeto desenvolvido para análise de dados de temperatura coletados por dispositivos IoT, utilizando PostgreSQL, Docker e Streamlit para visualização interativa.


## 🎥 Apresentação do Projeto

Clique no link abaixo para assistir à demonstração completa do dashboard e explicação do pipeline:

👉 [Assistir ao vídeo](https://www.youtube.com/watch?v=siV-DgenpIE)


## Tecnologias utilizadas

* Python
* Streamlit
* PostgreSQL
* Docker
* Pandas
* Plotly

## Funcionalidades

O dashboard apresenta:

* Indicadores gerais (KPIs)

  * Temperatura máxima e mínima para ambiente interno (In) e externo (Out)

* Comparação de temperatura

  * Análise entre ambiente interno e externo ao longo do tempo

* Leituras por hora

  * Distribuição da quantidade de medições ao longo do dia

* Temperaturas por dia

  * Máximas e mínimas diárias

## Insights obtidos

* O ambiente externo apresenta temperaturas mais elevadas e maior variação ao longo do tempo
* O ambiente interno se mantém mais estável
* Existem padrões de coleta de dados em determinados horários do dia
* As variações diárias seguem um comportamento consistente

## Banco de dados

O projeto utiliza PostgreSQL com:

Tabela:

* temperature_readings

Views:

* temp_in_out
* leituras_por_hora
* temp_max_min_por_dia
* temp_in_out_timeline

As views são responsáveis por transformar os dados brutos em informações analíticas utilizadas no dashboard.


## Como executar o projeto

### Instalar dependências

pip install -r requirements.txt

### Executar aplicação

python -m streamlit run dashboard.py

## Execução com Docker

docker build -t iot-dashboard .
docker run -p 8501:8501 iot-dashboard

## Acesso

Após executar, acesse no navegador:
http://localhost:8501

## Objetivo do projeto

Demonstrar a aplicação de conceitos de análise de dados, visualização interativa, integração com banco de dados e uso de containers.

## Autor

Thiago Henrique
Estudante de Análise e Desenvolvimento de Sistemas
