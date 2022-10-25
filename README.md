# bill-reader

> Microserviço da FERCEN para leitura de contas de energia.

## Documentação

A documentação da API é gerada automaticamente e está disponível na rota `/docs`.  
Em resumo, a API possui duas rotas: `/` e `/reader/`.

### Rota `/` (root)

Método: **GET**  
Descrição: Esta rota apenas retorna informações sobre o app.  
Modelo de resposta:
```json
{
    "app_name": "string",
    "app_version": "string",
    "environment": "string"
}
```

### Rota `/reader/`

Método: **POST**  
Descrição: Esta rota recebe uma conta de energia em formato PDF e retorna o valor a ser pago e o mês e ano que a conta se refere.  
Modelo de body (multipart/form-data):
```json
{
    "file": string($binary)
}
```
Modelo de resposta:
```json
{
    "message": "string",
    "price": "string - somente em status 200",
    "month": "string - somente em status 200"
}
```
