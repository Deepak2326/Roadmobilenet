document.addEventListener("DOMContentLoaded", function () {
    const dropbox = document.getElementById("dropbox");
    const fileInput = document.getElementById("fileInput");
    const classificationResult = document.getElementById("classificationResult");

    // ✅ Logout Functionality
    document.getElementById("logout").addEventListener("click", function () {
        localStorage.removeItem("authToken");
        window.location.href = "index.html";
    });

    // ✅ Handle Dropbox Click
    dropbox.addEventListener("click", function () {
        fileInput.click();
    });

    // ✅ Handle File Selection
    fileInput.addEventListener("change", function (event) {
        if (event.target.files.length > 0) {
            uploadImage(event.target.files[0]);
        }
    });

    // ✅ Handle Drag & Drop Upload
    dropbox.addEventListener("dragover", function (event) {
        event.preventDefault();
        dropbox.style.backgroundColor = "#3a3a3a"; // Match hover color
    });

    dropbox.addEventListener("dragleave", function () {
        dropbox.style.backgroundColor = "#2a2a2a"; // Reset to original
    });

    dropbox.addEventListener("drop", function (event) {
        event.preventDefault();
        dropbox.style.backgroundColor = "#2a2a2a"; // Reset to original
        if (event.dataTransfer.files.length > 0) {
            uploadImage(event.dataTransfer.files[0]);
        }
    });

    async function uploadImage(file) {
        const formData = new FormData();
        formData.append("file", file);

        const token = localStorage.getItem("authToken");
        if (!token) {
            alert("Session expired. Please login again.");
            window.location.href = "index.html"; // Redirect to login
            return;
        }

        // Show loading state
        classificationResult.style.display = "block";
        classificationResult.textContent = "Uploading & classifying...";
        classificationResult.className = "classification-result";

        try {
            const response = await fetch("http://127.0.0.1:5000/api/upload", {
                method: "POST",
                headers: { "Authorization": `Bearer ${token}` },
                body: formData
            });

            const data = await response.json();
            console.log("Server Response:", data);

            if (response.ok) {
                displayClassification(data.category, data.confidence);  // Now also passing confidence score
            } else {
                if (response.status === 401) {
                    alert("Session expired. Please login again.");
                    localStorage.removeItem("authToken");
                    window.location.href = "index.html";
                } else {
                    alert("Error: " + (data.error || "Failed to classify image."));
                }
            }
        } catch (error) {
            console.error("Network Error:", error);
            alert("Network error, please try again.");
        }
    }

    function displayClassification(category, confidence) {
        classificationResult.textContent = `Classified as: ${category} (Confidence: ${confidence.toFixed(2)}%)`;
        classificationResult.className = "classification-result"; // Reset classes

        if (category === "Minor") classificationResult.classList.add("minor");
        else if (category === "Moderate") classificationResult.classList.add("moderate");
        else if (category === "Major") classificationResult.classList.add("major");
    }
});
