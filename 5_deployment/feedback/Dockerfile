FROM svizor/zoomcamp-model:3.11.5-slim
LABEL authors="oluse"

RUN pip install pipenv gunicorn

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]
#copy dependency files from local system

RUN pipenv install --system --deploy

COPY ["predictor.py", "load_model.py", "./"]
#copy dependency files from local system
EXPOSE 9685
#
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9685", "predictor:app"]

#ENTRYPOINT ["top", "-b"]