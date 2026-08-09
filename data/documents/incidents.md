# Incident INC-2026-1042

## Incident Metadata

Date: 2026-07-18

Service: Authentication Service

Severity: SEV-1

Status: Resolved

## Summary

The Authentication Service experienced elevated error rates
following deployment version `auth-service-v2.4.1`.

Users experienced failures when attempting to log in or reset
their passwords.

## Root Cause

The deployment introduced an incompatible database connection
configuration.

The Authentication Service was therefore unable to establish
connections with PostgreSQL.

## Impact

The incident affected:

- User login
- Password reset operations

Other application services that did not depend on the
Authentication Service remained operational.

## Resolution

The incident was resolved by rolling back
`auth-service-v2.4.1` to `auth-service-v2.4.0`.

## Ownership

The incident was primarily owned by the Platform Engineering team.

## Follow-up

Future authentication deployments should validate database
connection configuration before production rollout.

A rollback procedure must be available for every production release.