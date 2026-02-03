"""Local Protocol sample server."""

import argparse

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import asks, bids, discovery

app = FastAPI(
  title="Local Protocol Sample Server",
  description="Reference implementation for Local Protocol conformance testing",
  version="0.1.0",
)

# CORS middleware
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=False,
  allow_methods=["*"],
  allow_headers=["*"],
)

# Include routers
app.include_router(discovery.router)
app.include_router(asks.router)
app.include_router(bids.router)


def main() -> None:
  """Run the server."""
  parser = argparse.ArgumentParser(description="Local Protocol Sample Server")
  parser.add_argument(
    "--host",
    type=str,
    default="0.0.0.0",
    help="Host to bind to",
  )
  parser.add_argument(
    "--port",
    type=int,
    default=8000,
    help="Port to bind to",
  )
  parser.add_argument(
    "--reload",
    action="store_true",
    help="Enable auto-reload for development",
  )
  args = parser.parse_args()

  uvicorn.run(
    "server:app",
    host=args.host,
    port=args.port,
    reload=args.reload,
  )


if __name__ == "__main__":
  main()
