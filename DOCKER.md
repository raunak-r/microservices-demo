```
/microservices-demo/serviceregistry$ sudo docker build -t msdemo/serviceregistry .
/microservices-demo/serviceregistry$ sudo docker run --network=host msdemo/serviceregistry
```

```aidl
/microservices-demo/py_django_backend$ sudo docker build -t msdemo/pydjango .
/microservices-demo/py_django_backend$ sudo docker run --network=host msdemo/pydjango
```