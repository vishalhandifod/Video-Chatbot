from moviepy.editor import VideoFileClip
import os

def convert_video_to_audio(video_path, output_dir='static/audio'):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate the audio file path
    audio_filename = os.path.splitext(os.path.basename(video_path))[0] + '.mp3'
    audio_path = os.path.join(output_dir, audio_filename)
    
    print(f"Audio file will be saved to: {audio_path}")
    
    try:
        # Load video clip and extract the audio
        video_clip = VideoFileClip(video_path)
        audio_clip = video_clip.audio
        
       
        temp_audio_path = os.path.join(output_dir, "temp_audio.mp3")
        audio_clip.write_audiofile(temp_audio_path)

        # Move the temporary file to the desired path
        if os.path.exists(temp_audio_path):
            os.rename(temp_audio_path, audio_path)
        
        print(f"Audio conversion successful: {audio_path}")
        
    except Exception as e:
        print(f"Error during video-to-audio conversion: {e}")
        
    finally:
        
        audio_clip.close()
        video_clip.close()
    
    return audio_path
