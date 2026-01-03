# python-check-url ✅

[![Check URL](https://github.com/carlosalbertomagnoferreira/python-check-url/actions/workflows/check-url.yml/badge.svg)](https://github.com/carlosalbertomagnoferreira/python-check-url/actions/workflows/check-url.yml)

**Verifica rapidamente o status HTTP de uma URL via CLI.**


## 🚀 Descrição

`python-check-url` é um script simples em Python que faz um GET em uma URL informada e reporta se o site está OK (2xx) ou redirecionando (3xx) — ou mostra o erro caso contrário.

É útil para checagens rápidas, integração em pipelines (ex.: GitLab CI) ou monitoramentos básicos.

---

## 🧩 Requisitos

- Python 3.13+
- Dependência: `requests`

Instale a dependência manualmente:

```bash
pip install requests
```

> Observação: o script atual desabilita verificações de certificado (`verify=False`) para permitir checagens em ambientes com certificados autoassinados.

---

## ⚙️ Como usar

Executar diretamente com Python passando a URL como argumento:

```bash
python check_url.py https://example.com
```

Exemplo de saída esperada:

- Em caso de sucesso (2xx/3xx):
```
Site - https://example.com: OK
```
- Em caso de erro (ex.: 404, 500):
```
Erro - Status Code 404: Not Found
```
- Em caso de parâmetro inválido ou ausência de argumento, o script imprime uma mensagem de erro.

---

## 🧪 Integração com CI

### GitLab (exemplo)

O repositório já contém um exemplo de job no arquivo `.gitlab-ci.yml` que executa o script manualmente:

```yaml
run_python_script:
  stage: check-url
  image: python:3.13.11-alpine3.23
  when: manual
  script:
    - python check_url.py $url
```

Basta definir a variável `url` no pipeline (ou no job) para que o job rode.

### GitHub Actions (disponível)

Também existe um workflow para GitHub Actions em `.github/workflows/check-url.yml` com acionamento manual (`workflow_dispatch`) que recebe um input `url`. Para executar:

- Pela interface: acesse a aba **Actions**, selecione **Check URL** e clique em **Run workflow**; informe `url` e confirme.
- Pela CLI (opcional): `gh workflow run check-url.yml -f url=https://example.com`

O workflow usa a mesma imagem `python:3.13.11-alpine3.23`, instala `requests` e executa `python check_url.py $url`.

---

## 🔒 Segurança e melhorias

- Atualmente as requisições ignoram validação TLS; considere ativar `verify` em ambientes de produção.

---

## 🙋‍♂️ Contribuições

Pull requests e issues são bem-vindos. Para algo pequeno (docs, melhoria de mensagens), abra um PR direto; para mudanças maiores, abra uma issue primeiro.
