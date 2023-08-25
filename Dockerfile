FROM python:3.7
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
# ENTRYPOINT ["python3", "-m", "application", "app.py"]
ENTRYPOINT ["python3", "app.py"]