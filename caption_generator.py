from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load the pre-trained model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def generate_caption(image_path):
    """
    Generates a caption for the given image.

    Args:
        image_path (str): Path to the image.

    Returns:
        str: Generated caption.
    """
    try:
        # Open and process the image
        image = Image.open(image_path).convert("RGB")
        inputs = processor(images=image, return_tensors="pt")
        outputs = model.generate(**inputs)

        # Decode the generated output
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        return f"Error generating caption: {e}"
