def get_parameters(net_resolution="-1x368", model_pose="BODY_25"):
  params = dict()
  params["logging_level"] = 3
  params["output_resolution"] = "-1x-1"
  params["net_resolution"] = net_resolution
  params["model_pose"] = model_pose
  params["alpha_pose"] = 0.6
  params["scale_gap"] = 0.3
  params["scale_number"] = 1
  params["render_threshold"] = 0.05
  # If GPU version is built, and multiple GPUs are available, set the ID here
  params["num_gpu_start"] = 0
  params["disable_blending"] = False
  # Ensure you point to the correct path where models are located
  params["default_model_folder"] =  "models/"
  # Construct OpenPose object allocates GPU memory
  return params
