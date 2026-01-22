// send file to backend for compilation
async function distributeCompile() {
    const fileInput = document.getElementById("codeFileInput");
    const status = document.getElementById("status");
    const result = document.getElementById("result");

    if (!fileInput.files.length) {
        alert("Please select a .cpp file");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    status.textContent = "Uploading...";
    result.textContent = "";

    try {
        const res = await fetch("/compile", {
            method: "POST",
            body: formData
        });
        const data = await res.json();
        status.textContent = data.success ? "Done" : "Error";
        result.textContent = data.output;
        updateQueue();
        updateLogs();
    } catch (err) {
        status.textContent = "Error";
        result.textContent = err.message;
    }
}

// fetch current compile queue
async function updateQueue() {
    const queueEl = document.getElementById("queue");
    try {
        const res = await fetch("/queue");
        const data = await res.json();
        queueEl.textContent = JSON.stringify(data.queue, null, 2);
    } catch (err) {
        queueEl.textContent = "Failed to fetch queue";
    }
}

// fetch logs
async function updateLogs() {
    const logsEl = document.getElementById("logs");
    try {
        const res = await fetch("/logs");
        const data = await res.json();
        logsEl.textContent = data.logs.join("\n");
    } catch (err) {
        logsEl.textContent = "Failed to fetch logs";
    }
}

// refresh queue & logs every 5s
setInterval(() => {
    updateQueue();
    updateLogs();
}, 5000);
