#!/usr/bin/env python
"""Script para realizar check de URL."""

import sys
from http import HTTPStatus

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

header = {"User-Agent": "python"}

def check_param(params):
    """Verifica se foi passado paramentro para a função."""
    try:
        site = params[1]
        check_url(site)
    except Exception as e:
        print(f'Erro na url informada: {e}')
        return


def check_url(url):
    """Realiza do check da url passada."""
    check = requests.get(url, headers=header, verify=False)
    if (
        HTTPStatus(check.status_code).is_success
        or HTTPStatus(check.status_code).is_redirection
    ):
        print(f'Site - {url}: OK')
    else:
        print(f'Erro - Status Code {check.status_code}: {check.reason}')


if __name__ == '__main__':
    check_param(sys.argv)
