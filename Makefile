.PHONY: test
test: pep8
	python runtests.py

.PHONY: pep8
pep8:
	@flake8 * --ignore=F403,F401,E501,F811,F841 --exclude=requirements.txt,*.pyc,*.md,Makefile,LICENSE,*.in
