docker run --rm \
	--volume ${GIT_REPOS}:/app/repos/ \
	--env AZIMU_API_HOST=${} \
	--env AZIMU_API_TOKEN=${}\
	azimuai/data-exporter:latest
