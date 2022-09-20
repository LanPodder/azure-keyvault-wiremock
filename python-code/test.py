from os import environ

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

import requests

secret = SecretClient(
    vault_url=environ["KEYVAULT"], credential=DefaultAzureCredential()
).get_secret("my-secret")
data = str(secret.value)
print(data)

x = requests.get(f'{environ["KEYVAULT"]}/secrets/my-secret/?api-version=7.3')
print(x.status_code)
print(x.json())