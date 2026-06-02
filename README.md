# ENCS3310 File Sharing Server

A simple, bilingual (English/Arabic) file sharing web server built with Python sockets.

## Project Overview

This project implements a basic HTTP web server in Python that serves HTML pages, CSS stylesheets, images, and files. It includes full support for both English and Arabic languages with proper right-to-left (RTL) text direction.

## Features

- **Bilingual Support**: Full English and Arabic interface
- **HTTP Server**: Built from scratch using Python sockets
- **File Serving**: Serves HTML pages, images, stylesheets, and downloadable files
- **Responsive Design**: Mobile-friendly CSS styling
- **Student Information Table**: Displays student details with ID card images
- **File Downloads**: Users can download files from the server
- **Language Switcher**: Easy navigation between English and Arabic versions

## Project Structure

```
Task3/
├── server.py                 # Python HTTP server (main application)
├── README.md                # Project documentation (this file)
├── html/
│   ├── home_en.html        # English homepage
│   └── home_ar.html        # Arabic homepage
├── css/
│   └── styles.css          # Stylesheet for both pages
├── imgs/                    # Image files directory
│   ├── mariam_id_card.jpg
│   ├── ramz_id_card.jpg
│   └── ruba_id_card.jpg
└── files/                   # Downloadable files directory
    ├── file1.txt
    ├── file2.txt
    └── file3.html
```

## Technical Specifications

### Server Details

- **Host**: localhost (127.0.0.1)
- **Port**: 6663
- **Protocol**: HTTP/1.1
- **Language**: Python 3

### Routing

| Route                                      | File Served                            |
| ------------------------------------------ | -------------------------------------- |
| `/`, `/index.html`, `/home_en.html`, `/en` | `html/home_en.html`                    |
| `/ar`, `/home_ar.html`                     | `html/home_ar.html`                    |
| `/imgs/*`                                  | Images from `imgs/` directory          |
| `/css/*`                                   | Stylesheets from `css/` directory      |
| `/files/*`                                 | Files from `files/` directory          |
| Other paths                                | Serves as file downloads from `files/` |

## How to Run

### Prerequisites

- Python 3.x installed

### Starting the Server

1. Open a terminal in the project directory
2. Run the server:
   ```bash
   python server.py
   ```
3. You should see:
   ```
   The server is running on http://localhost:6663
   ```

### Accessing the Server

Open your web browser and navigate to:

- **English Version**: `http://localhost:6663/` or `http://localhost:6663/en`
- **Arabic Version**: `http://localhost:6663/ar`

## Features Breakdown

### HTML Pages

- **Bilingual Content**: Both English and Arabic versions available
- **Student Information**: Table displaying student names, IDs, departments, completed credit hours, and ID card images
- **File Download Links**: Users can download files directly from the page
- **Language Switcher**: Quick links to switch between languages

### Styling

The CSS stylesheet provides:

- **Modern Design**: Gradient background with purple theme
- **Responsive Layout**: Adapts to mobile and desktop devices
- **RTL Support**: Automatically handles right-to-left text direction for Arabic
- **Interactive Elements**: Hover effects on tables, links, and images
- **Professional Typography**: Support for both English and Arabic fonts

## HTTP Status Codes

The server returns the following HTTP status codes:

- **200 OK**: Successful request with file/content
- **404 Not Found**: Requested resource doesn't exist
- **400 Bad Request**: Malformed HTTP request

## Server Statistics

The server tracks:

- **Total Requests**: Total number of HTTP requests received
- **Successful Requests**: Requests that returned 200 OK
- **Failed Requests**: Requests that returned 404 or 400

## Character Encoding

- **UTF-8 Encoding**: Full support for Arabic and special characters
- **Meta Charset**: `<meta charset="UTF-8">` declared in all HTML pages

## Supported File Types

| File Type   | Content-Type                        |
| ----------- | ----------------------------------- |
| HTML        | text/html                           |
| JPG/JPEG    | image/jpeg                          |
| PNG         | image/png                           |
| GIF         | image/gif                           |
| Other Files | application/octet-stream (download) |

## Student Information Included

The server displays information for three Computer Science students:

1. **Mariam Baradeiya** - ID: 1230663 - Completed: 91 credit hours
2. **Ramz AbuFarha** - ID: 1230963 - Completed: 71 credit hours
3. **Ruba Nabhan** - ID: 1230200 - Completed: 80 credit hours

## Notes

- Favicon requests (404) are normal and do not affect functionality
- The server handles both English and Arabic text properly with UTF-8 encoding
- All file paths are relative to the project root directory
- The server runs single-threaded and processes requests sequentially

## Troubleshooting

### Port Already in Use

If port 6663 is already in use:

1. Edit `server.py` and change `serverPort = 6663` to an available port
2. Update your browser URL accordingly

### Files Not Found

Ensure all files are in the correct directories as shown in the project structure above.

### Arabic Text Not Displaying Correctly

The HTML files include `<meta charset="UTF-8">` and `dir="rtl"` attributes. Ensure your browser supports UTF-8 encoding.

## Future Enhancements

Possible improvements for this project:

- Multi-threaded request handling
- SSL/HTTPS support
- More sophisticated routing
- Request logging to file
- Compression support
- Caching mechanisms

## Course

**Course**: ENCS3310 - Computer Networks (File Sharing Server Project)

---

**Created**: May 2026
**Last Updated**: June 2, 2026
