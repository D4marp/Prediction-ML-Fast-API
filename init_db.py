#!/usr/bin/env python3
"""
Initialize Database Script
Creates all tables in the database and seeds demo users
"""

import sys
import os

# Add app to path
sys.path.insert(0, os.path.dirname(__file__))

from app.database.dbhandler import Base, engine, SessionLocal
from app.database.sqlmodels import User, Item
from app.crud.users import create_user
from app.database.models import UserCreate

def init_db():
    """Initialize database - create all tables and seed demo data"""
    print("🔄 Creating database tables...")
    
    try:
        # Create all tables defined in Base
        Base.metadata.create_all(bind=engine)
        print("✅ Database initialized successfully!")
        print("✅ Tables created:")
        print("   - User table")
        print("   - Item table")
        
        # Seed demo users
        db = SessionLocal()
        try:
            # Check if demo users already exist
            demo_users = [
                UserCreate(
                    username="john_doe",
                    email="john@example.com",
                    full_name="John Doe",
                    password="SecurePass123"
                ),
                UserCreate(
                    username="jane_smith",
                    email="jane@example.com",
                    full_name="Jane Smith",
                    password="MyPassword456"
                ),
                UserCreate(
                    username="admin",
                    email="admin@example.com",
                    full_name="Administrator",
                    password="AdminPass789"
                )
            ]
            
            for user_data in demo_users:
                existing_user = db.query(User).filter(User.username == user_data.username).first()
                if not existing_user:
                    create_user(db, user_data)
                    print(f"   ✅ Created demo user: {user_data.username}")
                else:
                    print(f"   ℹ️  User already exists: {user_data.username}")
            
            print("\n📝 Demo Credentials:")
            print("   1. john_doe / SecurePass123")
            print("   2. jane_smith / MyPassword456")
            print("   3. admin / AdminPass789")
            
        finally:
            db.close()
        
        return True
    except Exception as e:
        print(f"❌ Error initializing database: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    init_db()
