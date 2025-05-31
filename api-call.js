async function getPredictedLabel(processed_t) {
  try {
    console.log("processed_t:", processed_t);
    console.log("Type:", typeof processed_t);
    console.log("Length:", processed_t.length);
    console.log("All numbers:", processed_t.every(item => typeof item === "number"));

    // Check before calling the API
    if (!Array.isArray(processed_t) || processed_t.length !== 63 || !processed_t.every(item => typeof item === "number")) {
      console.error("Invalid input: processed_t must be an array of 63 numbers");
      return null;
    }

    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ landmarks: processed_t })  // Must match backend schema
    });

    if (!response.ok) {
      console.error("API error:", response.statusText);
      return null;
    }

    const result = await response.json();
    const label = result.prediction;

    if (["up", "down", "left", "right"].includes(label)) {
      console.log("Predicted label:", label);
      return label;
    } else {
      console.log("No valid gesture detected");
      return null;
    }
  } catch (error) {
    console.error("Prediction API failed:", error);
    return null;
  }
}
