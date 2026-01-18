#!/usr/bin/env python3
"""
Script para checar disponibilidade de uma URL.
"""

import argparse
import logging
from http import HTTPStatus

import requests
from requests.exceptions import ConnectionError, RequestException, Timeout

DEFAULT_TIMEOUT = 5
HEADERS = {"User-Agent": "url-checker/1.0"}


def check_url(url: str, timeout: int, verify_ssl: bool) -> bool:
    """
    Verifica se a URL está acessível.
    """
    try:
        response = requests.get(
            url,
            headers=HEADERS,
            timeout=timeout,
            verify=verify_ssl
        )

        status = HTTPStatus(response.status_code)

        if status.is_success or status.is_redirection:
            logging.info(
                f"Site {url} está acessível "
                f"(status={response.status_code})"
            )
            return True

        logging.warning(
            f"Site {url} retornou erro "
            f"(status={response.status_code}, "
            f"reason={response.reason})"
        )
        return False

    except Timeout:
        logging.error(f"Timeout ao acessar {url}")

    except ConnectionError:
        logging.error(f"Erro de conexão ao acessar {url}")

    except RequestException as exc:
        logging.error(f"Erro inesperado ao acessar {url}: {exc}")

    return False


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Check de disponibilidade de URL"
    )

    parser.add_argument("url", help="URL a ser verificada")
    parser.add_argument(
        "--timeout",
        type=int,
        default=DEFAULT_TIMEOUT,
        help="Timeout em segundos (default: 5)"
    )
    parser.add_argument(
        "--insecure",
        action="store_true",
        help="Desabilita validação SSL"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Ativa modo verbose"
    )

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    success = check_url(
        url=args.url,
        timeout=args.timeout,
        verify_ssl=not args.insecure
    )

    raise SystemExit(0 if success else 1)


if __name__ == "__main__":
    main()
