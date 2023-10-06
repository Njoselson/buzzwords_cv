
tests:
	python -m unittest test_buzzwords

cv: 
	python generate_cv.py --file_name $(file_name)
	open $(file_name)

cover_letter: 
	python generate_cover_letter.py --file_name $(file_name)
	open $(file_name)

clean:
	find . -type f -name "*.sw[klmnop]" -delete
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete
	# find  . -type d -iname  '*__pycache__*' | xargs rm -rf
	
lint:
	black ./
