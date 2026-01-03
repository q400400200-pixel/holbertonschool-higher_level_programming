# Web Basics: HTTP, HTTPS, and curl

## Task 0: HTTP and HTTPS Basics

### Differences Between HTTP and HTTPS

HTTP is a protocol used to transfer data between a client and a server without encryption.
This means that the data can be intercepted or modified during transmission.

HTTPS is the secure version of HTTP. It uses SSL/TLS encryption to protect data.
Because of this, HTTPS is commonly used for websites that handle sensitive information.

### Structure of an HTTP Request and Response

#### HTTP Request
An HTTP request is sent by the client and contains:
- Method (GET, POST, etc.)
- URL or Path
- Headers
- Body (optional)

#### HTTP Response
An HTTP response is sent by the server and contains:
- Status Code
- Headers
- Body (content)

### Common HTTP Methods

- **GET**  
  Retrieves data from the server.  
  Example: Fetching a web page or API data.

- **POST**  
  Sends data to the server.  
  Example: Submitting a form.

- **PUT**  
  Updates existing data.  
  Example: Updating user information.

- **DELETE**  
  Deletes data from the server.  
  Example: Removing a resource.

### Common HTTP Status Codes

- **200 OK**  
  The request was successful.

- **301 Moved Permanently**  
  The resource has been moved to a new URL.

- **400 Bad Request**  
  The request is invalid.

- **404 Not Found**  
  The requested resource does not exist.

- **500 Internal Server Error**  
  The server encountered an error.

---

## Task 1: Consume Data from an API Using curl

### Introduction

curl is a command-line tool used to transfer data to or from a server.
It is widely used to interact with APIs and inspect HTTP requests and responses.

### Verifying curl Installation

```bash
curl --version
curl http://example.com
curl https://jsonplaceholder.typicode.com/posts
curl -I https://jsonplaceholder.typicode.com/posts
curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts
---
curl is a powerful tool for interacting with web servers and APIs.
It allows sending different HTTP requests and inspecting responses directly from the command line.
