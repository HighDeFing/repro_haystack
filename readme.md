## To execute

Create a venv:
1. `python3 -m venv env`
2. `source env/bin/activate`

Install haystack and requirements in env by:

```bash
pip install -r -requirements.txt
```

or/and

```bash
pip install farm-haystack numb unidecode pandas farm-haystack[ocr]
```

### Elastic search docker

We need docker for this.

```bash
docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.13.0
docker run --name es01-test --net elastic -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.13.0
```

For the rest of the executions:

```bash
docker start es01-test -a
```

### Upload the files

Execute the python file:
`repoducible_haystack/env/bin/python3 haystack_upload_files.py`

### Do the test

Execute the python file:
`repoducible_haystack/env/bin/python3 haystack_test.py`
