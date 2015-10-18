.PHONY: env all dev install

LPYTHON=python3
PYTHON=$(LPYTHON)/bin/$(LPYTHON)

all:

env:
	virtualenv  $(LPYTHON)

dev:	env
	$(PYTHON) setup.py develop

dev:	install
	$(PYTHON) setup.py install
