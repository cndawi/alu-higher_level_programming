# SQL - Introduction

## Description
This project introduces the fundamentals of relational databases and Structured Query Language (SQL) using MySQL. It covers basic database operations such as listing, creating, and deleting databases, as well as querying and manipulating data.

## Requirements
* **OS:** Ubuntu 20.04 LTS
* **Database:** MySQL 8.0
* All SQL queries must have a comment just before them.
* All SQL keywords must be in uppercase (`SELECT`, `SHOW`, `CREATE`, `DROP`, etc.).
* All files must end with a new line.

## Files

| File | Description |
| :--- | :--- |
| `0-list_databases.sql` | Lists all databases of a MySQL server. |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` in a MySQL server if it does not already exist. |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` in a MySQL server if it exists. |

## Usage
Execute any script against your local MySQL server using the following command:
```bash
cat <filename.sql> | mysql -hlocalhost -uroot -p
```

