# generates the client from the openapi spec

## Install deps for this script:
# pip install pipx
# pipx install openapi-python-client --include-deps

# run the server and get the spec
openapi-python-generate --url http://localhost:8000/openapi.json
