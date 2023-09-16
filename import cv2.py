import cv2
import numpy as np

def process_medical_image(input_image_path, output_image_path):
    # Load the medical image
    image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)

    # Apply Gaussian blur to reduce noise (adjust kernel size as needed)
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Apply thresholding (adjust threshold value as needed)
    _, thresholded_image = cv2.threshold(blurred_image, 128, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image
    result_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    cv2.drawContours(result_image, contours, -1, (0, 255, 0), 2)

    # Save the processed image
    cv2.imwrite(output_image_path, result_image)

    # Display the processed image (optional)
    cv2.imshow('Processed Medical Image', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_image_path = "input_image.png"
    output_image_path = "output_image.png"
    process_medical_image(input_image_path, output_image_path)
