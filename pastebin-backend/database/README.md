# Database

running postgres docker for database:

```bash
docker run -p 5432:5432 --name pastebin-postgres -e POSTGRES_PASSWORD=postgres -d postgres
```

instructions for setting up db:

1. execute DDL scripts to create tables.
2. execute DML scripts to insert rows.
