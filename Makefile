clean:
	rm -rf data/raw/*
	touch -f data/raw/.gitkeep
	rm raw_files.txt

raw_files.txt:
	python src/download_data.py
	touch raw_files.txt
