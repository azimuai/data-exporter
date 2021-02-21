FROM python:3.7-alpine

RUN apk add --no-cache git jq curl
ENV APP_USER="app" \
    APP_USER_SHELL="/sbin/nologin" \
    APP_USER_UID="1000"
ENV APP_HOME="/${APP_USER}"

ENV DEPENDENCIES="gettext"

ENV PATH="${PATH}:${APP_HOME}/.local/bin"

RUN apk add build-base
RUN apk add --no-cache ${DEPENDENCIES} && \
    adduser -h ${APP_HOME} -s ${APP_USER_SHELL} -u ${APP_USER_UID} -D ${APP_USER} && \
    ln -s ${APP_HOME}/docker-entrypoint.sh /docker-entrypoint.sh


WORKDIR ${APP_HOME}
USER ${APP_USER}

COPY --chown=${APP_USER}:${APP_USER} . ${APP_HOME}/

RUN mkdir ${APP_HOME}/repos
ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["app"]
