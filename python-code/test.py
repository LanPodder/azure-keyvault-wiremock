from os import environ

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

secret = SecretClient(
    vault_url=environ["KEYVAULT"], credential=DefaultAzureCredential()
).get_secret("my-secret")
data = str(secret.value)
print(data)