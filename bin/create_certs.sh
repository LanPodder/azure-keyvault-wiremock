#!/bin/bash
root_dir='mock/certs/'
openssl req -x509 -newkey rsa:2048 -utf8 -days 3650 -nodes -config ${root_dir}/client-cert.conf -keyout ${root_dir}/client-cert.key -out ${root_dir}/client-cert.crt
openssl pkcs12 -export -inkey ${root_dir}/client-cert.key -in ${root_dir}/client-cert.crt -out ${root_dir}/client-cert.p12 -password pass:password
keytool -importkeystore -noprompt -deststorepass password -destkeypass password -srckeystore ${root_dir}/client-cert.p12 -srcstorepass password -deststoretype pkcs12 -destkeystore ${root_dir}/client-cert.pkcs12