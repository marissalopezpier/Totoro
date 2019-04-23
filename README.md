# Totoro
respository
14-open access

## Mile per gallon Calculator and Gas Budget

Most people do not take the time to calculate the price it is to travel to and from work, since it takes up valuable time in the day. Here we have a program that does that for you, ```bash mileage.py ```. The only simple thing you have to do is remember your mileage spent and your gas input for that mileage.

This program takes two positional arguments ```bash miles``` and ``` bash gallons```. It also takes one optional argument ```bash -d|--date```. All of these inputs are positive integers greater than zero. Any questions please contact Marissa Lopez Pier, email: mal1@email.arizona.edu .

## Expected Behavior

```bash
[mal1@login2 14-open]$ ./mileage.py
usage: mileage.py [-h] [-d Date] MILES GALLONS
mileage.py: error: the following arguments are required: MILES, GALLONS

[mal1@login2 14-open]$ ./mileage.py -h
usage: mileage.py [-h] [-d Date] MILES GALLONS

Mileage per Gallon

positional arguments:
  MILES                 miles of trip
  GALLONS               gallons per car tank

optional arguments:
  -h, --help            show this help message and exit
  -d Date, --date Date  Record Date as YYMMDD (default: 190422)

[mal1@login2 14-open]$ ./mileage.py 0 0
Miles and gallons must be greater than zero

[mal1@login2 14-open]$ ./mileage.py 10 10 -d 190424
Old Average MPG: None
New MPG added: 1.0
New Average MPG: 1.0

[mal1@login2 14-open]$ ./mileage.py 10 25 -d
usage: mileage.py [-h] [-d Date] MILES GALLONS
mileage.py: error: argument -d/--date: expected one argument

[mal1@login2 14-open]$ ./mileage.py 10 25 -d 19424555
Date must have month, day, and year specified ordered(yearmonthday:i.e. 190422):
[mal1@login2 14-open]$


```



## Test Suite

A passing test suite looks like this:
```bash
[mal1@login2 14-open]$ make test
python3 -m pytest -v test.py
======================================================== test session starts =========================================================
platform linux -- Python 3.7.1, pytest-4.0.2, py-1.7.0, pluggy-0.8.0 -- /rsgrps/bh_class/conda/bin/python3
cachedir: .pytest_cache
rootdir: /rsgrps/bh_class/mal1/biosys-analytics/assignments/14-open, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.1, doctestplus-0.2.0, arraydiff-0.3
collected 6 items

test.py::test_usage PASSED                                                                                                     [ 16%]
test.py::test_badinputs1 PASSED                                                                                                [ 33%]
test.py::test_badinputs2 PASSED                                                                                                [ 50%]
test.py::test_badinputs3 PASSED                                                                                                [ 66%]
test.py::test_badinputs4 PASSED                                                                                                [ 83%]
test.py::test_one PASSED                                                                                                       [100%]

====================================================== 6 passed in 1.40 seconds ======================================================
```


## License
[MIT](https://choosealicense.com/licenses/mit/)
