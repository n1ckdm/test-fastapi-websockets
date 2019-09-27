# Websocket Test with FastAPI

## Running

Build the docker image and run it:

```docker
docker build -t wstest .
docker run -d --name wstest -p 80:80 wstest
```

Navigate to <http://localhost/> and then view the container logs with:

```docker
docker logs -f wstest
```

You should find that when clicking on the `ws://localhost/ws` button everything works fine, but clicking on the `ws://localhost/error` button gives a 403 (forbidden) error from uvicorn becuase the route doesn't exist (although this is a somewhat misleading error).
