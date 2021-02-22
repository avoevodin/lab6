# Practical tasks for 6th lab

## Dynamic programming


## Run tests

```shell
python3 -m unittest -v
```

## Test coverage

1. run test with coverage
```shell
coverage run -m unittest -v
```

2. generate simple report
```shell
coverage report -m
```

3. generate rich html report and open it
```shell
coverage html
open htmlcov/index.html
```

4. cleanup
```shell
coverage erase 
rm -rf htmlcov/
```