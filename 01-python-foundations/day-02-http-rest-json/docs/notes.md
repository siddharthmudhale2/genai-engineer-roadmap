# 🌐 Day 02 - HTTP, REST APIs & JSON
>
> **Phase:** Python Foundations

---

# 🌐 1. What is HTTP?

---

## 📖 Definition

**HTTP (HyperText Transfer Protocol)** is the communication protocol that allows a client (browser, mobile app, Python script, etc.) to communicate with a server over the internet.

HTTP defines **how requests are sent** and **how responses are returned**.

---

## 🎓 Interview Definition

HTTP is a **stateless application-layer protocol** used for communication between distributed systems over the World Wide Web.

---

## ❓ Why Do We Need HTTP?

Imagine opening:

https://www.google.com

How does your browser ask Google's server for the webpage?

It sends an **HTTP Request**.

Google processes the request and sends back an **HTTP Response**.

Without HTTP:

- Websites cannot load.
- APIs cannot communicate.
- Mobile applications cannot fetch data.
- AI models cannot receive prompts.

---

## ⚙️ How HTTP Works

```
Client

↓

HTTP Request

↓

Internet

↓

Server

↓

HTTP Response

↓

Client
```

---

## 🌍 Real-World Analogy

Imagine ordering food.

You

↓

Tell waiter your order

↓

Kitchen prepares food

↓

Waiter brings food

Mapping:

You → Client

Waiter → HTTP

Kitchen → Server

Food → Response

---

## 🏢 Industry Usage

HTTP is used everywhere.

Examples:

- ChatGPT
- Google
- GitHub
- Netflix
- Amazon
- Flipkart
- Instagram
- LinkedIn
- Gmail
- WhatsApp Web

Every API communication happens through HTTP or HTTPS.

---

## 🤖 GenAI Connection

When you call the OpenAI API:

```python
client.responses.create(...)
```

Behind the scenes:

```
Your Python Code

↓

HTTP POST Request

↓

OpenAI Server

↓

AI Response

↓

JSON

↓

Python Object
```

Every prompt you send to ChatGPT through an API travels over HTTP.

---

## 💡 Key Points

- HTTP is a protocol.
- Client starts communication.
- Server responds.
- Stateless protocol.

---

## ⚠ Common Mistakes

❌ HTTP is a programming language.

✅ HTTP is a communication protocol.

---

## 📘 Revision Notes

✔ HTTP = Communication Protocol

✔ Client sends Request

✔ Server sends Response

---

# 🌍 2. Client & Server

---

## 📖 What is a Client?

A **Client** is any software or device that requests data or services from another computer.

Examples:

- Browser
- Mobile App
- Python Program
- Postman
- React App

---

## 🎓 Interview Definition

A client is an application that initiates communication with a server by sending requests.

---

## Example

```python
import requests

requests.get(...)
```

Your Python script becomes the client.

---

## 📖 What is a Server?

A **Server** is a computer or software application that receives requests, processes them, and returns responses.

---

Examples

- GitHub Server
- OpenAI Server
- Google Server
- FastAPI Application
- Flask Application

---

## Workflow

```
Python Script

↓

Client

↓

Internet

↓

Server

↓

Response

↓

Client
```

---

## Client vs Server

| Client | Server |
|---------|---------|
| Sends Request | Receives Request |
| Receives Response | Sends Response |
| Browser | Web Server |
| Mobile App | API Server |
| Python Script | FastAPI |

---

## 🌍 Real Example

Instagram

You open Instagram.

↓

Instagram App sends request.

↓

Instagram Server processes request.

↓

Server returns your feed.

---

## 📘 Revision

Client asks.

Server answers.

---

# 📩 3. Request & Response

---

## 📖 What is a Request?

A request is a message sent by a client asking the server to perform an action.

---

A request contains:

- URL
- HTTP Method
- Headers
- Body (optional)

---

Example

```
GET /users
```

---

## 📖 What is a Response?

A response is the message returned by the server after processing the request.

A response contains:

- Status Code
- Headers
- Body

---

Example

```json
{
    "name":"Siddharth"
}
```

---

## Workflow

```
Browser

↓

Request

↓

Server

↓

Response

↓

Browser
```

---

## Interview Question

What is the difference between Request and Response?

Answer:

A request is sent by the client.

A response is returned by the server.

---

# 🌐 4. HTTP Methods

---

HTTP Methods specify **what action** the client wants to perform.

---

## GET

### Definition

Retrieve existing data.

---

### Example

Open GitHub Profile

```
GET /users/octocat
```

---

### Characteristics

- Safe
- Read only
- Does not modify data

---

## POST

### Definition

Create new data.

---

Examples

- Register User

- Login

- Send ChatGPT Prompt

- Upload Image

---

Example

```
POST /users
```

---

## PUT

### Definition

Replace an existing resource completely.

---

Example

Replace user profile.

---

## PATCH

### Definition

Update only specific fields.

---

Example

Change only email address.

---

## DELETE

### Definition

Remove existing data.

---

Example

Delete account.

---

## Comparison Table

| Method | Action | Example |
|----------|----------|----------|
| GET | Read | View Profile |
| POST | Create | Register |
| PUT | Replace | Replace Profile |
| PATCH | Update | Update Email |
| DELETE | Delete | Delete Account |

