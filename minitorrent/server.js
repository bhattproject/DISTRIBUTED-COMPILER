import express from "express";
import multer from "multer";
import cors from "cors";
import { exec } from "child_process";
import fs from "fs";
import path from "path";

const app = express();
const PORT = 3000;

// basic middleware stuff
// cors so frontend can hit this API without browser crying
app.use(cors());
app.use(express.json());

// folder to store uploaded cpp files
// creating it here so server doesn't crash if it doesn't exist
const UPLOAD_DIR = "./uploads";
if (!fs.existsSync(UPLOAD_DIR)) {
    fs.mkdirSync(UPLOAD_DIR);
}

// multer config for handling file uploads
// not fully optimized, just enough for now
const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, UPLOAD_DIR);
    },
    filename: (req, file, cb) => {
        // adding timestamp so files don't overwrite each other
        cb(null, `${Date.now()}-${file.originalname}`);
    }
});

const upload = multer({ storage });

// simple route to check if backend is alive
// helps while debugging frontend
app.get("/health", (req, res) => {
    res.json({ status: "ok" });
});

// main compile endpoint
// later this will be extended for distributed compilation
app.post("/compile", upload.single("file"), (req, res) => {

    // basic check, nothing fancy
    if (!req.file) {
        return res.status(400).json({
            error: "No file uploaded"
        });
    }

    const filePath = req.file.path;

    // output binary name (same as source file for now)
    // this might change once distribution is added
    const outputBinary = filePath.replace(".cpp", "");

    /*
        TODO:
        - split compilation work
        - send chunks to other nodes
        - wait for responses
        - merge results

        For now this just compiles locally to test the flow.
    */

    exec(`g++ ${filePath} -o ${outputBinary}`, (error, stdout, stderr) => {

        if (error) {
            // g++ errors usually go to stderr
            return res.json({
                success: false,
                phase: "compile",
                output: stderr
            });
        }

        // if we reach here, compilation worked
        res.json({
            success: true,
            phase: "compile",
            output: "Compilation successful",
            binary: path.basename(outputBinary)
        });
    });
});

// starting server
// keeping this simple for now
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
