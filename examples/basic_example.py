#!/usr/bin/env python3
"""
Simple test to verify basic template functionality.
"""

from trim_template.trim import TrimTemplate

# Simple test with basic variables
template_vars = {
    'page_title': 'Test Page',
    'site_name': 'TestApp',
    'main_heading': 'Hello World',
    'content': 'This is a test.',
    'current_year': 2025,
    'user': type('User', (), {'logged_in': False})(),
    'users': [],
}

def basic_example():
    tmpl = TrimTemplate('examples/main.html.trim', vars=template_vars, pretty=True)
    output = tmpl.render()
    print("=== Basic Example Output ===\n")
    print(output)

if __name__ == '__main__':
    basic_example()