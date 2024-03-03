#!/usr/bin/env python3

import connexion
import os
from dotenv import load_dotenv

from swagger_server import encoder

load_dotenv(override=True)

def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Coding Challenge: NL Search'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
