# simple-python-api


## Building Locally
```
docker build -t books-api:local -f ContainerFile .
```

## Running Locally
```
docker run --rm -it --name books-api  \
  -e="APP_ENV=local" \
  -p 8888:8000 \
  books-api:local
```
## Running Built Container
```
docker run --rm -it --name books-api  \
  -e="APP_ENV=local" \
  -p 8888:8000 \
  brpedromaia/simple-python-api:v5
```

for the elatic apm agent add the env vars below ( for local kubernetes testing env)
```
  -e="ELASTIC_APM_SERVICE_NAME=simple-python-api" \
  -e="ELASTIC_APM_SERVER_URL=http://apm-server:8200" \
  -e="ELASTIC_APM_SECRET_TOKEN=123456"
```

## Running Development Environemnt
```
git clone https://github.com/brpedromaia/simple-python-api
cd simple-python-api/
docker run --rm -it --name books-api:development  \
  -e="APP_ENV=local" \
  -p 8888:8000 \
  -v $PWD/:/app/ \
  brpedromaia/simple-python-api:v5 --host=0.0.0.0 --port=8000 --reload
```

# Testing

## Testing from swagger:
http://localhost:8888/docs

## Testing from the command line:

### List all books
```
curl http://localhost:8888/books/
#list
```
### Get book by id
```
curl http://localhost:8888/books/<< book_id>>
```
e.g.:
```
curl http://localhost:8888/books/B0001
#{"author":"J. R. R. Tolkien","id":"B0001","publication_year":1937,"genre":"Fantasy","name":"The Hobbit"}
```

### Create new book
```
curl -X 'POST' \
  'http://localhost:8888/books/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "string",
  "name": "string",
  "author": "string",
  "publication_year": int,
  "genre": "string"
}'
```
e.g.
```
curl -X 'POST' \
  'http://localhost:8888/books/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "B0003",
  "name": "DevOps Handbook",
  "author": "Gene Kim, Jez Humble, Patrick Debois, John Willis",
  "publication_year": 2016,
  "genre": "IT"
}'
#"201 Created"
```
### Update existing book
```
curl -X 'PUT' \
  'http://localhost:8888/books/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "string",
  "name": "string",
  "author": "string",
  "publication_year": int,
  "genre": "string"
}'
```
e.g.:
```
curl -X 'PUT' \
  'http://localhost:8888/books/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "B0003",
  "name": "The DevOps Handbook",
  "author": "Gene Kim, Jez Humble, Patrick Debois, John Willis",
  "publication_year": 2016,
  "genre": "IT"
}'
#"202 Accepted"
```

## Remove book
```
curl -X 'DELETE' \
  'http://localhost:8888/books/<<book_id>>' \
  -H 'accept: application/json'
```
e.g.:
```
curl -X 'DELETE' \
  'http://localhost:8888/books/B0003' \
  -H 'accept: application/json'
#"202 Accepted"
```

## Testing from Postman collection is inside this repository
