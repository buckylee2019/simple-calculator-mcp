#!/bin/bash

# Start the server in the background
echo "Starting Simple Calculator MCP server..."
python src/main.py &
SERVER_PID=$!

# Wait for the server to start
echo "Waiting for server to start..."
sleep 5

# Run the test client
echo "Running test client..."
python test_mcp_client.py

# Shutdown the server
echo "Shutting down server..."
kill $SERVER_PID

echo "Tests completed."
