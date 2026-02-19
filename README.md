# teste-completo

Projeto FastAPI criado com Backstage, incluindo CI/CD e deploy automático via ArgoCD.

[![CI/CD](https://github.com/backstage-learning-durelli/teste-completo/actions/workflows/ci-cd.yaml/badge.svg)](https://github.com/backstage-learning-durelli/teste-completo/actions/workflows/ci-cd.yaml)

## 🚀 Tecnologias

- Python 3.11+
- FastAPI 0.109+
- Poetry (dependency management)
- pytest (testing)
- uvicorn (ASGI server)

## 📋 Pré-requisitos

- Python 3.11 ou superior
- Poetry 1.7 ou superior

## 🔧 Como rodar

### Desenvolvimento

```bash
# Instalar dependências
poetry install

# Executar a aplicação
poetry run uvicorn app.main:app --reload
```

A aplicação estará disponível em `http://localhost:8000`

### Documentação API

FastAPI gera documentação automática:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🌐 Endpoints

### Health Check
```
GET http://localhost:8000/health
```

Resposta:
```json
{
  "status": "healthy",
  "service": "teste-completo",
  "version": "1.0.0"
}
```

### Hello Endpoint
```
GET http://localhost:8000/api/hello
```

Resposta:
```json
{
  "message": "Hello from teste-completo!"
}
```

### Info Endpoint
```
GET http://localhost:8000/api/info
```

Resposta:
```json
{
  "name": "teste-completo",
  "version": "1.0.0",
  "framework": "FastAPI",
  "python_version": "3.11+"
}
```

## 🧪 Testes

```bash
# Executar testes
poetry run pytest

# Executar testes com coverage
poetry run pytest --cov=app --cov-report=html

# Executar apenas um teste específico
poetry run pytest tests/test_routes.py::test_health_check
```

## 🎨 Formatação e Linting

```bash
# Formatar código com Black
poetry run black app tests

# Ordenar imports com isort
poetry run isort app tests

# Verificar com flake8
poetry run flake8 app tests

# Type checking com mypy
poetry run mypy app
```

## 🐳 Docker

```bash
# Build da imagem
docker build -t teste-completo:latest .

# Executar container
docker run -p 8000:8000 teste-completo:latest

# Verificar health check
curl http://localhost:8000/health
```

## 🔄 CI/CD e Deploy

### Pipeline Automático (GitHub Actions)

Este projeto possui um pipeline de CI/CD configurado que é executado automaticamente:

**Em Pull Requests:**
- Executa testes unitários com coverage
- Gera relatórios de cobertura

**No branch `main`:**
1. ✅ Executa testes
2. ✅ Builda a aplicação com Poetry
3. ✅ Cria imagem Docker otimizada
4. ✅ Publica no Docker Hub (`durellirsd/teste-completo`)
5. ✅ Atualiza manifestos Kubernetes com nova tag
6. ✅ Commit automático da mudança

### Deploy via ArgoCD

O deploy é gerenciado pelo ArgoCD usando GitOps:

- **Application**: `teste-completo`
- **Namespace**: `teste-completo`
- **Sync Policy**: Automático (prune + self-heal)

**Acessar no ArgoCD:**
```bash
# Via CLI
argocd app get teste-completo
argocd app sync teste-completo

# Ver logs
kubectl logs -n teste-completo -l app=teste-completo -f
```

### Estrutura de Deploy

```
k8s/
├── deployment.yaml  # Deployment com 2 réplicas
├── service.yaml     # ClusterIP na porta 80
└── ingress.yaml     # Ingress (opcional)
```

**Verificar recursos no Kubernetes:**
```bash
# Ver todos os recursos
kubectl get all -n teste-completo

# Acessar a aplicação (port-forward)
kubectl port-forward -n teste-completo svc/teste-completo 8000:80
curl http://localhost:8000/api/hello

# Ver logs da aplicação
kubectl logs -n teste-completo -l app=teste-completo -f
```

## 📁 Estrutura do Projeto

```
teste-completo/
├── app/
│   ├── __init__.py
│   ├── main.py              # Aplicação principal
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py        # Rotas da API
│   └── core/
│       ├── __init__.py
│       └── config.py        # Configurações
├── tests/
│   ├── __init__.py
│   └── test_routes.py       # Testes
├── k8s/                     # Manifestos Kubernetes
├── .github/workflows/       # CI/CD
├── Dockerfile
├── pyproject.toml           # Dependências Poetry
└── README.md
```

## 🔐 Configurações de Secrets

Para o pipeline funcionar, configure os seguintes secrets no GitHub:

- `DOCKERHUB_USERNAME`: Seu username do Docker Hub
- `DOCKERHUB_TOKEN`: Token de acesso do Docker Hub

**Como criar:**
1. Acesse: Repository → Settings → Secrets and variables → Actions
2. Clique em "New repository secret"
3. Adicione os secrets necessários

## 📝 Adicionando Novos Endpoints

1. Crie ou edite arquivos em `app/api/`
2. Defina modelos Pydantic para request/response
3. Adicione testes correspondentes em `tests/`
4. Execute os testes localmente
5. Commit e push - o CI/CD fará o resto!

## 🤝 Contribuindo

1. Crie uma branch: `git checkout -b feature/nova-feature`
2. Faça suas alterações
3. Execute testes: `poetry run pytest`
4. Commit: `git commit -m 'feat: adiciona nova feature'`
5. Push: `git push origin feature/nova-feature`
6. Abra um Pull Request

---

**Criado com ❤️ pelo Backstage Platform Team**
