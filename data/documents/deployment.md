# Deployment Policy

## Production Deployments

Production deployments require an approved pull request.

Services should be deployed using versioned releases.

Every production deployment must have a documented rollback procedure.

## Database Changes

Database schema changes must be reviewed before production deployment.

Application deployments that modify database connectivity must
validate their database configuration before production rollout.

## Emergency Deployments

Emergency deployments may bypass the normal deployment sequence
when necessary to mitigate an active production incident.

Emergency changes must be documented after the incident is resolved.

## Ownership

Deployment ownership depends on the service being modified.

Authentication deployments are owned by the Platform Engineering team.

Payment deployments are owned by the Payments Engineering team.

Database infrastructure changes are owned by the Infrastructure
Engineering team.