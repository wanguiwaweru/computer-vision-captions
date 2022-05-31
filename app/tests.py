from main import is_valid_image
import pytest

accurateImageDetails = {
    "url": "https://images.unsplash.com/photo-1535118563-03669b04f829?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTd8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=600&q=60",
    "image_format" :"image/jpeg",
    "width":400,
    "height":600,
    "totalBytes":35515
    }

inaccurateImageFormat = {
    "url": "https://images.unsplash.com/photo-1535118563-03669b04f829?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTd8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=600&q=60",
    "image_format" :"text/html",
    "width":400,
    "height":600,
    "totalBytes":35515
}

inaccurateImageSize = {
    "url": "https://images.unsplash.com/photo-1535118563-03669b04f829?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTd8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=600&q=60",
    "image_format" :"image/png",
    "width":40,
    "height":20,
    "totalBytes":35515
}

inaccurateFileSize = {
    "url": "https://images.unsplash.com/photo-1535118563-03669b04f829?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTd8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=600&q=60",
    "image_format" :"image/png",
    "width":400,
    "height":600,
    "totalBytes":6551500
}

accurateImageSize = {
    "url": "https://images.unsplash.com/photo-1535118563-03669b04f829?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MTd8fHxlbnwwfHx8fA%3D%3D&auto=format&fit=crop&w=600&q=60",
    "image_format" :"image/jpg",
    "width":40,
    "height":600,
    "totalBytes":65510
}

def test_is_valid_image():
    assert is_valid_image(accurateImageDetails) == True
    assert is_valid_image(inaccurateImageFormat) == "Invalid image format."
    assert is_valid_image(inaccurateFileSize) == "Image file size must be less than 4MB"
    assert is_valid_image(inaccurateImageSize) == "Image should be greater than 50 x 50"
    assert is_valid_image(accurateImageSize) == True