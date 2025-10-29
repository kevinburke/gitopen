# Virtual environment setup
VENV := venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip
VENV_MARKER := $(VENV)/.installed

.PHONY: test typecheck install clean

# Install dependencies into venv (creates venv if needed)
install: $(VENV_MARKER)

$(VENV_MARKER): requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install --requirement requirements.txt
	touch $(VENV_MARKER)
	@echo "Dependencies installed. You can now run 'make test'."

# Run tests (with type checking first)
test: $(VENV_MARKER)
	$(PYTHON) -m mypy gitopen gitopen_test.py
	$(PYTHON) gitopen_test.py

# Run type checking only
typecheck: $(VENV_MARKER)
	$(PYTHON) -m mypy gitopen gitopen_test.py

# Clean up virtual environment
clean:
	rm -rf $(VENV)
