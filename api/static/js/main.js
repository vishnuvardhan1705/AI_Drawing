// Base API URL (adjust if backend is on another port/domain)
const API_BASE_URL = "http://127.0.0.1:8000/drawings/";

// Parse drawings data from template
const drawings = JSON.parse(document.getElementById("drawings-data").textContent);

const categorySelect = document.getElementById("categorySelect");
const drawingSelect = document.getElementById("drawing");

// ---------------------------
// Filtering: category → drawings
// ---------------------------
function updateDrawingOptions(category) {
    drawingSelect.innerHTML = '<option value="">Choose Here</option>';

    drawings.forEach(drawing => {
        if (category === "All" || drawing.category === category) {
            let opt = document.createElement("option");
            opt.value = drawing.id;        // ✅ use ID now
            opt.textContent = drawing.name;
            drawingSelect.appendChild(opt);
        }
    });
}

// Run once on load (show all drawings)
updateDrawingOptions("All");

// Update when category changes
categorySelect.addEventListener("change", function () {
    updateDrawingOptions(this.value);
});

// ---------------------------
// Fetch drawing by ID
// ---------------------------
async function fetchDrawing(id) {
    try {
        const response = await fetch(`${API_BASE_URL}${id}/`);
        if (!response.ok) {
            throw new Error("Drawing not found");
        }
        return await response.json();
    } catch (error) {
        console.error("Error fetching drawing:", error);
        return null;
    }
}

// ---------------------------
// Start Drawing button handler
// ---------------------------
document.querySelector(".strtbtn").addEventListener("click", async function () {
    const selectedId = drawingSelect.value;

    if (!selectedId) {
        alert("Please select a drawing first!");
        return;
    }

    const drawingData = await fetchDrawing(selectedId);
    
    if (drawingData) {
        displayDrawingSteps(drawingData.stepdiscription);
    }
});

// ---------------------------
// Render drawing steps
// ---------------------------
function displayDrawingSteps(steps) {
    const container = document.querySelector(".drawingstepssection");
    container.innerHTML = ""; // clear previous steps

    steps.forEach(step => {
        const stepDiv = document.createElement("div");
        stepDiv.classList.add("card", "p-3", "mb-3");

        stepDiv.innerHTML = `
            <h5>Step ${step.stepno}</h5>
            <p>${step.steptext}</p>
            <img src="${step.image}" class="img-fluid" alt="Step ${step.stepno}">
        `;

        container.appendChild(stepDiv);
    });
}
