FROM python:3.7.4-alpine3.9 AS build

# RUN apk update \
#     && apk add postgresql-client libffi-dev gcc musl-dev postgresql-dev
WORKDIR /blogEA
COPY requirements.txt .
RUN pip3 install --user -r requirements.txt

COPY ./*.py ./

# Create image and copy requirements from build image. Also, install only
# essential packages for running the app. It reduces the image size 
# from 319 to 165 Mb
FROM python:3.7.4-alpine3.9 

WORKDIR /blogEA
COPY --from=build /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy application files at the end of building process for cache improvement
COPY ./*.py ./
EXPOSE 5000

ENTRYPOINT ["/usr/local/bin/python", "blog_api.py"]