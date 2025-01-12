from vedo import load, Plotter

# Path to the OBJ file
obj_file = r"C:\Users\Nafis\OneDrive\Documentos\GitHub\office_layout_optimization_machine_learning\Input\SimpleOfficelayout-3DView-{3D}.obj"

# Load the 3D model
model = load(obj_file)

# Create a Plotter object for interactivity
plotter = Plotter(title="Dynamic 3D Model Viewer", axes=True, bg="lightblue")

# Add the model to the plotter
plotter.add(model)

# Customize the camera view
plotter.camera.SetPosition([200, 200, 200])  # Adjust the camera to a custom position
plotter.camera.SetFocalPoint([0, 0, 0])  # Focus on the model
plotter.camera.SetViewUp([0, 0, 1])  # Set Z-axis as the "up" direction

# Show the model in interactive mode
plotter.show(interactive=True)
