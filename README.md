# FHIR

## Parte 1- Configuração de servidor FHIR (Arquitetura)

### Passo a Passo realizado

1. Pesquisa e estudo sobre no repositorio [hapi-fhir-jpaserver-starter](https://github.com/hapifhir/hapi-fhir-jpaserver-starter)

2. Construção do docker-compose utilizando a [imagem docker](https://hub.docker.com/r/hapiproject/hapi)

3. Inclusão do ElasticSearch no docker-compose e no aplicacao.yml

4. Inclusão do Kibana no docker-compose para conectar ao ElasticSearch, porém nessa etapa ele quebrou o ElasticSearch.
- Possiveis caminhos para solução da inclusão do Kibana
    - Debugar o log do ElasticSearch
    - Remover o Kibana e verificar a documentação.


## Requisitos
* Docker =>  20.10.17
* Docker-compose => 1.29.2
* Python => 3.10
## Como rodar
### Subindo o docker-compose
```
docker-compose up -d
```

### Derrubando o docker-compose
```
docker-compose down
```

### Instalando depedencias do python
```
pip3 install -r requirements.txt
```

### Realizando carga de dados no servidor
```
python3 src/main.py
```