# DISTRIBUTED-COMPILER
THIS COMPILER DISTRIBUTES CODE BETWEEN MACHINES 

in vs code terminal ---





Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\venv\Scripts\activate
ls
ip install -r requirements.txt

open in browser         http://localhost:5000 


✅ FIX THAT FIRST — Unlock PowerShell Script Execution (Do This Only Once)
Open PowerShell as Administrator

Search "PowerShell" in Start Menu

Right-click → “Run as Administrator”

Then paste this command once to allow PowerShell scripts:



Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
Press Y and Enter.

✅ Done — this now allows your Activate.ps1 script to run.

You only need to do this once per user account.
🧪 Step 2: In EACH window/tab, activate your virtual environment
Run this in each window:


then on powershell

cd "D:\XXXXXXXXXXXXXX\minitorrent"
.\venv\Scripts\Activate.ps1
✅ If it works, your terminal will look like this:


(venv) PS  "D:\XXXXXXXXXXXXXX\minitorrent"
🧪 Step 3: In FIRST window → run Flask server

1-------------
cd server
python app.py
✅ Output should say:


Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
🧪 Step 4: In SECOND window → run Peer 1

2-------------
cd client
python peer1.py
✅ It should connect to the server and wait for files.

🧪 Step 5: In THIRD window → run Peer 2

3---------------
cd client
python peer2.py
✅ You now have server + 2 clients running!
