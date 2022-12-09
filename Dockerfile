FROM python:3.9
WORKDIR /projTST
COPY requirements.txt /projTST/requirements.txt
RUN pip install -r requirements.txt
COPY . /projTST
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]