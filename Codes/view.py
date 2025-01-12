from vedo import load, Plotter, Light

# Path to the OBJ file
obj_file = r"C:\Users\Nafis\OneDrive\Documentos\GitHub\office_layout_optimization_machine_learning\Input\SimpleOfficelayout-3DView-{3D}.obj"

# Load the 3D model
model = load(obj_file)

# Create a Plotter object for interactivity
plotter = Plotter(title="Dynamic 3D Model Viewer", axes=True, bg="lightblue")

# Add the model to the plotter
plotter.show(model, viewup="z")  # 'viewup="z"' sets the vertical axis as Z

# Add a grid to the background
plotter.add_grid()

# Add a custom light source
light = Light(position=(0, 0, 200), intensity=1.0, c="white")  # Positioned above the model
plotter.add_light(light)

# Customize camera view
plotter.camera.SetPosition([200, 200, 200])  # Adjust camera to start at a custom position
plotter.camera.SetFocalPoint([0, 0, 0])  # Focus on the model
plotter.camera.SetViewUp([0, 0, 1])  # Set Z-axis as the "up" direction

plotter.export_html("3d_model_viewer.html")


# Enable interactivity (rotate, zoom, pan)
plotter.interactive()
