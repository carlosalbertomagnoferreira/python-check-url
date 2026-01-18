# python-check-url ✅

[![Check URL](https://github.com/carlosalbertomagnoferreira/python-check-url/actions/workflows/check-url.yml/badge.svg)](https://github.com/carlosalbertomagnoferreira/python-check-url/actions/workflows/check-url.yml)

**Verifica rapidamente o status HTTP de uma URL via CLI.**


## 🚀 Descrição

`python-check-url` é um script simples em Python que faz um GET em uma URL informada e reporta se o site está OK (2xx) ou redirecionando (3xx) — ou mostra o erro caso contrário.

É útil para checagens rápidas, integração em pipelines (ex.: GitLab CI) ou monitoramentos básicos.

---

## 🧩 Requisitos

- Python 3.13+
- Gerenciador de dependências: `uv`

### Instalação do UV

O `uv` é um gerenciador de pacotes Python rápido e moderno. Instale-o com:

```bash
pip install uv
```

> Observação: o script atual desabilita verificações de certificado (`verify=ssl=False`) para permitir checagens em ambientes com certificados autoassinados.

---

## ⚙️ Como usar

### Configuração inicial

Antes de usar o script, sincronize as dependências com:

```bash
uv sync
```

### Executando o script

Execute o `main.py` passando a URL como argumento:

```bash
uv run python main.py https://example.com
```

### Opções disponíveis

```bash
uv run python main.py <url> [--timeout SEGUNDOS] [--insecure] [--verbose]
```

**Argumentos:**
- `<url>` (obrigatório): URL a ser verificada
- `--timeout SEGUNDOS` (opcional): Tempo máximo de espera em segundos (default: 5)
- `--insecure` (opcional): Desabilita validação de certificado SSL/TLS
- `--verbose` (opcional): Ativa modo verbose com mensagens de debug

### Exemplos

Verificação simples:
```bash
uv run python main.py https://example.com
```

Com timeout customizado:
```bash
uv run python main.py https://example.com --timeout 10
```

Ignorando validação SSL:
```bash
uv run python main.py https://example.com --insecure
```

Com verbose:
```bash
uv run python main.py https://example.com --verbose
```

### Saída esperada

- **Sucesso (2xx/3xx):**
```
2026-01-17 10:30:45,123 - INFO - Site https://example.com está acessível (200 OK)
```

- **Erro (4xx/5xx):**
```
2026-01-17 10:30:45,123 - WARNING - Site https://example.com retornou status 404 (Not Found)
```

- **Falha de conexão:**
```
2026-01-17 10:30:45,123 - ERROR - Erro de conexão ao acessar https://example.com
```

**Código de saída:**
- `0`: URL acessível (2xx ou 3xx)
- `1`: URL inacessível ou erro na requisição

---

## 🧪 Integração com CI

### GitLab (exemplo)

O repositório já contém um exemplo de job no arquivo `.gitlab-ci.yml` que executa o script manualmente:

```yaml
run_python_script:
  stage: check-url
  image: python:3.13.11-alpine3.23
  when: manual
  before_script:
    - python --version
    - pip install uv
    - uv sync
  script:
    - echo "Running Python script..."
    - uv run python main.py $url
```

Basta definir a variável `url` no pipeline (ou no job) para que o job rode.

### GitHub Actions (disponível)

Também existe um workflow para GitHub Actions em `.github/workflows/check-url.yml` com acionamento manual (`workflow_dispatch`) que recebe um input `url`. Para executar:

- Pela interface: acesse a aba **Actions**, selecione **Check URL** e clique em **Run workflow**; informe `url` e confirme.
- Pela CLI (opcional): `gh workflow run check-url.yml -f url=https://example.com`

O workflow usa a mesma imagem `python:3.13.11-alpine3.23`, instala `uv`, sincroniza as dependências e executa `uv run python main.py $url`.

---

## 🙋‍♂️ Contribuições

Pull requests e issues são bem-vindos. Para algo pequeno (docs, melhoria de mensagens), abra um PR direto; para mudanças maiores, abra uma issue primeiro.
