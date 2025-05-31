📊 Monitoring Metrics for Model Performance and Server Health
-------------------------------------------------------------

### 1\. **Model-Related Metric**

#### 🔹 Metric: *CPU Time for Model Inference*

-   **What it Measures:**\
    The total CPU time used by your model-serving process.

-   **Why it Matters:**\
    Helps assess how much CPU your model inference is consuming over time --- essential for performance tuning and cost monitoring.

* * * * *

### 2\. **`python_gc_collections_total` (Data-Related)**

#### 🔹 Best Visualization: **Gauge**

-   **Why a Gauge?**

    -   Provides a clear snapshot of the total number of garbage collection events.

    -   Useful when you want a real-time count without focusing on historical trends.

    -   Allows for threshold-based coloring to indicate abnormal GC activity levels.

-   **How to Use:**

    -   Display the raw counter value to show how many collections have occurred.

    -   Optionally reset or compare with previous values manually if needed.

    -   Use thresholds to highlight unusually high GC activity.

* * * * *

### 3\. **`process_resident_memory_bytes` (Server-Related)**

#### 🔹 Best Visualization: **Pie Chart**

-   **Why a Pie Chart?**

    -   Clearly shows memory usage as a portion of total available memory.

    -   Useful for visualizing the relative memory consumption of processes or components.

    -   Intuitive for quickly understanding memory distribution.

-   **How to Use:**

    -   Combine with total system memory to show used vs. free memory.

    -   Slice the chart by service/component if applicable.

    -   Apply color coding to indicate warning or critical usage thresholds.