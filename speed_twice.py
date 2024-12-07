from pydub import AudioSegment
import os
from math import ceil

def process_audio(input_folder, speed_factor, segment_length_mins=15):
    """
    Recursively process all MP3 files in the specified folder and its subfolders.
    Split files longer than segment_length_mins into separate files and change speed.
    
    Args:
        input_folder (str): Path to folder containing MP3 files
        speed_factor (float): Speed multiplier (e.g., 1.5 for 50% faster)
        segment_length_mins (int): Maximum length of each segment in minutes
    """
    # Convert minutes to milliseconds
    segment_length_ms = segment_length_mins * 60 * 1000
    output_base = os.path.join(input_folder, "processed_audio")
    os.makedirs(output_base, exist_ok=True)
    
    def split_and_speed_change(audio, original_filename, output_path):
        """Split audio into segments and change speed for each segment"""
        duration = len(audio)
        num_segments = ceil(duration / segment_length_ms)
        
        for i in range(num_segments):
            start_time = i * segment_length_ms
            end_time = min((i + 1) * segment_length_ms, duration)
            
            # Extract segment
            segment = audio[start_time:end_time]
            
            # Change speed
            speed_adjusted = segment._spawn(segment.raw_data, overrides={
                "frame_rate": int(segment.frame_rate * speed_factor)
            })
            
            # Generate output filename
            if num_segments > 1:
                segment_filename = f"speed_{speed_factor}x_part{i+1:03d}_{original_filename}"
            else:
                segment_filename = f"speed_{speed_factor}x_{original_filename}"
                
            output_file = os.path.join(output_path, segment_filename)
            
            # Export the modified audio
            speed_adjusted.export(output_file, format="mp3")
            print(f"Saved: {output_file}")

    def process_folder(current_folder):
        # Create corresponding output subfolder structure
        rel_path = os.path.relpath(current_folder, input_folder)
        current_output_folder = os.path.join(output_base, rel_path)
        os.makedirs(current_output_folder, exist_ok=True)
        
        # Process all items in current folder
        for item in os.listdir(current_folder):
            full_path = os.path.join(current_folder, item)
            
            # If it's a directory, process it recursively
            if os.path.isdir(full_path) and not item == "processed_audio":
                process_folder(full_path)
            
            # If it's an MP3 file, process it
            elif item.lower().endswith('.mp3'):
                try:
                    print(f"\nProcessing: {full_path}")
                    
                    # Load the audio file
                    audio = AudioSegment.from_mp3(full_path)
                    
                    # Process the audio
                    split_and_speed_change(audio, item, current_output_folder)
                    
                except Exception as e:
                    print(f"Error processing {full_path}: {str(e)}")
                    continue
    
    # Start processing from the root folder
    process_folder(input_folder)

if __name__ == "__main__":
    # Example usage
    folder_path = input("Enter the folder path containing MP3 files: ")
    speed = float(input("Enter speed factor (e.g., 1.5 for 50% faster, 0.5 for 50% slower): "))
    segment_mins = int(input("Enter maximum segment length in minutes (default 15): ") or "15")
    
    process_audio(folder_path, speed, segment_mins)
    print("\nProcessing complete!")