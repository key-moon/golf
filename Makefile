.PHONY: dist submission.zip

dist:
	rm -rf dist
	mkdir -p dist
	python generator.py
	rm -rf dist/__pycache__

submission.zip: dist
	zip -j -r submission.zip dist

check_base:
	python checker.py base_code
check_dist:
	python checker.py dist 
# solve:
# 	OPENAI_API_KEY=$(cat ~/.openai_api_key) python solver.py 
