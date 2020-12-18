#!/bin/bash
# cURL only methods: displays all HTTP methods allowed by the server
curl -sI "$1" | grep Allow: | cut -d ' ' -f2-