---

## Real Example

ChatGPT

You type:

"Explain HTTP"

↓

Client sends

POST Request

↓

OpenAI

↓

Returns Response

---

## 📘 Revision

GET

Read

POST

Create

PUT

Replace

PATCH

Update

DELETE

Remove

---

# 🚦 5. HTTP Status Codes

---

## 📖 Definition

Status Codes indicate whether the request succeeded or failed.

---

## Categories

| Code | Meaning |
|------|----------|
| 1xx | Informational |
| 2xx | Success |
| 3xx | Redirect |
| 4xx | Client Error |
| 5xx | Server Error |

---

### Important Status Codes

200 OK

Request successful.

---

201 Created

New resource created.

---

204 No Content

Success with no response body.

---

400 Bad Request

Invalid request.

---

401 Unauthorized

Authentication required.

---

403 Forbidden

Permission denied.

---

404 Not Found

Requested resource not found.

---

500 Internal Server Error

Server-side problem.

---

502 Bad Gateway

Gateway received an invalid response from an upstream server.

---

503 Service Unavailable

Server temporarily unavailable.

---

## Interview Question

Difference between 401 and 403?

401

Authentication required.

403

Authenticated but not allowed.

---

## 📘 Revision

200

Success

404

Not Found

500

Server Error

---

# 🏷 6. HTTP Headers

---

## Definition

Headers provide additional information about the request or response.

---

Examples

```
Content-Type

Authorization

User-Agent

Accept
```

---

### Content-Type

Specifies data format.

Example

```
Content-Type: application/json
```

---

### Authorization

Contains API Key or Token.

Example

```
Authorization: Bearer sk-xxxxxxxx
```

---

### User-Agent

Identifies the client application.

---

## Why Headers Matter?

Without headers,

the server may not know:

- Who you are
- What format you're sending
- What format you expect back

---

# 📦 7. What is JSON?

---

## 📖 Definition

JSON (**JavaScript Object Notation**) is a lightweight text format used for exchanging structured data between systems.

---

## 🎓 Interview Definition

JSON is a language-independent data interchange format consisting of key-value pairs and arrays.

---

## Why JSON?

Because:

- Easy to read.
- Easy to write.
- Lightweight.
- Supported everywhere.

---

Example

```json
{
    "name":"Siddharth",
    "role":"Generative AI Engineer",
    "skills":[
        "Python",
        "FastAPI",
        "GenAI"
    ]
}
```

---

## JSON Data Types

- String
- Number
- Boolean
- Object
- Array
- Null

---

# 🐍 8. Python Dictionary vs JSON

Python

```python
person = {
    "name":"Siddharth",
    "age":24
}
```

JSON

```json
{
    "name":"Siddharth",
    "age":24
}
```

Difference

Python Dictionary

↓

Python Object

JSON

↓

String Representation

---

# 🌐 9. What is REST API?

---

## 📖 Definition

A REST API (Representational State Transfer API) is an API that follows REST architectural principles and communicates over HTTP.

---

## Simple Definition

A REST API allows two applications to communicate using HTTP methods such as GET, POST, PUT, PATCH, and DELETE.

---

## Real Examples

GitHub API

OpenAI API

Gemini API

Spotify API

Weather API

Stripe API

---

# REST Principles

- Client-Server Architecture
- Stateless Communication
- Uniform Interface
- Resource-Based URLs
- Cacheable Responses

---

# 🤖 GenAI Connection

Every modern LLM API is a REST API.

Examples

OpenAI

Gemini

Anthropic

Mistral

Groq

Hugging Face

All use:

- HTTPS
- JSON
- Authorization Header
- POST Requests

---

# 🏭 Industry Usage

Every AI Engineer works with:

HTTP

↓

REST APIs

↓

JSON

↓

Authentication

↓

API Keys

↓

LLMs

Master these concepts before using any AI SDK.

---

# ⚠ Common Mistakes

❌ Confusing HTTP with HTTPS.

❌ Thinking GET modifies data.

❌ Sending API keys in URLs.

❌ Ignoring status codes.

❌ Assuming every response is successful.

---

# 💡 Best Practices

✅ Always check status codes.

✅ Use HTTPS whenever possible.

✅ Validate JSON responses.

✅ Never hardcode API keys.

✅ Handle API errors gracefully.

---

# 💼 Interview Questions

1. What is HTTP?

2. Explain Client-Server Architecture.

3. Difference between GET and POST?

4. Difference between PUT and PATCH?

5. Explain REST API.

6. What is JSON?

7. Why is HTTP stateless?

8. What is a 404 error?

9. Difference between 401 and 403?

10. What are HTTP Headers?

---

# 🚀 One-Page Revision

✅ HTTP → Communication Protocol

✅ Client → Sends Request

✅ Server → Sends Response

✅ Request → URL + Method + Headers + Body

✅ Response → Status + Headers + Body

✅ GET → Read

✅ POST → Create

✅ PUT → Replace

✅ PATCH → Update

✅ DELETE → Remove

✅ 200 → OK

✅ 404 → Not Found

✅ 500 → Server Error

✅ JSON → Data Exchange Format

✅ REST API → HTTP-based API

---
