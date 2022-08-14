import subprocess

subprocess.call(['poetry', 'add', '-D', 'pytest', 'pytest-cov', 'pytest-asyncio', 'pyright', 'black', 'flake8=4.0.1', 'isort', 'poethepoet', 'pyproject-flake8', 'notebook'])
subprocess.call(['poetry', 'install'])
