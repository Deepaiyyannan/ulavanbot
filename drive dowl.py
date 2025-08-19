import requests
from PIL import Image
from io import BytesIO

# ✅ File ID from your Google Drive link
file_id = "1nSwlTRGPyJpPhi2b6RBbjWWlREHy1JF4"

# ✅ Direct download link format
url = f"https://drive.google.com/uc?export=download&id={file_id}"

# Download the image
response = requests.get(url)
response.raise_for_status()  # raises error if request fails

# Open as image
img = Image.open(BytesIO(response.content))
img.show()

# Save image
img.save("downloaded_image.jpg")
print("✅ Image saved as downloaded_image.jpg")

