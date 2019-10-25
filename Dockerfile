FROM python:3.7.4-alpine3.9 AS build

COPY requirements.txt .
RUN pip3 install --user -r requirements.txt

# Create image and copy requirements from build image. Also, install only
# essential packages for running the app. It reduces the image size 
# from 113 to 105 Mb. Original size is 98.5MB.
FROM python:3.7.4-alpine3.9 

WORKDIR /blogEA
COPY --from=build /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copy application files at the end of building process for cache improvement
COPY ./*.py ./
EXPOSE 5000

#ENTRYPOINT ["/usr/local/bin/python", "blog_api.py"]
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "blog_api:api"]
