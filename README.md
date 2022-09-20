# azure-keyvault-wiremock

Example on how to mock azure-keyvault for local testing using wiremock.

Run the code by running the wiremock mock first using `docker compose up`
and then the python code by either using `docker build --file python-code/Dockerfile . --tag pcode && docker run --net=host pcode python3 /app/test.py`
or by running it directly on the machine using `KEYVAULT=https://localhost:8443 REQUESTS_CA_BUNDLE=$PWD/mock/certs/client-cert.crt python3 python-code/test.py`