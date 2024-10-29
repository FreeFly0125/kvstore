# Key-Value Store Service

This service implement simple key-value storage with CRD operations for data object.

## Main functionalities

Implement basic operations(Create, Read, Delete) for data as key-value object.

Used PostgreSQL as storage and ensure the multi-tenancy and is capable of handling different clients while managing secure boundaries around each tenant’s respective data.

Set optional TTL(Time-To-Live) for each data object for setting the data reliable period.

## Service APIs

### Tenant API

To ensure multi-tenancy with boundaries among tenants, some basic APIs to deal with tenant management.

- Register API - `POST /api/tenant/signup`

- Signing In API - `POST /api/tenant/signin`

After sign in, a JWT token is generated and will be used for authorization for comming requests.

### Object API

All the objects APIs are involving JWT token generated after sign in as one tenant.

- Create Data API - `POST api/object`

- Read Data API - `GET api/object/{key}`

- Delete Data API - `DELETE api/object/{key}`

- Batch Data Insert API - `POST api/batch/object`

## Run the service

Main commands are written in make script. You can run the application with command `make run`