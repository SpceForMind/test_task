### Test task API

| HTTP Method        | URI           | Result  |
| ------------- |:-------------:| :------------:|
| GET      | /api/v1.0/fib/<int:yournum>/| fibonacci numeral |
| GET      | /api/v1.0/fact/<int:yournum>/     | factorial of the numeral |
### Example 
1) Request **http://127.0.0.1:5000/api/v1.0/fib/3/** will return json

```
{

  "result": 24
  
}
```
2) Request **http://127.0.0.1:5000/api/v1.0/fact/3/** will return json

```
{

  "result": 6
  
}
```

### Run application

Flask application located in src/app.py. Run it as default python script
```
python3 app.py 
``` 

### Unit tests
Unit tests located in src/tests/unit_tests.py. Run it using follow command
```
 python3 -m unittest -v unit_tests.py
``` 

### Where the application was tested
+ Ubuntu 18.04

+ Python 3.6.7

+ Flask 1.0.2