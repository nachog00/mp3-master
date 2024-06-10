const { app, BrowserWindow } = require('electron');
const path = require('path');

function createWindow() {
    const win = new BrowserWindow({
        width: 800,
        height: 600,
        webPreferences: {
            nodeIntegration: true,
            preload: path.join(__dirname, 'frontend/preload.js')
        }
    })
    
    win.loadFile('frontend/index.html')

    // Run the python backend
    var python = require('child_process').spawn('./backend/.venv/Scripts/python', ['./backend/main.py']);

    python.stdout.on('data', function (data) {
        console.log("data: ", data.toString('utf8'));
    });

    python.stderr.on('data', (data) => {
        console.log(`stderr: ${data}`); // when error
    });
}

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow()
    }
})