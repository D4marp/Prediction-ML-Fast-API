#!/usr/bin/env python3
"""
Complete API Testing Script
Tests all endpoints including Login, Register, CRUD operations, and Sales Prediction
"""

import requests
import json
import time
from typing import Dict, Optional

API_BASE = "http://localhost:8000"

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    END = '\033[0m'

def print_section(title):
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    print(f"{Colors.CYAN}{title}{Colors.END}")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}\n")

def print_success(message):
    print(f"{Colors.GREEN}✅ {message}{Colors.END}")

def print_error(message):
    print(f"{Colors.RED}❌ {message}{Colors.END}")

def print_info(message):
    print(f"{Colors.YELLOW}ℹ️  {message}{Colors.END}")

def test_status():
    """Test API Status"""
    print_section("Testing API Status")
    try:
        response = requests.get(f"{API_BASE}/")
        if response.status_code == 200:
            data = response.json()
            print_success("API Status OK")
            print(f"Response: {json.dumps(data, indent=2)}")
            return True
        else:
            print_error(f"API Status Failed: {response.status_code}")
            return False
    except Exception as e:
        print_error(f"Connection Error: {str(e)}")
        return False

def test_register(username="testuser", email="test@example.com", full_name="Test User", password="password123"):
    """Test User Registration"""
    print_section(f"Testing User Registration - {username}")
    try:
        payload = {
            "username": username,
            "email": email,
            "full_name": full_name,
            "password": password
        }
        response = requests.post(f"{API_BASE}/users/", json=payload)
        
        if response.status_code in [200, 201]:
            print_success(f"User {username} registered successfully")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
            return True
        else:
            if "already exists" in response.text or response.status_code == 400:
                print_info(f"User {username} already exists (which is fine for testing)")
                return True
            print_error(f"Registration Failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_login(username="testuser", password="password123") -> Optional[str]:
    """Test User Login and get Token"""
    print_section(f"Testing User Login - {username}")
    try:
        payload = {
            "username": username,
            "password": password
        }
        response = requests.post(f"{API_BASE}/token", data=payload)
        
        if response.status_code == 200:
            data = response.json()
            token = data.get("access_token")
            print_success(f"Login successful")
            print(f"Token: {token[:50]}...")
            print(f"Response: {json.dumps(data, indent=2)}")
            return token
        else:
            print_error(f"Login Failed: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return None

def test_get_user(username="testuser"):
    """Test Get User"""
    print_section(f"Testing Get User - {username}")
    try:
        response = requests.get(f"{API_BASE}/users/{username}")
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"User {username} retrieved successfully")
            print(f"Response: {json.dumps(data, indent=2)}")
            return True
        else:
            print_error(f"Get User Failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_create_item(token: str, name="Test Product", description="A test product", price=99.99, available=True) -> Optional[str]:
    """Test Create Item"""
    print_section(f"Testing Create Item - {name}")
    try:
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        payload = {
            "name": name,
            "description": description,
            "price": price,
            "available": available
        }
        response = requests.post(f"{API_BASE}/items/", json=payload, headers=headers)
        
        if response.status_code in [200, 201]:
            data = response.json()
            item_id = data.get("id")
            print_success(f"Item '{name}' created successfully")
            print(f"Item ID: {item_id}")
            print(f"Response: {json.dumps(data, indent=2)}")
            return item_id
        else:
            print_error(f"Create Item Failed: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return None

def test_get_items():
    """Test Get All Items"""
    print_section("Testing Get All Items")
    try:
        response = requests.get(f"{API_BASE}/items/")
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Retrieved {len(data)} items")
            for idx, item in enumerate(data, 1):
                print(f"\n  Item {idx}:")
                print(f"    ID: {item.get('id')}")
                print(f"    Name: {item.get('name')}")
                print(f"    Price: {item.get('price')}")
                print(f"    Available: {item.get('available')}")
            return data
        else:
            print_error(f"Get Items Failed: {response.status_code}")
            return None
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return None

def test_update_item(token: str, item_id: str, name: Optional[str] = None, price: Optional[float] = None):
    """Test Update Item"""
    print_section(f"Testing Update Item - {item_id}")
    try:
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        payload = {}
        if name:
            payload["name"] = name
        if price:
            payload["price"] = price
        
        response = requests.patch(f"{API_BASE}/items/{item_id}", json=payload, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Item {item_id} updated successfully")
            print(f"Response: {json.dumps(data, indent=2)}")
            return True
        else:
            print_error(f"Update Item Failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_delete_item(token: str, item_id: str):
    """Test Delete Item"""
    print_section(f"Testing Delete Item - {item_id}")
    try:
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        response = requests.delete(f"{API_BASE}/items/{item_id}", headers=headers)
        
        if response.status_code in [200, 204]:
            print_success(f"Item {item_id} deleted successfully")
            if response.text:
                print(f"Response: {response.text}")
            return True
        else:
            print_error(f"Delete Item Failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def test_sales_prediction(token: str, features: list):
    """Test Sales Prediction"""
    print_section(f"Testing Sales Prediction")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post(
            f"{API_BASE}/predict-sales/",
            json=features,
            headers=headers
        )
        
        if response.status_code == 200:
            data = response.json()
            print_success(f"Sales prediction successful")
            print(f"Features: {data.get('features')}")
            print(f"Predicted Sales: {data.get('predicted_sales')}")
            print(f"Response: {json.dumps(data, indent=2)}")
            return True
        else:
            print_error(f"Sales Prediction Failed: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def main():
    print(f"{Colors.BLUE}{'*'*60}{Colors.END}")
    print(f"{Colors.CYAN}FastAPI Complete System Testing{Colors.END}")
    print(f"{Colors.BLUE}{'*'*60}{Colors.END}")
    
    results = {}
    token = None
    item_id = None
    
    # Test 1: API Status
    results['api_status'] = test_status()
    time.sleep(1)
    
    # Test 2: Register User
    results['register'] = test_register()
    time.sleep(1)
    
    # Test 3: Login
    token = test_login()
    results['login'] = token is not None
    time.sleep(1)
    
    # Test 4: Get User
    results['get_user'] = test_get_user()
    time.sleep(1)
    
    # Test 5: Create Item
    item_id = test_create_item(token, "Laptop Gaming", "High-performance gaming laptop", 15000000, True)
    results['create_item'] = item_id is not None
    time.sleep(1)
    
    # Test 6: Get Items
    items = test_get_items()
    results['get_items'] = items is not None
    time.sleep(1)
    
    # Test 7: Update Item
    if item_id:
        results['update_item'] = test_update_item(token, item_id, "Laptop Gaming Pro", 16000000)
        time.sleep(1)
    
    # Test 8: Sales Prediction
    if token:
        results['sales_prediction'] = test_sales_prediction(token, [50.0, 100.0, 25.5])
        time.sleep(1)
    
    # Test 9: Delete Item
    if item_id:
        results['delete_item'] = test_delete_item(token, item_id)
        time.sleep(1)
    
    # Summary
    print_section("Test Summary")
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    print(f"Total Tests: {total}")
    print(f"Passed: {Colors.GREEN}{passed}{Colors.END}")
    print(f"Failed: {Colors.RED}{total - passed}{Colors.END}\n")
    
    for test_name, result in results.items():
        status = f"{Colors.GREEN}✅ PASS{Colors.END}" if result else f"{Colors.RED}❌ FAIL{Colors.END}"
        print(f"  {test_name}: {status}")
    
    print(f"\n{Colors.BLUE}{'='*60}{Colors.END}")
    if passed == total:
        print_success("All tests passed! System fully integrated!")
    else:
        print_error(f"{total - passed} test(s) failed. Please check the errors above.")
    print(f"{Colors.BLUE}{'='*60}{Colors.END}\n")

if __name__ == "__main__":
    main()
