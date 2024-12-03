## FastAPI - Nginx - Static Web File - Starter

This minimal example demonstrates how to use NGINX and FastAPI to serve static files and expose API endpoints.

### Path Structure

* **API Endpoint**: The API path is accessible via `/api`.
* **Static Files**: Static files are served from the `/static` path.
* **Static Website**: The static website content is served from the root path `/`.

### Nginx Configuration

The NGINX configuration files are located in the `nginx/conf.d` folder.

```
./www/html:/var/www/html
./nginx/conf.d:/etc/nginx/conf.d
./static:/var/static
```

### API Configuration

```bash
pip install --no-cache-dir -r requirements.txt
fastapi run main.py
```
