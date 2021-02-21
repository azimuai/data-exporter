#!/usr/bin/env sh
set -o errexit -o pipefail
export DEBUG="${DEBUG:-false}"
if [ ${DEBUG} = "true" ]; then set -o xtrace; fi

case ${1} in
    app) sh  /app/iteraterepos ;;
    *) exec "$@" ;;
esac
