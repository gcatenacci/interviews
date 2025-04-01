import * as http from 'http';

const PORTS = [8080, 9090];

async function logAccess(port: number) {
  console.log(`Accessed port ${port}`);
}

function createServer(port: number, message: string) {
  http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end(message);
    logAccess(port);
  }).listen(port, () => {
    console.log(`Server running on port ${port}`);
  });
}

createServer(8080, 'Hello from 8080');
createServer(9090, 'Hello from 9090');
