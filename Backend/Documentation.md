# Crud

__Stack__ : Python with Flask-restful

Very simple Layered architecture with 4 layers

- Presentation -> resources
- Logic -> controller
- Database -> repository
- Domain -> model

## Presentation layer

It is the routes, endpoints using the flask api

## Logic layer

The logic involving working with the data.
Serving the requests generated by end user.

## Database layer

An in memory repository for storing the data

## Domain layer

Programing components.