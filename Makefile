build:
	python -m build

upload: build
	twine upload dist/*
