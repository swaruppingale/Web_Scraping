# HTTP Protocol Basics

HTTP (Hypertext Transfer Protocol) is the foundational communication protocol
used by clients (browsers, scripts) to interact with web servers.

## Request–Response Model
HTTP follows a stateless request–response model:
- A client sends an HTTP request
- The server returns an HTTP response
- Each request is independent of previous requests

## Common HTTP Methods
- GET: Retrieve data from a server
- POST: Submit data to a server
- PUT / PATCH: Update resources
- DELETE: Remove resources

## HTTP Headers
Headers carry metadata about the request or response:
- User-Agent: Identifies the client
- Accept / Accept-Language: Preferred response format
- Cookies: Maintain session state

## HTTP Status Codes
- 2xx: Success (200 OK)
- 3xx: Redirection
- 4xx: Client errors (403 Forbidden, 404 Not Found)
- 5xx: Server errors

## Relevance to Web Scraping
Understanding HTTP is essential to:
- Mimic browser behavior
- Interpret access restrictions
- Handle rate limiting and errors
