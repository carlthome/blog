install:
	python -m venv .venv
	.venv/bin/pip install -r requirements.txt

freeze:
	pip freeze -r requirements.txt > requirements.txt

clean:
	rm -r .venv

build:
	python src/download_nltk.py
	cd src && python download_gists.py

	#find posts -name "*.ipynb" | parallel 'jupyter nbconvert --to notebook --ExecutePreprocessor.timeout=-1 --execute {}'

	cd src && nikola build
	rm -r docs/
	mv src/output/ docs/
