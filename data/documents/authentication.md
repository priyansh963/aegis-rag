# Authentication Service

## Overview

The Authentication Service is responsible for user login,
token generation, session validation, and password reset.

The service is accessed through the API Gateway.

## Dependencies

The Authentication Service uses PostgreSQL to store user
account metadata.

Redis is used for temporary session and token-related data.

The Authentication Service depends on the PostgreSQL database
being available for normal login operations.

## Ownership

The Authentication Service is owned by the Platform Engineering team.

## Operational Behavior

If the Authentication Service is unavailable, users may be
unable to log in or reset their passwords even when other
application services remain healthy.

## Deployment

Authentication releases are versioned using semantic-style
service versions such as `auth-service-v2.4.0`.

Production deployments require an approved pull request and
must have a rollback procedure.