docker run --rm \
	--volume ${GIT_REPOS}:/app/repos/ \
	--env AZIMU_API_HOST=https://2fc72d777afb.ngrok.io \
	--env AZIMU_API_TOKEN=tyfuygiluhoijpkwqefqwef \
	azimuai/data-exporter:latest
