#!/bin/bash
# sends JSON POST request to url
curl -s -X POST -H "Content-Type: application/json" -d "@$2" "$1"
