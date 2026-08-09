# Database Infrastructure

## Overview

Aurelius Systems primarily uses PostgreSQL for transactional data.

Authentication data is stored in the authentication database.

Payment transactions are stored in the payments database.

## Backups

Database backups are performed every six hours.

## Schema Changes

Database schema changes must be reviewed before production deployment.

Schema changes must be compatible with the application version
being deployed.

## Ownership

The database infrastructure is managed by the Infrastructure
Engineering team.

## Availability

Applications that depend on PostgreSQL may experience failures
when the database is unavailable or when an application uses an
incompatible database configuration.