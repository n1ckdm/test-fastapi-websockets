from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.websockets import WebSocket

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>FastAPI</title>
    </head>
    <body>
        <h1>WebSocket Test</h1>
        <form action="" onsubmit="connectWS1(event)">
            <button>Connect to ws://localhost/ws</button>
        </form>
        <br/>
        <form action="" onsubmit="connectWS(event)">
            <button>Connect to ws://localhost/error</button>
        </form>
        <script>
            function connectWS1(event) {
                var ws = new WebSocket("ws://localhost/ws");
                ws.addEventListener('open', (event) => {
                    ws.send('Hello Server!');
                    alert('WebSocket Connected!')
                });
                event.preventDefault()
            }
            function connectWS2(event) {
                var ws = new WebSocket("ws://localhost/error");
                ws.addEventListener('open', (event) => {
                    ws.send('Hello Server!');
                    alert('WebSocket Connected!')
                });
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
