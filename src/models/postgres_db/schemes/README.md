## Run Alembic Migrations

### Configuration

```bash
cp alembic.ini.example alembic.ini
```

```bash
alembic init alembic
```

```bash
alembic revision --autogenerate -m "Initial Commit"
```

- Update the `alembic.ini` with your database credentials (`sqlalchemy.url`)

### (Optional) Create a new migration

```bash
alembic revision --autogenerate -m "Add ..."
```

### Upgrade the database

```bash
alembic upgrade head
```