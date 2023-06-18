from fastapi import FastAPI
from resources import rootResource
from resources import bookResource
from config import appConfig
from elasticapm.contrib.starlette import make_apm_client, ElasticAPM


def create_app():
    app = FastAPI(title = "REST API using FastAPI PostgreSQL Async EndPoints")
    app.add_middleware(ElasticAPM, client=apm)
    app.include_router(rootResource.resource)
    app.include_router(bookResource.resource)
    appConfig.init()
    return app
    

apm = make_apm_client()
app = create_app()