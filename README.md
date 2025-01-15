# **Optimizing Office Layouts in Revit Using Dynamo Generative Design and Machine Learning**

## **Project Overview**
This project focuses on the **optimization of office layouts** in Revit by leveraging **Dynamo's Generative Design capabilities** combined with **machine learning** to produce efficient, functional, and aesthetically pleasing designs. The project aims to enhance productivity and usability in office spaces while maintaining compliance with design standards such as clearance between furniture and accessibility requirements.

![Office Layout Example](Images/office-optimization.jpg "Office Layout Example")

---

## Purpose  
- To design an efficient and data-driven tool that maximizes the number of desks in an office layout while ensuring comfort, accessibility, and compliance with design constraints.
- To integrate generative design (Revit Dynamo) and machine learning (Python) into a practical solution for architects and designers to make informed decisions.

## Learning Outcome
- Gain foundational skills in generative design.
- Learn how to integrate data analysis and machine learning for design optimization.
- Develop a decision-making tool that visualizes and ranks layouts.

## Structure
1. **Introduction**
    - Overview of the problem (efficient office layouts).
    - Importance of integrating generative design and machine learning.
2. **Tools and Technologies**
    - Revit Dynamo (generative design).
    - Python (data analysis, data visualization, and machine learning).
    - Visualization tools (Power BI or/and Python).
    - Other if necessary: Revit API, Scikit-Learn, TensorFlow.
3. **Workflow Breakdown**
    - Design generation.
    - Data extraction and preprocessing.
    - Machine learning analysis and ranking.
    - Visualization and decision-making.
4. **Evaluation Metrics**
    - Number of desks.
    - Accessibility (aisle widths).
    - Additional factors like proximity to windows.

---

# Revit Projects

| Step | Description                             | Image                                                                 |
|------|-----------------------------------------|-----------------------------------------------------------------------|
| 1    | Before Dynamo                           | ![Before Dynamo](Revit%20projects/first-attempt-of-office-layout-too-dense.jpg)                 |
| 2    | Second Attempt - Wrong Coordinates      | ![Second Attempt](Revit%20projects/second-attempt-wrong-coordinates.jpg) |
| 3    | Fifth Attempt - Sliders and Coordinates Fixed | ![Fifth Attempt](Revit%20projects/third-attempt-cross-prooduct-sliders.jpg) |
| 4    | Study Running 5-10                      | ![Study Running](Revit%20projects/fourth-attempt-cross-product-slider15.jpg)        |
| 5    | Layout in Navisworks                    | ![Navisworks](Revit%20projects/fifth-attempt-sliders-and-coordinates-fixed.jpg)  |


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

