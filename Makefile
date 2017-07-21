.PHONY: test test-cov

TAG="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
PROJECT_PACKAGE=tic_tac_toe


test:
	@echo $(TAG)Running tests$(END)
	py.test -v --tb=short group_project

tox:
	@echo $(TAG)Running TOX$(END)
	tox
