# Simple Calculator MCP

A Model Context Protocol (MCP) server that provides simple calculator functions for performing operations on numbers.

## Overview

Simple Calculator MCP is a lightweight tool that demonstrates how to build an MCP server using FastMCP and Server-Sent Events (SSE) transport. It provides basic arithmetic operations like addition, subtraction, multiplication, division, as well as more advanced mathematical functions like trigonometry, logarithms, and factorials.

This tool runs as a remote MCP server using Server-Sent Events (SSE) transport, allowing it to be deployed centrally and accessed by any MCP-compatible client, including Amazon Q Developer CLI, Claude, and other AI assistants that support the MCP protocol.

## Features

- **Basic Arithmetic**: Addition, subtraction, multiplication, division
- **Advanced Operations**: Power, modulo, square root, factorial
- **Scientific Functions**: Logarithms, trigonometric functions (sin, cos, tan)
- **Expression Evaluation**: Calculate simple mathematical expressions
- **Session Management**: Proper handling of concurrent connections and session expiration
- **Health Check Endpoint**: For monitoring server status

## Installation

### Prerequisites

- Python 3.11+ (or Docker)

### Setup

#### Option 1: Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-calculator-mcp.git
   cd simple-calculator-mcp
   ```

2. Create virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

#### Option 2: Docker Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-calculator-mcp.git
   cd simple-calculator-mcp
   ```

2. Build the Docker image:
   ```bash
   docker build -t simple-calculator-mcp -f Dockerfile .
   ```

3. Run the Docker container:
   ```bash
   docker run -p 8000:8000 simple-calculator-mcp
   ```

## Usage

### Starting the Server

#### Local:
```bash
python src/main.py --host 0.0.0.0 --port 8000
```

#### Docker:
```bash
# The server starts automatically when running the container
docker run -p 8000:8000 simple-calculator-mcp
```

### Testing the Server

#### Automated Testing
The repository includes a test script that will start the server, run tests against all calculator functions, and then shut down the server:

```bash
./run_tests.sh
```

#### Manual Testing with the Test Client
You can also run the test client manually after starting the server:

```bash
# Start the server in one terminal
python src/main.py

# Run the test client in another terminal
python test_mcp_client.py
```

### Configuring MCP Clients

To connect to your remote MCP server, configure your MCP client with:

```json
{
  "mcpServers": {
      "calculator": {
        "command": "npx",
        "args": [
          "mcp-remote", 
          "http://localhost:8000/mcp", 
          "--allow-http", 
          "--transport", 
          "streamable-http"
        ]
      }
  }
}
```

### Available Tools

- `add(a, b)`: Add two numbers together
- `subtract(a, b)`: Subtract the second number from the first
- `multiply(a, b)`: Multiply two numbers together
- `divide(a, b)`: Divide the first number by the second
- `power(base, exponent)`: Raise the base to the power of the exponent
- `modulo(a, b)`: Calculate the remainder when the first number is divided by the second
- `calculate(expression)`: Evaluate a simple mathematical expression
- `square_root(number)`: Calculate the square root of a number
- `factorial(number)`: Calculate the factorial of a non-negative integer
- `logarithm(number, base)`: Calculate the logarithm of a number with the specified base
- `trigonometric(function, angle, is_radians)`: Calculate trigonometric functions (sin, cos, tan)

## Examples

### Addition

```
add(5, 3)
```

Result:
```
## Addition Result

5 + 3 = 8
```

### Subtraction

```
subtract(10, 4)
```

Result:
```
## Subtraction Result

10 - 4 = 6
```

### Multiplication

```
multiply(6, 7)
```

Result:
```
## Multiplication Result

6 × 7 = 42
```

### Division

```
divide(20, 5)
```

Result:
```
## Division Result

20 ÷ 5 = 4.0
```

### Power

```
power(2, 8)
```

Result:
```
## Power Result

2 ^ 8 = 256
```

### Square Root

```
square_root(16)
```

Result:
```
## Square Root Result

√16 = 4.0
```

### Factorial

```
factorial(5)
```

Result:
```
## Factorial Result

5! = 120
```

### Logarithm

```
logarithm(100, 10)
```

Result:
```
## Logarithm Result

log_10(100) = 2.0
```

### Trigonometric Function

```
trigonometric("sin", 30, False)
```

Result:
```
## Sine Result

sin(30°) = 0.5
```

### Expression Calculation

```
calculate("2 + 3 * 4")
```

Result:
```
## Calculation Result

2 + 3 * 4 = 14
```

## Security Considerations

- The `calculate` function uses Python's `eval()` which can be dangerous with untrusted input. In a production environment, you should use a safer expression evaluator.
- The server implements basic input validation to prevent malicious expressions.
- Sessions automatically expire after a configurable timeout (default: 30 minutes)

## Deploying to a Remote Server

To deploy the MCP server to a remote machine:

1. Install Docker on your remote server
2. Copy the project files to the server or clone from your repository
3. Build and run the Docker container:
   ```bash
   docker build -t simple-calculator-mcp -f Dockerfile .
   docker run -d -p 8000:8000 simple-calculator-mcp
   ```

For secure access, consider setting up:
- A reverse proxy with SSL/TLS (like Nginx or Traefik)
- Authentication middleware
- Firewall rules to restrict access

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- MCP protocol developers for enabling AI-powered tools
