import kagglehub

# Download latest version
path = kagglehub.dataset_download("mateuszbuda/lgg-mri-segmentation")

print("Path to dataset files:", path)

# Create ~/.kaggle/kaggle.json:
#   {"username":"curtis12345","key":"cc37227e37f67396fac644906cf45c35"}
# Link the downloaded directory to where the benchmark wants it:
#   ln -s ~/.cache/kagglehub/datasets/mateuszbuda/lgg-mri-segmentation/versions/2 ~/.cache/mldata/lgg-segmentation

