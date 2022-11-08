FROM python:3.10.8-slim
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y gcc g++ tesseract-ocr
ENV PYTHONPATH "${PYTHONPATH}:/app"
COPY ./requirements.txt /app/requirements.txt
COPY . /app
RUN pip install -r requirements.txt
RUN cd PassportEye && python setup.py install && cd ..
RUN mkdir -p uploaded_images
EXPOSE 8000
CMD ["python", "app.py"]
