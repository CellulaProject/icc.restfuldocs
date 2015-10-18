.PHONY: env dev install

LPYTHON=python3
PYTHON=$(LPYTHON)/bin/$(LPYTHON)

env:
	[ -d $(LPYTHON) ] || virtualenv  $(LPYTHON)

dev:	env
	$(PYTHON) setup.py develop

install: env
	$(PYTHON) setup.py install
