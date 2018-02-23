
CP=cp
RM=rm
ECHO=echo
PYTEST=pytest

test: clean
	@$(ECHO) "Executing test cases"
	@$(PYTEST) --cov-report html --benchmark-disable --cov .

bench: clean
	@$(ECHO) "Executing test cases with benchmarking"
	@$(PYTEST) --cov-report html --benchmark-histogram --benchmark-columns='min, max, mean, median' --cov .

.PHONY: clean

clean:
	@$(RM) -rf __pycache__
	@$(RM) -rf *.pyc
	@$(RM) -rf .cache
	@$(RM) -rf .coverage
	@$(RM) -rf htmlcov
	@$(RM) -rf benchmark*.svg
	@$(RM) -rf .benchmarks
