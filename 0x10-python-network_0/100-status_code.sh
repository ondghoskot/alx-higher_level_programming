#!/bin/bash
# displays status of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
