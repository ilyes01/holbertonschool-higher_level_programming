#!/bin/bash
# size of the status code of the response
curl -so /dev/null -w '%{http_code}' "$1"
