import requests
import json
import time

class SeedanceClient:
    """
    Python Client for Seedance 2.0 (Oriental Skylark) API.
    Supports Text-to-Video, Image-to-Video and Lip-Sync.
    """
    def __init__(self, api_key: str, base_url: str = "https://api.byteplus.com/v1/seedance"):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def generate_video(self, prompt, image_url=None, mode="pro"):
        """
        Trigger a video generation task using Seedance 2.0 model.
        """
        payload = {
            "model": "seedance-2.0-pro",
            "prompt": prompt,
            "image_url": image_url,
            "config": {
                "resolution": "1080p",
                "fps": 30,
                "motion_bucket_id": 127
            }
        }
        response = requests.post(f"{self.base_url}/video/generate", headers=self.headers, json=payload)
        return response.json()

    def lip_sync(self, video_id, audio_url):
        """
        Apply Seedance 2.0 Lip-Sync to an existing video.
        """
        payload = {
            "video_id": video_id,
            "audio_url": audio_url
        }
        response = requests.post(f"{self.base_url}/edit/lip_sync", headers=self.headers, json=payload)
        return response.json()

    def get_task_status(self, task_id):
        """
        Check the status of a generation task.
        """
        response = requests.get(f"{self.base_url}/task/{task_id}", headers=self.headers)
        return response.json()

# Example Usage:
# client = SeedanceClient(api_key="your_seedance_api_key_here")
# task = client.generate_video(prompt="A futuristic cyberpunk city in 4K")
# print(task)
