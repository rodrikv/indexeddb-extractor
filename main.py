import os
import subprocess
import http.server
import ssl

HOST = 'example.com'
PORT = 443
CERT_FILE = 'selfsigned.crt'
KEY_FILE = 'selfsigned.key'


def generate_self_signed_cert():
    """Generate a self-signed SSL certificate."""
    print("Generating self-signed SSL certificate...")
    try:
        subprocess.run([
            "openssl", "req", "-x509", "-nodes", "-days", "365",
            "-newkey", "rsa:2048", "-keyout", KEY_FILE, "-out", CERT_FILE,
            "-subj", "/CN=localhost"
        ], check=True)
        print("Self-signed SSL certificate generated successfully.")
    except subprocess.CalledProcessError:
        print("Failed to generate self-signed SSL certificate. Exiting.")
        exit(1)


class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom HTTP request handler to serve ffosexporter.html."""

    def do_GET(self):
        if self.path == '/':
            self.path = 'ffosexporter.html'
        return super().do_GET()


def setup_https_server():
    """Set up the HTTPS server using the self-signed SSL certificate."""
    server_address = (HOST, PORT)
    httpd = http.server.HTTPServer(server_address, CustomHTTPRequestHandler)

    httpd.socket = ssl.wrap_socket(
        httpd.socket,
        keyfile=KEY_FILE,
        certfile=CERT_FILE,
        server_side=True
    )

    print(f"Serving on https://{HOST}:{PORT}")
    httpd.serve_forever()


def main():
    """Main function to execute the setup."""
    if not os.path.exists(CERT_FILE) or not os.path.exists(KEY_FILE):
        generate_self_signed_cert()

    setup_https_server()


if __name__ == "__main__":
    main()