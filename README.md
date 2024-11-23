# Enhanced Firefox OS Data Exporter

An enhanced version of the Firefox OS Data Exporter with added JSON syntax highlighting and improved user interface features. This tool helps you extract and visualize data from Firefox OS IndexedDB databases with better readability and export options.

## Features

- Automatic IndexedDB database discovery
- Enhanced JSON visualization with syntax highlighting
- Easy copy and download functionality 
- Improved user interface
- Support for calendar and SMS data export
- Self-hosted HTTPS server for secure access

### Available Export Formats
- **Calendar:** Export to standard ICS files
- **SMS:** Export to commhistory-tool compatible JSON

## Based on Original Firefox OS Data Exporter

This project is based on the original Firefox OS Data Exporter repository. The original tool was developed as part of the article [Exporting the Firefox OS Offline Calendar](http://digitalimagecorp.de/flatpress/?x=entry:entry151212-222444) and serves as a general tool for exporting IndexedDB databases. Unlike Mozilla's [Storage Inspector](https://developer.mozilla.org/en-US/docs/Tools/Storage_Inspector), this script dumps databases in text format for easy copy/paste and further processing.

### Original Motivation
Firefox stores IndexedDB database contents in SQLite format, but only as *serialized* data representations. This makes it impossible to view the database directly with SQLite - the data needs to be deserialized through Firefox first, which is exactly what this tool does.

### Firefox OS Connection
Firefox OS applications store much of their user data in IndexedDB databases without providing direct application or API access (e.g., Offline Calendar data). The only way to backup or export this data is by working directly with the database files.

## New Features

### JSON Syntax Highlighting
- Color-coded syntax highlighting for better readability
- Distinct colors for different JSON elements:
  - Strings (green)
  - Numbers (blue)
  - Booleans (blue)
  - Null values (blue)
  - Object keys (dark gray)
  - Punctuation (dark gray)

### Enhanced UI Features
- Copy to clipboard functionality
- Download JSON file option
- Proper indentation and formatting
- Responsive design
- Error handling for invalid JSON
- XSS prevention

## Installation

1. Clone this repository
2. Install Python 3.x
3. Configure the server (see Configuration section)
4. Run the server:
```bash
python main.py
```

## Configuration

The server can be configured by modifying the following parameters in `main.py`:

```python
# Define the host and port
HOST = 'localhost'  # Change this to your desired host
PORT = 443         # Change this to your desired port
CERT_FILE = 'selfsigned.crt'  # Name of the SSL certificate file
KEY_FILE = 'selfsigned.key'   # Name of the SSL key file
```

### Host Configuration
- For local development: use `'localhost'`
- For network access: use your IP address or domain name
- Examples:
  ```python
  HOST = 'localhost'        # Local development
  HOST = '192.168.1.100'   # Local network
  HOST = 'example.com'     # Domain name
  ```

### Port Configuration
- Default HTTPS port is 443 (requires root/admin privileges)
- For non-privileged ports, use values above 1024
- Examples:
  ```python
  PORT = 443    # Standard HTTPS port (requires root/admin)
  PORT = 8443   # Alternative HTTPS port
  PORT = 3000   # Development port
  ```

### SSL Certificate
The server automatically generates a self-signed SSL certificate if one doesn't exist. You can:

1. Let the server generate one automatically:
   - First run will create `selfsigned.crt` and `selfsigned.key`
   - Certificate will be valid for 365 days

2. Generate manually using OpenSSL:
   ```bash
   openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
     -keyout selfsigned.key -out selfsigned.crt \
     -subj "/CN=your-domain.com"
   ```

3. Use your own certificates:
   - Place your `.crt` and `.key` files in the project directory
   - Update `CERT_FILE` and `KEY_FILE` in `main.py` to match your filenames

### Security Notes
- Self-signed certificates will show a browser warning
- For production, use properly signed certificates
- Keep your key file secure and never commit it to version control

## Usage

1. Access the tool via HTTPS at the configured host and port
2. Select the database you want to export
3. View the formatted JSON output
4. Use the copy or download buttons to export the data

## Security Features
- Self-signed SSL certificate generation
- HTTPS server implementation
- Secure data handling

## Technical Details
- Pure JavaScript implementation
- No external dependencies
- Efficient regex-based syntax highlighting
- Minimal DOM manipulation

## Extended Use Case: Retrieving Lost IndexedDB Data

A significant application of this enhanced tool has been in retrieving IndexedDB data from expired or inaccessible domains. When websites become unavailable or domains expire, their associated IndexedDB data can become trapped in the browser's storage. This tool provides a way to access and export this otherwise inaccessible data, serving as a valuable data recovery solution for situations where the original domain is no longer available.

## Contributing

Feel free to submit issues and enhancement requests.

## License

[Original License Terms Apply]

## Credits

Enhanced version built upon the original Firefox OS Data Exporter by [Original Author].