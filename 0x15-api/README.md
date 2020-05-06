HTTP Methods
REST APIs enable you to develop any kind of web application having all possible CRUD (create, retrieve, update, delete) operations. REST guidelines suggest using a specific HTTP method on a specific type of call made to the server (though technically it is possible to violate this guideline, yet it is highly discouraged).

Use below-given information to find a suitable HTTP method for the action performed by API.

Table of Contents

HTTP GET
HTTP POST
HTTP PUT
HTTP DELETE
HTTP PATCH
Summary
Glossary

HTTP GET
Use GET requests to retrieve resource representation/information only  and not to modify it in any way. As GET requests do not change the state of the resource, these are said to be safe methods. Additionally, GET APIs should be idempotent, which means that making multiple identical requests must produce the same result every time until another API (POST or PUT) has changed the state of the resource on the server.

If the Request-URI refers to a data-producing process, it is the produced data which shall be returned as the entity in the response and not the source text of the process, unless that text happens to be the output of the process.

For any given HTTP GET API, if the resource is found on the server, then it must return HTTP response code 200 (OK)  along with the response body, which is usually either XML or JSON content (due to their platform-independent nature).

In case resource is NOT found on server then it must return HTTP response code 404 (NOT FOUND). Similarly, if it is determined that GET request itself is not correctly formed then server will return HTTP response code 400 (BAD REQUEST).

Example request URIs
HTTP GET http://www.appdomain.com/users
HTTP GET http://www.appdomain.com/users?size=20&page=5
HTTP GET http://www.appdomain.com/users/123
HTTP GET http://www.appdomain.com/users/123/address

HTTP POST
Use POST APIs to create new subordinate resources, e.g., a file is subordinate to a directory containing it or a row is subordinate to a database table. Talking strictly in terms of REST, POST methods are used to create a new resource into the collection of resources.

Ideally, if a resource has been created on the origin server, the response SHOULD be HTTP response code 201 (Created) and contain an entity which describes the status of the request and refers to the new resource, and a Location header.

Many times, the action performed by the POST method might not result in a resource that can be identified by a URI. In this case, either HTTP response code 200 (OK) or 204 (No Content) is the appropriate response status.

Responses to this method are not cacheable, unless the response includes appropriate Cache-Control or Expires header fields.

Please note that POST is neither safe nor idempotent, and invoking two identical POST requests will result in two different resources containing the same information (except resource ids).

Example request URIs
HTTP POST http://www.appdomain.com/users
HTTP POST http://www.appdomain.com/users/123/accounts

HTTP PUT
Use PUT APIs primarily to update existing resource (if the resource does not exist, then API may decide to create a new resource or not). If a new resource has been created by the PUT API, the origin server MUST inform the user agent via the HTTP response code 201 (Created) response and if an existing resource is modified, either the 200 (OK) or 204 (No Content) response codes SHOULD be sent to indicate successful completion of the request.

If the request passes through a cache and the Request-URI identifies one or more currently cached entities, those entries SHOULD be treated as stale. Responses to this method are not cacheable.

The difference between the POST and PUT APIs can be observed in request URIs. POST requests are made on resource collections, whereas PUT requests are made on an individual resource.
Example request URIs
HTTP PUT http://www.appdomain.com/users/123
HTTP PUT http://www.appdomain.com/users/123/accounts/456

HTTP DELETE
As the name applies, DELETE APIs are used to delete resources (identified by the Request-URI).

A successful response of DELETE requests SHOULD be HTTP response code 200 (OK) if the response includes an entity describing the status, 202 (Accepted) if the action has been queued, or 204 (No Content) if the action has been performed but the response does not include an entity.

DELETE operations are idempotent. If you DELETE a resource, its removed from the collection of resources. Repeatedly calling DELETE API on that resource will not change the outcome  however, calling DELETE on a resource a second time will return a 404 (NOT FOUND) since it was already removed. Some may argue that it makes the DELETE method non-idempotent. Its a matter of discussion and personal opinion.

If the request passes through a cache and the Request-URI identifies one or more currently cached entities, those entries SHOULD be treated as stale. Responses to this method are not cacheable.

Example request URIs
HTTP DELETE http://www.appdomain.com/users/123
HTTP DELETE http://www.appdomain.com/users/123/accounts/456

HTTP PATCH
HTTP PATCH requests are to make partial update on a resource. If you see PUT requests also modify a resource entity so to make more clear  PATCH method is the correct choice for partially updating an existing resource and PUT should only be used if youre replacing a resource in its entirety.

Please note that there are some challenges if you decide to use PATCH APIs in your application:

Support for PATCH in browsers, servers, and web application frameworks is not universal. IE8, PHP, Tomcat, Django, and lots of other software has missing or broken support for it.
Request payload of PATCH request is not straightforward as it is for PUT request. e.g.
HTTP GET /users/1

produces below response:

{id: 1, username: 'admin', email: 'email@example.org'}

A sample patch request to update the email will be like this:

HTTP PATCH /users/1

[
{ op: replace, path: /email, value: new.email@example.org }
]
There may be following possible operations are per the HTTP specification.

[
{ "op": "test", "path": "/a/b/c", "value": "foo" },
{ "op": "remove", "path": "/a/b/c" },
{ "op": "add", "path": "/a/b/c", "value": [ "foo", "bar" ] },
{ "op": "replace", "path": "/a/b/c", "value": 42 },
{ "op": "move", "from": "/a/b/c", "path": "/a/b/d" },
{ "op": "copy", "from": "/a/b/d", "path": "/a/b/e" }
]

PATCH method is not a replacement for the POST or PUT methods. It applies a delta (diff) rather than replacing the entire resource.


Summary of HTTP Methods for RESTful APIs
The below table summarises the use of HTTP methods discussed above.

HTTP METHOD CRUD    ENTIRE COLLECTION (E.G. /USERS) SPECIFIC ITEM (E.G. /USERS/123)
POST    Create  201 (Created), Location header with link to /users/{id} containing new ID.  Avoid using POST on single resource
GET Read    200 (OK), list of users. Use pagination, sorting and filtering to navigate big lists.   200 (OK), single user. 404 (Not Found), if ID not found or invalid.
PUT Update/Replace  405 (Method not allowed), unless you want to update every resource in the entire collection of resource.    200 (OK) or 204 (No Content). Use 404 (Not Found), if ID not found or invalid.
PATCH   Partial Update/Modify   405 (Method not allowed), unless you want to modify the collection itself.  200 (OK) or 204 (No Content). Use 404 (Not Found), if ID not found or invalid.
DELETE  Delete  405 (Method not allowed), unless you want to delete the whole collection  use with caution. 200 (OK). 404 (Not Found), if ID not found or invalid.

Glossary
Safe Methods
As per HTTP specification, the GET and HEAD methods should be used only for retrieval of resource representations  and they do not update/delete the resource on the server. Both methods are said to be considered safe.

This allows user agents to represent other methods, such as POST, PUT and DELETE, in a special way, so that the user is made aware of the fact that a possibly unsafe action is being requested  and they can update/delete the resource on server and so should be used carefully.

Idempotent Methods
The term idempotent is used more comprehensively to describe an operation that will produce the same results if executed once or multiple times. Idempotence is a handy property in many situations, as it means that an operation can be repeated or retried as often as necessary without causing unintended effects. With non-idempotent operations, the algorithm may have to keep track of whether the operation was already performed or not.

In HTTP specification, The methods GET, HEAD, PUT and DELETE are declared idempotent methods. Other methods OPTIONS and TRACE SHOULD NOT have side effects, so both are also inherently idempotent.

References: https://restfulapi.net/http-methods/
