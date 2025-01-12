# **Optimizing Office Layouts in Revit Using Dynamo Generative Design and Machine Learning**

## **Project Overview**
This project focuses on the **optimization of office layouts** in Revit by leveraging **Dynamo's Generative Design capabilities** combined with **machine learning** to produce efficient, functional, and aesthetically pleasing designs. The project aims to enhance productivity and usability in office spaces while maintaining compliance with design standards such as clearance between furniture and accessibility requirements.

---

## **Key Features**
1. **Generative Design in Dynamo:**
   - Automated desk and furniture placement.
   - Grid-based and randomized object placement methods.
   - Optimization based on constraints such as spacing, clearance, and room dimensions.

2. **Machine Learning for Feedback Integration:**
   - Incorporates historical feedback or user-defined parameters for improved design iterations.
   - Identifies optimal layouts based on metrics like number of objects placed, clearance maintained, and efficient use of space.

3. **Revit Integration:**
   - Uses **Revit’s Ceiling and Lighting tools** to enhance visualization.
   - Automates model preparation, including lighting and furniture arrangement.

4. **Visualization:**
   - Exported models rendered using tools such as **Vedo**, **Forge Viewer**, and **Python 3D libraries** for interactive exploration.
   - Displays final results on a web page for stakeholders.

5. **Clash Detection:**
   - Ensures layouts are free of conflicts by leveraging **Navisworks** for clash detection before finalizing designs.

---

## **Project Workflow**
### **Step 1: Model Preparation in Revit**
- Created office spaces with predefined room separators and layouts.
- Added essential furniture such as desks, chairs, countertops, sinks, and lighting fixtures.

### **Step 2: Generative Design with Dynamo**
- Defined constraints (e.g., minimum distances between objects and walls).
- Set goals such as maximizing the number of objects placed while minimizing overlap.
- Used Dynamo's **Generative Design** feature to explore multiple layout options.

### **Step 3: Machine Learning Integration**
- Collected design feedback to train models for predicting optimal layouts.
- Implemented algorithms to balance clearance, functionality, and space utilization.

### **Step 4: Visualization**
- Exported models to **FBX/GLTF formats** and visualized in Python using **Vedo**.
- Embedded 3D models on a web page for interactive exploration using **Forge Viewer**.

### **Step 5: Validation**
- Performed clash detection using **Navisworks** to ensure practical viability.
- Incorporated necessary adjustments to resolve issues before finalizing.

---

## **Technologies Used**
- **Autodesk Revit**: Primary design tool.
- **Dynamo**: Automation and Generative Design workflows.
- **Python**: Data processing, visualization (Vedo).
- **Navisworks**: Clash detection and validation.
- **Forge Viewer**: Web-based 3D visualization.
- **Machine Learning Libraries**: Scikit-learn/TensorFlow (for predictive modeling).

---

## **How to Use**
### **Setup**
1. Clone the repository:
   ```bash
   git clone https://github.com/nafisatibrahim/office-layout-optimization_machine_learning.git
   ```
2. Install required dependencies for Dynamo, Python, and Forge Viewer:
   - Python: Install libraries like `vedo`, `pandas`.
   - Forge Viewer: Follow [Forge Viewer documentation](https://forge.autodesk.com/en/docs/viewer/v7/).

3. Ensure you have **Revit**, **Navisworks**, and Dynamo installed.

### **Execution**
1. Open the **Dynamo script** in Revit.
2. Define input parameters such as:
   - Room dimensions.
   - Distance constraints (e.g., 3 feet between desks).
   - Optimization goals (maximize desks, minimize overlap).
3. Run the **Generative Design study**.
4. Export the best layout for further rendering or clash detection.

### **Visualization**
- Use **Vedo** to render the 3D model in Python.
- Embed the 3D model on a webpage using Forge Viewer.

---

## **Sample Outputs**
1. **Generative Design Layouts**:
   - Visual representation of optimized office layouts.
2. **Interactive 3D Models**:
   - Embedded web-based exploration using Forge Viewer.
3. **Clash-Free Design**:
   - Validated layouts after running Navisworks.

---

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

