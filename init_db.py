#!/usr/bin/env python3
"""
Initialize Database Script
Creates all tables in the database
"""

import sys
import os

# Add app to path
sys.path.insert(0, os.path.dirname(__file__))

from app.database.dbhandler import Base, engine
from app.database.sqlmodels import User, Item

def init_db():
    """Initialize database - create all tables"""
    print("🔄 Creating database tables...")
    
    try:
        # Create all tables defined in Base
        Base.metadata.create_all(bind=engine)
        print("✅ Database initialized successfully!")
        print("✅ Tables created:")
        print("   - User table")
        print("   - Item table")
        return True
    except Exception as e:
        print(f"❌ Error initializing database: {str(e)}")
        return False

if __name__ == "__main__":
    init_db()
