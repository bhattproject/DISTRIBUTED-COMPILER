function distributeCompile() {
    const fileInput = document.getElementById("codeFileInput");
    const file = fileInput.files[0];
    if (!file) {
        alert("Please select a .cpp file.");
        return;
    }
    const formData = new FormData();
    formData.append("file", file);
    fetch("/distribute_compile", {
        method: "POST",
        body: formData
    })
    .then(resp => resp.text())
    .then(msg => document.getElementById("result").innerHTML = msg);
}
