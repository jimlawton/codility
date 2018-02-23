# codility
Codility solutions.

Thanks to https://github.com/timhourigan for the test framework stuff!

# First Time Setup

$ pipenv shell

# Run Tests

* $ cd lessons/01/1_bingap
* $ make         (same as make test)
* $ make bench   (run benchmark as well)

This will execute the unit tests (pyTest), run code coverage and execute the benchmark unit tests. 
The benchmark tests can be a little slow as they do multiple iterations and it is best to turn 
them off during early development.

## Outputs

* On screen code coverage, benchmark and unit test results
* benchmark_XXXX_XXXX.svg - Plot of benchmark performance - Mixed usage and sensitive to the test order.
* htmlcov - Code coverage report

All can be turned on/off by the Makefile.

The benchmark output could be changed to JSON I think and plotted elsewhere.

# pyTest

http://pytest-benchmark.readthedocs.io/en/latest/usage.html

# Big O

* https://wiki.python.org/moin/TimeComplexity
* https://nikhilgopal.com/code%20optimization/python/2012/04/24/a-refresher-on-big-o-notation-python.html

# Lessons

* https://app.codility.com/programmers/lessons/1-iterations/
