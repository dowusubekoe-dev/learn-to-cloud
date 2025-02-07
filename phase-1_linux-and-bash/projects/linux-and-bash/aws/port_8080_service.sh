#!/bin/bash
while true; do
    echo -e "HTTP/1.1 200 OK\n\nCTF{port_explorer}" | nc -l -p 8080
done
