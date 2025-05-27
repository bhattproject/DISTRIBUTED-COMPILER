#!/bin/bash
echo "Starting Flask server on port 5000..."
cd server && python3 app.py &
cd ../client && python3 peer1.py &
cd ../client && python3 peer2.py &
