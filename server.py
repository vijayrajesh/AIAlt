#!/usr/bin/env python3
"""
Simple HTTP Server with CORS support for the SEO Alt Text Generator
Run this script to serve the index.html file without CORS issues
"""

import http.server
import socketserver
import os
from urllib.parse import urlparse, parse_qs, unquote
import requests

PORT = 8000

class CORSRequestHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP Request Handler with CORS support and proxy endpoints"""
    
    def end_headers(self):
        """Add CORS headers to all responses"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def do_OPTIONS(self):
        """Handle preflight requests"""
        self.send_response(200)
        self.end_headers()
    
    def do_GET(self):
        """Handle GET requests with proxy support"""
        parsed_path = urlparse(self.path)
        
        # Proxy endpoint for fetching HTML content
        if parsed_path.path == '/proxy/html':
            self.handle_proxy_html(parsed_path)
        # Proxy endpoint for fetching images
        elif parsed_path.path == '/proxy/image':
            self.handle_proxy_image(parsed_path)
        else:
            # Serve static files normally
            super().do_GET()
    
    def handle_proxy_html(self, parsed_path):
        """Proxy endpoint to fetch HTML content from external URLs"""
        try:
            params = parse_qs(parsed_path.query)
            if 'url' not in params:
                self.send_error(400, 'Missing url parameter')
                return
            
            target_url = unquote(params['url'][0])
            
            # Fetch the URL
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(target_url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # Send response
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(response.content)
            
        except requests.RequestException as e:
            self.send_error(500, f'Failed to fetch URL: {str(e)}')
        except Exception as e:
            self.send_error(500, f'Server error: {str(e)}')
    
    def handle_proxy_image(self, parsed_path):
        """Proxy endpoint to fetch images from external URLs"""
        try:
            params = parse_qs(parsed_path.query)
            if 'url' not in params:
                self.send_error(400, 'Missing url parameter')
                return
            
            target_url = unquote(params['url'][0])
            
            # Fetch the image
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(target_url, headers=headers, timeout=10, stream=True)
            response.raise_for_status()
            
            # Send response
            self.send_response(200)
            content_type = response.headers.get('Content-Type', 'image/jpeg')
            self.send_header('Content-Type', content_type)
            self.end_headers()
            
            # Stream the image data
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    self.wfile.write(chunk)
            
        except requests.RequestException as e:
            self.send_error(500, f'Failed to fetch image: {str(e)}')
        except Exception as e:
            self.send_error(500, f'Server error: {str(e)}')
    
    def log_message(self, format, *args):
        """Custom log format"""
        print(f"[{self.log_date_time_string()}] {format % args}")


def main():
    """Start the HTTP server"""
    # Change to the script's directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
        print("=" * 60)
        print("🚀 SEO Alt Text Generator Server")
        print("=" * 60)
        print(f"📡 Server running at: http://localhost:{PORT}")
        print(f"📂 Serving files from: {os.getcwd()}")
        print("\n💡 Open your browser and navigate to:")
        print(f"   http://localhost:{PORT}/index.html")
        print("\n⚙️  Proxy endpoints available:")
        print(f"   - /proxy/html?url=<URL>  (Fetch HTML content)")
        print(f"   - /proxy/image?url=<URL> (Fetch images)")
        print("\n🛑 Press Ctrl+C to stop the server")
        print("=" * 60)
        print()
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped. Goodbye!")


if __name__ == "__main__":
    main()
