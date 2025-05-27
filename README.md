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
![Screenshot 2025-05-27 060843](https://github.com/user-attachments/assets/0fd9c6fe-dc8f-450f-9f64-edc83e7ab1d9)



![Screenshot 2025-05-27 060853](https://github.com/user-attachments/assets/1f5146e0-d518-48e9-8ab0-0405aded89c0)














in vs code terminal create environmnet using 
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate



--------------------------------------------------------------------
Step 1: Open PowerShell as Administrator
Click Start, type powershell

Right-click Windows PowerShell → Run as administrator

Click Yes to allow it

Step 2: In the Administrator PowerShell window, run this command to temporarily allow scripts:
powershell
Copy
Edit
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
When prompted, type Y and press Enter

Step 3: Leave this Administrator PowerShell window open.
Now, without closing this window:

Step 4: Navigate to your project folder in this Administrator PowerShell:
powershell
Copy
Edit
cd "D:\projectxxx'\DIST1\minitorrent"
Step 5: Activate your virtual environment here:
powershell
Copy
Edit
.\venv\Scripts\activate


-----------------------------------------------
ls
cd ..
pip install -r requirements.txt
Since there’s no app.py but you do have a run.sh, this shell script probably runs your server or project.

How to run run.sh on Windows?
Windows PowerShell doesn’t run .sh scripts natively.

You can either:

Option 1: Run the commands inside run.sh manually in PowerShell.

Option 2: Use Git Bash (or WSL) on Windows to run the .sh script directly.

What to do now?
Open the run.sh file in VS Code or any text editor and copy-paste the contents here, so I can help translate it to PowerShell commands if needed.

Or, if you have Git Bash installed, open Git Bash terminal, navigate to this folder and run:

bash
Copy
Edit
./run.sh

