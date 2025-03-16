# Exercise 1: YAML Configuration File

## Problem

You are working on a project that requires you to define a YAML file for a complex application. The application has the following configuration:

- application name: myapp
- version: 1.0
- author: your name
- description: a complex yaml exercise
- environment settings:
  - development:
    - host: localhost
    - port: 3000
    - database:
      - type: mysql
      - host: localhost
      - port: 3306
      - username: dev_user
      - schema name: development_schema
      - logging configuration:
        - log file: /var/log/dev.log
        - log level: debug
      - modules:
        - name: module 1
          - enabled: true
          - priority: 1
        - name: module 2
          - enabled: false
          - priority: 2
  - production:
    - host: production.example.com
    - port: 80
    - database:
      - type: postgresql
      - host: db.example.com
      - port: 5432
      - username: prod_user
      - schema name: production_schema
      - logging configuration:
        - log file: /var/log/prod.log
        - log level: info
      - modules:
        - name: module 1
          - enabled: true
          - priority: 1
        - name: module 2
          - enabled: true
          - priority: 2

Your task is to create a YAML configuration file named `config.yml`, and transform the configuration above into valid YAML syntax.

### Additional requirements

- `modules` should be represented as a sequence of maps not a map of maps!
- You should use `"` where appropriate
- Use your best judgement to determine the most appropriate data types to use. Obviously every value can be a string, but that's not the point of this exercise.
