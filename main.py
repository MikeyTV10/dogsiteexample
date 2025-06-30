from flask import Flask

app = Flask(__name__)

CSS_STYLE = """
body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background:#f9f9f9; color:#222; margin: 2em;}
a { color: #007acc; text-decoration:none;}
a:hover { text-decoration:underline;}
header { font-size: 2.5em; font-weight: bold; margin-bottom: 0.5em; color: #d35400; }
.content { background: white; padding: 2em; border-radius: 12px; box-shadow: 0 0 10px #ccc;}
p { font-size: 1.1em; line-height: 1.6em; margin-bottom: 1em;}
code { background: #eee; padding: 2px 6px; border-radius: 4px; font-family: monospace; }
"""

@app.route('/')
def home():
    return f"""
    <html>
    <head><title>dog.example.co - What is DogWeb?</title>
    <style>{CSS_STYLE}</style>
    </head>
    <body>
    <div class="content">
      <header>Welcome to dog.example.co!</header>
      
      <p><strong>What is DogWeb?</strong></p>
      <p>
        DogWeb is a friendly, decentralized network for creating and sharing <em>DogsSites</em>.
        Unlike traditional websites, DogsSites are simple Python + CSS-powered web apps hosted on DogNet domains like <code>dog.example.co</code>.
      </p>
      
      <p><strong>What are DogSites?</strong></p>
      <p>
        DogSites are unique web experiences built with Python and styled with CSS. They live on special dog-prefixed subdomains, such as:
      </p>
      <ul>
        <li><code>dog.myapp.co</code></li>
        <li><code>dog.friendly.co</code></li>
        <li><code>dog.fun.co</code></li>
      </ul>
      
      <p>
        Each DogSite can be powered by either:
        <ul>
          <li>A GitHub repository with Python code that runs dynamically</li>
          <li>A dedicated server IP hosting your DogSite</li>
        </ul>
      </p>
      
      <p>
        The goal of DogWeb is to keep things simple, creative, and community-driven — no heavy JavaScript frameworks or complicated deployment steps. Just Python, CSS, and the joy of sharing dog-themed sites.
      </p>

      <p>
        Want to create your own DogSite? Head over to the main DogNet homepage and get started!
      </p>

      <hr>
      <p style="font-size:0.9em; color:#666;">
        &copy; 2025 DogNet Initiative
      </p>
    </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    print("dog.example.co running on http://127.0.0.1:5000")
    app.run(debug=True)
