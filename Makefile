.PHONY: env dev install test edit

LPYTHON=python3
PYTHON=$(PWD)/$(LPYTHON)/bin/$(LPYTHON)
ROOT=$(PWD)

test:	
	ip a | grep 2001
	ip a | grep 172.
	. $(LPYTHON)/bin/activate
	cd src && $(PYTHON) app.py

env:
	[ -d $(LPYTHON) ] || virtualenv  $(LPYTHON)

dev:	env
	$(PYTHON) setup.py develop

install: env
	$(PYTHON) setup.py install
	
edit:	
	cd src && emacs app.py
