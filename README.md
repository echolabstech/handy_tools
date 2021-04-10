# handy_tools
This is for sending files from your phone to your laptop. Alternatives to this tool include dropbox, connecting your phone to your laptop via USB, airdrop, etc... Sometimes these tools don't work or aren't preferred for reasons.

## requirements to use this tool
- python3.8 or higher
- pip3 for python3.8 or higher
- a web browser

## How to use this tool
### setup env vars
```
export FLASK_DEBUG=1
export FLASK_APP=app.py
export FLASK_ENV=development
```

### instructions
1. pip3 install requirements.txt
2. flask run -p 5002
3. view http://127.0.0.1:5002/ from web browser on your phone