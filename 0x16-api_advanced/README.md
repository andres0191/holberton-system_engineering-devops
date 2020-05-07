# Create an API
## What is an API
It is a way of describing the way in which programs or websites exchange data.
The data exchange format is usually JSON or XML.
## Why do we need an API?
Offer data to applications that run on a mobile
Offer data to other developers in a more or less standard format.
Offer data to our own website / application
Consume data from other applications or websites
## API providers
Some examples of websites that provide APIS are:
Twitter: access to user data, status
Google: for example to consume a Google map
But there are many more: Facebook, YouTube, Amazon, foursquare ...
[But there are still many more:](http://www.programmableweb.com/apis/directory)
## What does REST API mean?
REST comes from, REpresentational State Transfer
It is a type of web development architecture that is fully supported by the HTTP standard.
REST consists of a list of rules that must be followed in designing the architecture of an API.
We will talk about restful web services if they comply with the REST architecture.
Restful = adjective, Rest = noun
# #How REST works
###API calls
API calls are implemented as HTTP requests, in which: 
* The URL represents the resource
```
http://www.formandome.es/api/cursos/1
```
* The method (HTTP Verbs) represents the operation:
```
GET http://www.formandome.es/api/cursos/1
```
* The HTTP status code represents the result:
```
200 OK HTTP/1.1
404 NOT FOUND HTTP/1.1
```
## Resource creation
The URL will be "open" (the resource does not yet exist and therefore does not have an id)
* The method must be POST:
```
http://eventos.com/api/eventos/3/comentarios
```
## Response to resource creation
###Possible outcomes:
* 403 (Access prohibited)
* 400 (wrong request, eg a field is missing or its value is invalid)
* 500 (Server side error when trying to create the resource, eg DB has been dropped)
* 201 (Resource created successfully)
* What URL does the newly created resource have?
* The convention in REST is to return it in the response as the value of the HTTP Location header
###Resource update
* PUT method
* According to REST orthodoxy, updating would mean changing ALL the data
* PATCH is a new standard HTTP (2010) method intended to change only certain data. Many REST programming frameworks still don't support it
* Possible outcomes
* Errors already seen with POST
* 201 (Resource created, when we pass the desired id to the server)
* 200 (Resource successfully modified)
###Delete resources
*DELETE method
*Some possible outcomes:
- 200 OK
- 404 Not found
- 500 Server error
* After executing DELETE successfully, the following GET requests to the resource URL should return 404Response to resource creation
[More Info](https://juanda.gitbooks.io/webapps/content/api/arquitectura-api-rest.html)
