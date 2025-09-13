#!/usr/bin/env python3
"""
Image overlay module for adding prediction results to uploaded images.
Uses Pillow to draw prediction information on images.
"""

from PIL import Image, ImageDraw, ImageFont
import io
import logging
from typing import Dict, Any

logger = logging.getLogger(__name__)

class ImageOverlay:
    """Class for adding prediction overlays to images."""
    
    def __init__(self):
        """Initialize the image overlay processor."""
        self.default_font_size = 16
        self.overlay_color = (255, 255, 255, 200)  # Semi-transparent white
        self.text_color = (0, 0, 0, 255)  # Black text
        self.border_color = (0, 0, 0, 255)  # Black border
    
    def add_prediction_overlay(self, image_data: bytes, prediction_result: Dict[str, Any]) -> Image.Image:
        """
        Add prediction overlay to the uploaded image.
        
        Args:
            image_data: Raw image bytes
            prediction_result: Prediction results from the model
            
        Returns:
            PIL Image with overlay added
        """
        try:
            # Open the image
            image = Image.open(io.BytesIO(image_data))
            
            # Convert to RGBA if not already
            if image.mode != 'RGBA':
                image = image.convert('RGBA')
            
            # Create overlay
            overlay = Image.new('RGBA', image.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(overlay)
            
            # Calculate overlay position (top-right corner)
            overlay_width = 350
            overlay_height = 200
            margin = 20
            
            # Position in top-right corner
            x = image.width - overlay_width - margin
            y = margin
            
            # Ensure overlay fits within image bounds
            if x < 0:
                x = margin
                overlay_width = image.width - 2 * margin
            if y < 0:
                y = margin
            
            # Draw semi-transparent background rectangle
            draw.rectangle(
                [x, y, x + overlay_width, y + overlay_height],
                fill=self.overlay_color,
                outline=self.border_color,
                width=2
            )
            
            # Try to load a font, fall back to default if not available
            try:
                font = ImageFont.truetype("arial.ttf", self.default_font_size)
                small_font = ImageFont.truetype("arial.ttf", self.default_font_size - 2)
            except (OSError, IOError):
                try:
                    font = ImageFont.load_default()
                    small_font = ImageFont.load_default()
                except:
                    font = None
                    small_font = None
            
            # Prepare text content
            probability_text = f"Readmit probability: {prediction_result['readmit_probability_percent']}"
            prediction_text = f"Prediction: {prediction_result['prediction']}"
            
            # Risk factors text
            risk_factors = prediction_result.get('risk_factors', [])
            risk_text_lines = ["Top risk factors:"]
            for factor in risk_factors[:3]:  # Top 3 factors
                risk_text_lines.append(f"• {factor['factor']}")
            
            # Draw text
            text_y = y + 15
            line_height = 25
            
            # Draw probability
            draw.text((x + 10, text_y), probability_text, fill=self.text_color, font=font)
            text_y += line_height
            
            # Draw prediction
            draw.text((x + 10, text_y), prediction_text, fill=self.text_color, font=font)
            text_y += line_height + 5
            
            # Draw risk factors
            for i, line in enumerate(risk_text_lines):
                current_font = font if i == 0 else small_font
                draw.text((x + 10, text_y), line, fill=self.text_color, font=current_font)
                text_y += line_height - 3 if i > 0 else line_height
            
            # Composite the overlay onto the original image
            result_image = Image.alpha_composite(image, overlay)
            
            # Convert back to RGB if needed
            if result_image.mode == 'RGBA':
                # Create a white background
                background = Image.new('RGB', result_image.size, (255, 255, 255))
                background.paste(result_image, mask=result_image.split()[-1])  # Use alpha channel as mask
                result_image = background
            
            return result_image
            
        except Exception as e:
            logger.error(f"Error adding overlay to image: {str(e)}")
            # Return original image if overlay fails
            try:
                return Image.open(io.BytesIO(image_data))
            except:
                # Create a simple error image
                error_image = Image.new('RGB', (400, 300), (255, 255, 255))
                draw = ImageDraw.Draw(error_image)
                draw.text((50, 150), "Error processing image", fill=(255, 0, 0))
                return error_image
    
    def create_prediction_summary_image(self, prediction_result: Dict[str, Any], 
                                      width: int = 400, height: int = 300) -> Image.Image:
        """
        Create a standalone image with prediction summary.
        Useful when no image is uploaded but you want to return a visual result.
        
        Args:
            prediction_result: Prediction results from the model
            width: Image width
            height: Image height
            
        Returns:
            PIL Image with prediction summary
        """
        try:
            # Create new image with white background
            image = Image.new('RGB', (width, height), (255, 255, 255))
            draw = ImageDraw.Draw(image)
            
            # Try to load font
            try:
                title_font = ImageFont.truetype("arial.ttf", 20)
                font = ImageFont.truetype("arial.ttf", 16)
                small_font = ImageFont.truetype("arial.ttf", 14)
            except (OSError, IOError):
                try:
                    title_font = ImageFont.load_default()
                    font = ImageFont.load_default()
                    small_font = ImageFont.load_default()
                except:
                    title_font = None
                    font = None
                    small_font = None
            
            # Draw title
            title = "Hospital Readmission Prediction"
            draw.text((20, 20), title, fill=(0, 0, 0), font=title_font)
            
            # Draw prediction details
            y_pos = 60
            line_height = 25
            
            # Probability
            prob_text = f"Readmit Probability: {prediction_result['readmit_probability_percent']}"
            draw.text((20, y_pos), prob_text, fill=(0, 0, 0), font=font)
            y_pos += line_height
            
            # Prediction
            pred_text = f"Prediction: {prediction_result['prediction']}"
            color = (255, 0, 0) if prediction_result['will_readmit'] else (0, 128, 0)
            draw.text((20, y_pos), pred_text, fill=color, font=font)
            y_pos += line_height + 10
            
            # Risk factors
            draw.text((20, y_pos), "Top Risk Factors:", fill=(0, 0, 0), font=font)
            y_pos += line_height
            
            risk_factors = prediction_result.get('risk_factors', [])
            for factor in risk_factors[:3]:
                factor_text = f"• {factor['factor']} ({factor['impact']} impact)"
                draw.text((30, y_pos), factor_text, fill=(0, 0, 0), font=small_font)
                y_pos += line_height - 5
            
            return image
            
        except Exception as e:
            logger.error(f"Error creating prediction summary image: {str(e)}")
            # Create simple error image
            error_image = Image.new('RGB', (width, height), (255, 255, 255))
            draw = ImageDraw.Draw(error_image)
            draw.text((50, height//2), "Error creating summary", fill=(255, 0, 0))
            return error_image
