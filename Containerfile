FROM python:3.8.0-alpine3.10

USER root

WORKDIR /app
COPY src/ src/
COPY --chmod=0777 bin/container-entrypoint /container-entrypoint
COPY README.md .
COPY ./setup.py .

RUN pip3 install --upgrade pip ;\
    pip3 install --no-cache-dir .

WORKDIR /app/src/

ENV APP_ENV dev
EXPOSE 8000
ENTRYPOINT ["/container-entrypoint"]
CMD ["--host=0.0.0.0", "--port=8000"]