# HTTPS and Security Settings

- Enforced HTTPS with `SECURE_SSL_REDIRECT = True`.
- Implemented HSTS:
  - `SECURE_HSTS_SECONDS = 31536000`
  - `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
  - `SECURE_HSTS_PRELOAD = True`
- Cookies secured:
  - `SESSION_COOKIE_SECURE = True`
  - `CSRF_COOKIE_SECURE = True`
- Added headers:
  - `X_FRAME_OPTIONS = 'DENY'`
  - `SECURE_CONTENT_TYPE_NOSNIFF = True`
  - `SECURE_BROWSER_XSS_FILTER = True`
- Deployment: configure Nginx with SSL/TLS (Let’s Encrypt recommended).
