# simple-python-api


## Building Locally
```
docker build -t python-api -f ContainerFile .
```

## Running Locally
```
docker run --rm -it --name python-api  \
  -e="APP_ENV=local" \
  -p 8888:8000 \
  python-api:latest
```

for elatic apm agent add the env vars below
```
  -e="ELASTIC_APM_SERVICE_NAME=simple-python-api" \
  -e="ELASTIC_APM_SERVER_URL=http://apm-server:8200" \
  -e="ELASTIC_APM_SECRET_TOKEN=123456"
```

## Running Development Environemnt
```
docker run --rm -it --name python-api  \
  -e="APP_ENV=local" \
  -p 8888:8000 \
  -v $PWD/:/app/ \
  python-api:latest --host=0.0.0.0 --port=8000 --reload
```

# Accessing
http://localhost:8888/books

Postman collection is inside this repository