FROM python

COPY python-code/requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt

RUN mkdir /app

COPY python-code /app

RUN mkdir /certs
COPY mock/certs /certs
ENV KEYVAULT=https://localhost:8443
ENV REQUESTS_CA_BUNDLE=/certs/client-cert.crt