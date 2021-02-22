# Practical tasks for 6th lab

## Dynamic programming


## Run tests

```shell
python3 -m unittest -v
```

## Test coverage

1. install coverage module
```shell
pip3 install coverage
```

2. run test with coverage
```shell
coverage run -m unittest -v
```

3. generate simple report
```shell
coverage report -m
```

4. generate rich html report and open it
```shell
coverage html
open htmlcov/index.html
```

5. cleanup
```shell
coverage erase 
rm -rf htmlcov/
```