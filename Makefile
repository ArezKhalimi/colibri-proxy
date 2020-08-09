# default arguments
HTTP_PORT=8080

# build and run Docker
build-docker:
	docker-compose build --force-rm
run-docker:
	docker-compose up
# Local build
build:
	cp .myenv.example src/.myenv && \
	pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements/dev.txt
# Local-run
run:
	cd src/ && \
	gunicorn server:app -b :$(HTTP_PORT) \
	--worker-class aiohttp.GunicornWebWorker --reload --access-logfile -
