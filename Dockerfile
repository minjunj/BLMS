FROM tensorflow/tensorflow:2.13.0

WORKDIR /app
COPY . /app
# RUN pip install autochord
ENTRYPOINT ["python3", "auto-chord.py"]