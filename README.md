# UwinRent

## Requirements
* <MAIN>/server Requirements
* <MAIN>/client Requirements
* Caddyserver2 

## How to run - dev

1. Follow <MAIN>/server startup steps

2. Follow <MAIN>/client startup steps

3. in `<MAIN>` run `sudo caddy start`
   now at https://localhost:80 the app is running


## Sequence diagram 

steps that the server undertakes when getting a request from a browser

1. browser sends GET / to server

2. server proxies GET / to client

3. client returns files associated with GET /

4. server returns files to browser

5. browser creates graphql connection with server

6. graphql connection between browser and server is persistent

after the persistent connection is established the client is not needed until further files are requested.

Step 1 through 4 are repeated if te browser requests additional files

steps 5 and 6 repeat every time a connection is established or reconnect occurs

![Alt text](/images/BaseCodeStructure.jpg)
