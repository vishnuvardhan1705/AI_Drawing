// main.js

// Base API URL (adjust if backend is on another port/domain)
const API_BASE_URL = "http://127.0.0.1:8000/api/items/";

// Populate drawings dropdown from backend
async function fetchDrawing(name) {
    try {
        const response = await fetch(`${API_BASE_URL}${name}/`);
        if (!response.ok) {
            throw new Error("Drawing not found");
        }
        return await response.json();
    } catch (error) {
        console.error("Error fetching drawing:", error);
        return null;
    }
}

// Event handler when category is selected
document.getElementById("categorySelect").addEventListener("change", async function () {
    const category = this.value;

    // For now, we assume category matches drawing `name` in DB
    if (category) {
        const drawingData = await fetchDrawing(category);

        const drawingSelect = document.getElementById("drawing");
        drawingSelect.innerHTML = '<option value="">Choose Here</option>'; // reset dropdown

        if (drawingData) {
            // Add the drawing to dropdown
            let opt = document.createElement("option");
            opt.value = drawingData.id;
            opt.textContent = drawingData.name;
            drawingSelect.appendChild(opt);
        }
    }
});

// Event handler when "Start Drawing" button is clicked
document.querySelector(".strtbtn").addEventListener("click", async function () {
    const drawingSelect = document.getElementById("drawing");
    const selectedId = drawingSelect.value;

    if (!selectedId) {
        alert("Please select a drawing first!");
        return;
    }

    // Find selected drawing (we need to fetch it again by name, or store earlier)
    const selectedName = drawingSelect.options[drawingSelect.selectedIndex].text;
    const drawingData = await fetchDrawing(selectedName);

    if (drawingData) {
        displayDrawingSteps(drawingData.stepdiscription);
    }
});

// Function to render steps
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
