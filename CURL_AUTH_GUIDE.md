# CURL Authentication Guide

## Method 1: Using Cookie Jar (Recommended)

### Step 1: Login and Save Cookies
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/api/auth/login/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -c cookies.txt \
  -d '{
    "email": "your-email@example.com",
    "password": "your-password"
  }'
```

The `-c cookies.txt` flag saves all cookies (including sessionid and csrftoken) to a file.

### Step 2: Use Saved Cookies for Authenticated Requests
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/products/' \
  -H 'accept: application/json' \
  -b cookies.txt
```

The `-b cookies.txt` flag sends the saved cookies with your request.

### Complete Example (Login + Get Products)
```bash
# Login and save cookies
curl -X 'POST' \
  'http://127.0.0.1:8000/api/auth/login/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -c cookies.txt \
  -d '{
    "email": "user@example.com",
    "password": "password123"
  }'

# Use cookies to access protected endpoint
curl -X 'GET' \
  'http://127.0.0.1:8000/api/products/' \
  -H 'accept: application/json' \
  -b cookies.txt
```

---

## Method 2: Copy Cookies from Browser

### Step 1: Login via Browser
1. Open your browser and navigate to `http://127.0.0.1:8000/api/schema/swagger-ui/`
2. Login using the Swagger UI or make a login request
3. Open Developer Tools (F12)
4. Go to **Application** tab (Chrome) or **Storage** tab (Firefox)
5. Click on **Cookies** → `http://127.0.0.1:8000`
6. Find the `sessionid` cookie and copy its value

### Step 2: Use Cookie in CURL
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/products/' \
  -H 'accept: application/json' \
  -H 'Cookie: sessionid=YOUR_SESSIONID_VALUE_HERE'
```

### Complete Example
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/products/' \
  -H 'accept: application/json' \
  -H 'Cookie: sessionid=abc123def456ghi789'
```

---

## Method 3: Using Token Authentication (If Available)

If token authentication is set up, you can use:

```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/products/' \
  -H 'accept: application/json' \
  -H 'Authorization: Token YOUR_TOKEN_HERE'
```

---

## Notes

- **Cookie Jar Method** is the easiest and most reliable for curl
- **Browser Method** is useful for quick testing
- Cookies expire when the session expires
- Make sure your server is running on `http://127.0.0.1:8000`

## Troubleshooting

If you get a 403 Forbidden error, you might need to include the CSRF token:
```bash
# First, get CSRF token
curl -c cookies.txt -b cookies.txt \
  'http://127.0.0.1:8000/api/auth/login/' \
  -X POST \
  -H 'Content-Type: application/json' \
  -d '{"email": "user@example.com", "password": "password123"}'
```

