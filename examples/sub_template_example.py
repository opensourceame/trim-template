#!/usr/bin/env python3
"""
Example demonstrating sub-template usage with TrimTemplate.
This shows how to include multiple sub-templates in a main template.
"""

from trim_template.trim import TrimTemplate
from datetime import datetime

# Simple class to represent a user object
class User:
    def __init__(self, id, name, email, role, avatar_url, is_admin=False):
        self.id = id
        self.name = name
        self.email = email
        self.role = role
        self.avatar_url = avatar_url
        self.is_admin = is_admin

# Simple class to represent the current user
class CurrentUser:
    def __init__(self, logged_in=True, name="", email=""):
        self.logged_in = logged_in
        self.name = name
        self.email = email

# Sample data for the template
template_vars = {
    'page_title': 'User Dashboard',
    'site_name': 'MyAwesomeApp',
    'main_heading': 'Welcome to the Dashboard',
    'content': 'This page demonstrates sub-template usage with header, user cards, and footer.',
    'current_year': datetime.now().year,
    'user': CurrentUser(
        logged_in=True,
        name='John Doe',
        email='john@example.com'
    ),
    'users': [
        User(
            id=1,
            name='Alice Johnson',
            email='alice@example.com',
            role='Admin',
            avatar_url='/avatars/alice.jpg',
            is_admin=True
        ),
        User(
            id=2,
            name='Bob Smith',
            email='bob@example.com',
            role='User',
            avatar_url='/avatars/bob.jpg',
            is_admin=False
        ),
        User(
            id=3,
            name='Carol Davis',
            email='carol@example.com',
            role='Moderator',
            avatar_url='/avatars/carol.jpg',
            is_admin=True
        )
    ]
}

def main():
    # Create template instance with pretty formatting
    tmpl = TrimTemplate('examples/main.html.trim', vars=template_vars, pretty=True)

    # Render the template
    output = tmpl.render()

    print("=== Sub-Template Example Output ===\n")
    print(output)

    print("\n=== Template Debug Info ===")
    tmpl.debug()

if __name__ == '__main__':
    main()