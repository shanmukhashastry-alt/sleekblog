# Save all the files to the working directory for download
import os

# Create the main HTML file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

# Create the CSS file
with open('styles.css', 'w', encoding='utf-8') as f:
    f.write(css_content)

# Create the JavaScript file
with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

# Create the README file
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(setup_instructions)

# Create the package.json file
with open('package.json', 'w', encoding='utf-8') as f:
    f.write(package_json)

# Create a simple .gitignore file
gitignore_content = '''# Dependencies
node_modules/

# Build outputs
dist/
build/

# Environment variables
.env
.env.local

# OS generated files
.DS_Store
Thumbs.db

# Editor files
.vscode/
.idea/
*.swp
*.swo

# Logs
*.log
npm-debug.log*
'''

with open('.gitignore', 'w', encoding='utf-8') as f:
    f.write(gitignore_content)

print("✅ All files have been created successfully!")
print("\\n📁 Files created:")
files_created = ['index.html', 'styles.css', 'script.js', 'README.md', 'package.json', '.gitignore']
for file in files_created:
    if os.path.exists(file):
        size = os.path.getsize(file)
        print(f"  • {file} ({size} bytes)")

print("\\n🚀 Your sleek blog website is ready!")
print("\\n📋 Next steps:")
print("1. Download all the files")
print("2. Open index.html in a web browser")
print("3. Customize the content to match your needs")
print("4. Deploy to your preferred hosting platform")