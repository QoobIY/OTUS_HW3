# WSGI FRAMEWORK

This is WSGI framework similar to django, but much simplified

## Requirements

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [parse](https://pypi.org/project/parse/).

```bash
pip install parse
```


## Usage
To start the server write in bash console
```bash
python3 main.py <PORT>
```
This is how server start with port 8082
```bash
python3 main.py 8082
>>Serving on port 8082...
>>192.168.1.1 - - [20/May/2019 12:33:34] "GET / HTTP/1.1" 200 510
>>192.168.1.1 - - [20/May/2019 12:33:34] "GET /favicon.ico HTTP/1.1" 200 30
...
192.168.101.127 - - [20/May/2019 12:34:04] "GET /hello HTTP/1.1" 200 330
192.168.101.127 - - [20/May/2019 12:34:04] "GET /favicon.ico HTTP/1.1" 200 30
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.