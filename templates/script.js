document.addEventListener("DOMContentLoaded", () => {
    const sections = document.querySelectorAll("section");
    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("visible");
            }
        });
    });

    sections.forEach(section => observer.observe(section));

    // Form submission (simulated prediction result)
    const form = document.getElementById("prediction-form");
    form.addEventListener("submit", (e) => {
        e.preventDefault(); // Prevent actual form submission

        // Display simulated result
        const resultMessage = document.getElementById("result-message");
        resultMessage.textContent = "Prediction: Based on your inputs, your risk of heart disease is moderate.";
        resultMessage.classList.remove("hidden");
    });
});
