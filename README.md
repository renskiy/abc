# abc

## Installation and run
```bash
./manage.py migrate
./manage.py runserver
```

### docker
```bash
docker build -t abc .
docker run --rm -ti -v `pwd`:/data -p 8000:8000 abc
```

## API

Go to http://localhost:8000
