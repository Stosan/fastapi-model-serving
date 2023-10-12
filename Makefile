# This is a Makefile for managing server operations

# .PHONY is used to specify non-file targets
.PHONY: activate_server run_server run

# This target activates the virtual environment
activate_server:
	source dfaenv/bin/activate

# This target runs the server
run_server:
	uvicorn src.main:app --reload

# This target runs both activate_server and run_server
run: activate_server run_server
