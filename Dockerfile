FROM python
WORKDIR /hello
COPY . /hello
CMD ["python3","hello.py"]
