# 📚 TECHNICAL DOCUMENTATION
## FastAPI Complete Integration System

---

## 📋 TABLE OF CONTENTS

1. [System Architecture](#system-architecture)
2. [Installation & Setup](#installation--setup)
3. [API Endpoints Reference](#api-endpoints-reference)
4. [Database Schema](#database-schema)
5. [Authentication Flow](#authentication-flow)
6. [Frontend Implementation](#frontend-implementation)
7. [Security Implementation](#security-implementation)
8. [Error Handling](#error-handling)
9. [Performance Optimization](#performance-optimization)
10. [Deployment Guide](#deployment-guide)

---

## 🏗️ SYSTEM ARCHITECTURE

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    CLIENT LAYER                          │
│                                                           │
│  ┌──────────────────────────────────────────────────┐   │
│  │  Web Browser (HTML5 + CSS3 + JavaScript)        │   │
│  │  - Responsive UI with Tailwind CSS              │   │
│  │  - Real-time form validation                    │   │
│  │  - Token management (localStorage)              │   │
│  │  - Error handling & user feedback               │   │
│  └──────────────────────────────────────────────────┘   │
└──────────────────────┬──────────────────────────────────┘
                       │ HTTP/HTTPS
                       │
┌──────────────────────▼──────────────────────────────────┐
│                 API LAYER (FastAPI)                     │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Main Application (main.py)                     │  │
│  │  - FastAPI instance                            │  │
│  │  - Middleware setup                            │  │
│  │  - Root endpoint                               │  │
│  │  - Shutdown handling                           │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
│  ┌──────────────┬──────────────┬────────────────────┐  │
│  │ Users Router │ Items Router │ Prediction Router  │  │
│  ├──────────────┼──────────────┼────────────────────┤  │
│  │ POST /users/ │ POST /items/ │ POST /predict-    │  │
│  │ GET /users/  │ GET /items/  │     sales/        │  │
│  │              │ PATCH/DELETE │                    │  │
│  └──────────────┴──────────────┴────────────────────┘  │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Security Layer                                │  │
│  │  - JWT Token generation & validation          │  │
│  │  - Password hashing (bcrypt)                   │  │
│  │  - OAuth2 password flow                        │  │
│  │  - User authentication                         │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Middleware                                    │  │
│  │  - CORS (Cross-Origin Resource Sharing)       │  │
│  │  - Request/Response logging                    │  │
│  │  - Error handling                              │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
└──────────────────────┬──────────────────────────────────┘
                       │ SQLAlchemy ORM
                       │
┌──────────────────────▼──────────────────────────────────┐
│              DATABASE LAYER (SQLite)                    │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │  User Table                                    │  │
│  │  - username (PK)                               │  │
│  │  - email (UNIQUE)                              │  │
│  │  - full_name                                   │  │
│  │  - hashed_password                             │  │
│  │  - disabled (boolean)                          │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │  Item Table                                    │  │
│  │  - id (UUID, PK)                               │  │
│  │  - name                                        │  │
│  │  - description                                 │  │
│  │  - price (FLOAT, > 0)                          │  │
│  │  - available (boolean)                         │  │
│  └──────────────────────────────────────────────────┘  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### Component Interaction Diagram

```
Frontend (User Action)
        │
        ▼
Form Submission
        │
        ▼
JavaScript Fetch API
        │
        ▼
HTTP Request to Backend
        │
        ▼
FastAPI Router
        │
        ├──► Middleware (Logging, CORS)
        │
        ├──► Input Validation (Pydantic)
        │
        ├──► Authentication Check
        │
        ├──► CRUD Operation
        │
        └──► Database Query (SQLAlchemy)
        │
        ▼
Database Response
        │
        ▼
Format Response (JSON)
        │
        ▼
HTTP Response
        │
        ▼
Frontend JavaScript
        │
        ▼
Display Result to User
```

---

## 🚀 INSTALLATION & SETUP

### Prerequisites

```bash
# Check Python version (3.7+)
python3 --version

# Check pip
pip3 --version
```

### Step 1: Clone Repository

```bash
git clone https://github.com/CarFerPin/FastAPI.git
cd FastAPI
```

### Step 2: Create Virtual Environment

```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirement.txt
```

Dependencies:
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `sqlalchemy` - ORM
- `pydantic` - Data validation
- `pyjwt` - JWT tokens
- `passlib[bcrypt]` - Password hashing
- `python-multipart` - Form parsing
- `scikit-learn` - ML model

### Step 4: Initialize Database

```bash
python init_db.py
```

This creates:
- `app.db` SQLite database
- User table
- Item table

### Step 5: Run Server

```bash
# Development (with auto-reload)
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# Production
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Step 6: Access Application

- **Web UI**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📡 API ENDPOINTS REFERENCE

### Authentication

#### POST /token
**Authenticate user and get JWT token**

Request:
```http
POST /token HTTP/1.1
Content-Type: application/x-www-form-urlencoded

username=damar&password=password123
```

Response (200):
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

Error Response (401):
```json
{
  "detail": "Incorrect username or password"
}
```

---

### User Management

#### POST /users/
**Register new user**

Request:
```json
{
  "username": "damar",
  "email": "damar@gmail.com",
  "full_name": "Damar Galih",
  "password": "password123"
}
```

Response (201):
```json
{
  "username": "damar",
  "email": "damar@gmail.com",
  "full_name": "Damar Galih",
  "disabled": false
}
```

Validation:
- Username: required, unique
- Email: required, valid format, unique
- Password: required, min 8 chars recommended
- Full Name: optional

#### GET /users/{username}
**Get user details**

Request:
```http
GET /users/damar HTTP/1.1
```

Response (200):
```json
{
  "username": "damar",
  "email": "damar@gmail.com",
  "full_name": "Damar Galih",
  "disabled": false
}
```

Response (404):
```json
{
  "detail": "User not found"
}
```

---

### Item Management

#### POST /items/
**Create new item**

Request:
```json
{
  "name": "Laptop Gaming ASUS ROG",
  "description": "High-performance gaming laptop",
  "price": 25000000,
  "available": true
}
```

Response (201):
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Laptop Gaming ASUS ROG",
  "description": "High-performance gaming laptop",
  "price": 25000000,
  "available": true
}
```

Validation:
- Name: required, max 100 chars
- Description: optional, max 500 chars
- Price: required, must be > 0
- Available: required, boolean

#### GET /items/
**Get all items**

Request:
```http
GET /items/ HTTP/1.1
```

Response (200):
```json
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "Laptop Gaming ASUS ROG",
    "description": "High-performance gaming laptop",
    "price": 25000000,
    "available": true
  },
  {
    "id": "550e8400-e29b-41d4-a716-446655440001",
    "name": "Monitor 4K",
    "description": "27-inch 4K monitor",
    "price": 5000000,
    "available": true
  }
]
```

Pagination (optional):
```http
GET /items/?skip=0&limit=10
```

#### PATCH /items/{item_id}
**Update item**

Request:
```json
{
  "name": "Laptop Gaming ASUS ROG Upgraded",
  "price": 26000000
}
```

Response (200):
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Laptop Gaming ASUS ROG Upgraded",
  "description": "High-performance gaming laptop",
  "price": 26000000,
  "available": true
}
```

Note: Only update fields provided, others unchanged

#### DELETE /items/{item_id}
**Delete item**

Request:
```http
DELETE /items/550e8400-e29b-41d4-a716-446655440000 HTTP/1.1
```

Response (204):
```
No Content
```

Response (404):
```json
{
  "detail": "Item not found"
}
```

---

### Sales Prediction

#### POST /predict-sales/
**Predict sales using ML model**

**Requires authentication!**

Request:
```http
POST /predict-sales/ HTTP/1.1
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

[50.0, 100.0, 25.5]
```

Response (200):
```json
{
  "features": [50.0, 100.0, 25.5],
  "predicted_sales": 241.5
}
```

Features:
- Array of numbers
- Can represent: marketing spend, reach, days, etc.
- Used by trained Linear Regression model

Response (401):
```json
{
  "detail": "Not authenticated"
}
```

---

## 🗄️ DATABASE SCHEMA

### User Table

```sql
CREATE TABLE "user" (
    username VARCHAR NOT NULL PRIMARY KEY,
    email VARCHAR NOT NULL UNIQUE,
    full_name VARCHAR,
    hashed_password VARCHAR NOT NULL,
    disabled BOOLEAN DEFAULT false
);
```

**Columns:**
- `username` (VARCHAR): Primary key, unique identifier
- `email` (VARCHAR): User email, must be unique
- `full_name` (VARCHAR): Optional full name
- `hashed_password` (VARCHAR): Bcrypt hashed password
- `disabled` (BOOLEAN): Account status (false = active)

**Indexes:**
```sql
CREATE INDEX ix_user_email ON user(email);
```

**Sample Data:**
```sql
INSERT INTO "user" VALUES (
    'damar',
    'damar@gmail.com',
    'Damar Galih',
    '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lm',
    0
);
```

### Item Table

```sql
CREATE TABLE item (
    id CHAR(36) NOT NULL PRIMARY KEY,
    name VARCHAR NOT NULL,
    description VARCHAR,
    price FLOAT NOT NULL,
    available BOOLEAN NOT NULL
);
```

**Columns:**
- `id` (CHAR(36)): UUID primary key
- `name` (VARCHAR): Item name
- `description` (VARCHAR): Item description (optional)
- `price` (FLOAT): Item price (must be > 0)
- `available` (BOOLEAN): Availability status

**Indexes:**
```sql
CREATE INDEX ix_item_name ON item(name);
CREATE INDEX ix_item_available ON item(available);
```

**Sample Data:**
```sql
INSERT INTO item VALUES (
    '550e8400-e29b-41d4-a716-446655440000',
    'Laptop Gaming ASUS ROG',
    'High-performance gaming laptop',
    25000000,
    1
);
```

---

## 🔐 AUTHENTICATION FLOW

### JWT Token Flow

```
┌─────────────────────────────────────────────────────────────┐
│                   USER LOGIN FLOW                            │
└─────────────────────────────────────────────────────────────┘

1. User enters username & password in UI
   │
   ▼
2. JavaScript fetch POST /token
   │
   ▼
3. FastAPI receives request
   │
   ├──► Validate input format
   │
   ├──► Query database for user
   │
   └──► If user not found → return 401
   │
   ▼
4. Verify password
   │
   ├──► Hash provided password with same salt
   │
   └──► Compare with stored hashed_password
        │
        └──► If mismatch → return 401
   │
   ▼
5. Generate JWT Token
   │
   ├──► Create payload: {sub: username, exp: expiry_time}
   │
   ├──► Sign with secret key using HS256
   │
   └──► Encode to string
   │
   ▼
6. Return token to client
   │
   ▼
7. JavaScript stores token in localStorage
   │
   ▼
8. For authenticated requests, send:
   Authorization: Bearer {token}
```

### JWT Token Structure

```
Header.Payload.Signature

Example Token:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJzdWIiOiJkYW1hciIsImV4cCI6MTcwMzAwMDAwMH0.
abcdef123456...

Decoded:

Header (base64url):
{
  "alg": "HS256",
  "typ": "JWT"
}

Payload (base64url):
{
  "sub": "damar",         // subject (username)
  "exp": 1703000000,      // expiration time
  "iat": 1702996400       // issued at time
}

Signature (HS256):
HMACSHA256(
  base64UrlEncode(header) + "." + base64UrlEncode(payload),
  secret_key
)
```

### Password Hashing

```
User Registration:

1. User provides: password = "password123"
   │
   ▼
2. Generate random salt (16 bytes)
   │
   ▼
3. Hash password with bcrypt:
   hashed = bcrypt.hashpw(password, salt)
   │
   Result: $2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3...
           (includes salt + hash)
   │
   ▼
4. Store only hashed_password in database

Login Verification:

1. User provides: password = "password123"
   │
   ▼
2. Retrieve hashed_password from database
   │
   ▼
3. Use bcrypt to verify:
   bcrypt.checkpw(password, hashed_password)
   │
   Result: True or False
   │
   ▼
4. If True → generate token, if False → 401
```

---

## 🎨 FRONTEND IMPLEMENTATION

### File Structure

```
/app/static/
├── index.html          # Main HTML with embedded CSS & JS
├── styles/            # (Optional) CSS files
└── js/               # (Optional) JavaScript files
```

### HTML Structure

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Application</title>
    <link href="https://cdn.tailwindcss.com" rel="stylesheet">
</head>
<body>
    <!-- Navigation -->
    <!-- Hero Section -->
    <!-- Features Grid -->
    <!-- Main Content Grid -->
    
    <!-- Forms & Components -->
    <div class="container">
        <!-- Register Form -->
        <!-- Login Form -->
        <!-- User Management -->
        <!-- Item CRUD -->
        <!-- Sales Prediction -->
    </div>
    
    <script>
        // JavaScript API integration
    </script>
</body>
</html>
```

### JavaScript API Integration

```javascript
const API_BASE = 'http://localhost:8000';
let currentToken = localStorage.getItem('access_token');

// Register User
async function registerUser(data) {
    const response = await fetch(`${API_BASE}/users/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    return await response.json();
}

// Login
async function login(username, password) {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    
    const response = await fetch(`${API_BASE}/token`, {
        method: 'POST',
        body: formData
    });
    const data = await response.json();
    
    if (response.ok) {
        currentToken = data.access_token;
        localStorage.setItem('access_token', currentToken);
    }
    return data;
}

// Create Item
async function createItem(itemData) {
    const response = await fetch(`${API_BASE}/items/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(itemData)
    });
    return await response.json();
}

// Get Items
async function getItems() {
    const response = await fetch(`${API_BASE}/items/`);
    return await response.json();
}

// Update Item
async function updateItem(itemId, updates) {
    const response = await fetch(`${API_BASE}/items/${itemId}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(updates)
    });
    return await response.json();
}

// Delete Item
async function deleteItem(itemId) {
    const response = await fetch(`${API_BASE}/items/${itemId}`, {
        method: 'DELETE',
        headers: { 'Authorization': `Bearer ${currentToken}` }
    });
    return response.status === 204;
}

// Predict Sales (requires token)
async function predictSales(features) {
    const response = await fetch(`${API_BASE}/predict-sales/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${currentToken}`
        },
        body: JSON.stringify(features)
    });
    return await response.json();
}
```

### Form Validation

```javascript
// Client-side validation
function validateEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
}

function validatePassword(password) {
    return password.length >= 8;
}

function validatePrice(price) {
    return parseFloat(price) > 0;
}

// Display error messages
function showError(element, message) {
    element.innerHTML = `<div class="text-red-500">${message}</div>`;
}

function showSuccess(element, message) {
    element.innerHTML = `<div class="text-green-500">${message}</div>`;
}
```

---

## 🔒 SECURITY IMPLEMENTATION

### Password Hashing with Bcrypt

```python
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__rounds=12
)

# Hash password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verify password
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
```

### JWT Token Management

```python
from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "your-secret-key"  # Change in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            return None
        return username
    except JWTError:
        return None
```

### Input Validation with Pydantic

```python
from pydantic import BaseModel, Field, EmailStr, validator

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr  # Automatic email validation
    full_name: Optional[str] = None
    password: str = Field(..., min_length=8)
    
    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v

class ItemCreate(BaseModel):
    name: str = Field(..., max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(..., gt=0)  # Must be > 0
    available: bool
```

### CORS Configuration

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Error Handling

```python
from fastapi import HTTPException, status

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

# Usage
if not user:
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )
```

---

## ⚠️ ERROR HANDLING

### Common HTTP Status Codes

```
200 OK - Request succeeded
201 Created - Resource created
204 No Content - Request succeeded, no content
400 Bad Request - Invalid input
401 Unauthorized - Authentication failed
403 Forbidden - Permission denied
404 Not Found - Resource not found
422 Unprocessable Entity - Validation error
500 Internal Server Error - Server error
```

### Error Response Format

```json
{
  "detail": "User not found"
}
```

### Exception Handling Example

```python
@router.post("/users/")
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        # Check if user exists
        existing_user = db.query(User).filter(User.username == user.username).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )
        
        # Create new user
        hashed_password = hash_password(user.password)
        db_user = User(
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            hashed_password=hashed_password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
        
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
```

---

## ⚡ PERFORMANCE OPTIMIZATION

### Database Query Optimization

```python
# ❌ Bad - N+1 query problem
for item in db.query(Item).all():
    print(item.user)  # Each iteration queries database

# ✅ Good - Use eager loading
from sqlalchemy.orm import joinedload
db.query(Item).options(joinedload(Item.user)).all()
```

### Caching Tokens

```javascript
// Store token in localStorage
localStorage.setItem('access_token', token);

// Retrieve for authenticated requests
const token = localStorage.getItem('access_token');
const headers = {
    'Authorization': `Bearer ${token}`
};
```

### Connection Pooling

```python
from sqlalchemy import create_engine

engine = create_engine(
    'sqlite:///./app.db',
    connect_args={"check_same_thread": False},
    pool_size=10,
    max_overflow=20
)
```

### Response Compression

FastAPI automatically handles response compression. Enable in production:

```python
from fastapi.middleware import gzip

app.add_middleware(gzip.GZIPMiddleware, minimum_size=1000)
```

---

## 🚀 DEPLOYMENT GUIDE

### Development to Production Checklist

- [ ] Update SECRET_KEY to secure value
- [ ] Set DEBUG = False
- [ ] Configure CORS for production domains
- [ ] Use environment variables for secrets
- [ ] Switch from SQLite to PostgreSQL
- [ ] Add database backups
- [ ] Enable HTTPS/SSL
- [ ] Set up monitoring
- [ ] Configure logging
- [ ] Add rate limiting
- [ ] Set up CI/CD pipeline
- [ ] Test error scenarios
- [ ] Load testing

### Docker Deployment

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Environment Variables

```bash
# .env file
SECRET_KEY=your-secure-secret-key
DATABASE_URL=postgresql://user:password@localhost/dbname
ENVIRONMENT=production
DEBUG=false
```

### Production Server Configuration

```bash
# Using Gunicorn + Uvicorn
gunicorn app.main:app \
    --workers 4 \
    --worker-class uvicorn.workers.UvicornWorker \
    --bind 0.0.0.0:8000 \
    --access-logfile - \
    --error-logfile -
```

---

## 📈 MONITORING & LOGGING

### Application Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

@app.post("/token")
async def login(form_data):
    logger.info(f"Login attempt: {form_data.username}")
    # ...
```

### Health Check Endpoint

```python
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
```

### Performance Metrics

```python
from time import time

@app.middleware("http")
async def add_process_time_header(request, call_next):
    start_time = time()
    response = await call_next(request)
    process_time = time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response
```

---

**End of Technical Documentation**
