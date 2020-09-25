FROM postgres

COPY DDL/create_pastes_table.sql /docker-entrypoint-initdb.d/001_data.sql

# necessary because postgresql sets VOLUME /var/lib/postgresql/data in its
# Dockerfile which means it will be empty every time the container starts
# if you don't persist it to the Docker host. We're using a custom
# path instead to avoid it being empty
ENV PGDATA=/data
