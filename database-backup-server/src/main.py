from http.server import HTTPServer
from package.server import Server

HOST_NAME = "0.0.0.0"
SERVER_PORT = 8080

# Entry point for the server

if __name__ == "__main__":
  httpServer = HTTPServer((HOST_NAME, SERVER_PORT), Server)
  print(f"Server started at http://{HOST_NAME}:{SERVER_PORT}")
  try:
    httpServer.serve_forever()
  except KeyboardInterrupt:
    httpServer.server_close()
    print("Server stopped")