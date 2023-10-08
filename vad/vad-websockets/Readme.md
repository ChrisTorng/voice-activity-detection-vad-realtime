https://dashboard.ngrok.com/cloud-edge/domains
Get a domain freely: dear-annually-robin.ngrok-free.app

Optional for internet access:
New command line:
`cd vad\vad-websockets`
- Start Tunneling: `ngrok start --all --config ngrok.yml`

New command line:
`cd vad\vad-websockets`
- Start Server to Open index.html: `python -m http.server 5001`
Open http://localhost:5001/ or ngrok: https://dear-annually-robin.ngrok-free.app/

New command line:
`cd vad\vad-websockets`
- Start Websockets Server
    - (1) `python .\vad-websockets.py`
    - (2) `python .\vad-websockets-perclient.py`