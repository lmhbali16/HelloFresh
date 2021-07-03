from fastapi import FastApi

app = FastAPI(docs_url='/api/a/docs', openapi_url='/api/a/openapi.json')


app.