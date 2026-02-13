# Seedance 2.0 API (ByteDance) - Unofficial Documentation & Access

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Status: Beta](https://img.shields.io/badge/Status-Beta_Access-orange)](https://github.com/seedance-api/seedance-api/issues/1)
[![Model: Seedance 2.0](https://img.shields.io/badge/Model-Seedance%202.0-blue)](https://github.com/seedance-api/seedance-api/issues/1)

> **⚠️ Notice:** The public API endpoint is currently rolling out. **[Click here to join the Priority Access List](https://github.com/seedance-api/seedance-api/issues/1)** to get notified immediately when we open global registration (ETA: < 24 hours).

---

## ⚡️ Quick Links

| Resource | Status | Action |
| :--- | :--- | :--- |
| **Get API Key** | 🟡 Waitlist | [**Request Access Here**](https://github.com/seedance-api/seedance-api/issues/1) |
| **Video Samples** | 🟢 Live | [**View Demo GIFs below**](#-video-samples) |
| **Python SDK** | 🔵 Preview | [**View Code Example**](#-python-api-preview) |

---

## 🎬 Video Samples

![seedance-2 0](https://github.com/seedance-api/seedance-api/blob/main/assets/seedance-2.0.jpg)



---

## 🐍 Python API Preview

*Use this code snippet to integrate Seedance 2.0 once your key is activated.*

```python
import requests

# Endpoint will be live at api.sedanceai.com
url = "[https://api.sedanceai.com/v2/generate](https://api.sedanceai.com/v2/generate)" 

payload = {
    "prompt": "Cinematic shot of a cybernetic tiger, 2k resolution, 60fps, hyper-realistic",
    "model": "seedance-2.0-turbo",  # Latest ByteDance model
    "aspect_ratio": "16:9",
    "api_key": "YOUR_API_KEY_HERE" # Get this from the Waitlist Issue
}

# Note: This is a preview. Actual response format may vary slightly.
# response = requests.post(url, json=payload)
# print(response.json()) 
```

## 💬 FAQ
Q: Where can I get the API Key? > A: We are limiting access to ensure stability. Please comment on Issue #1 to get on the whitelist.

Q: Does this support Dreamina features? > A: Yes, it includes the core Seedance architecture used in Dreamina.

Q: Pricing? > A: We will offer Pay-as-you-go credits. No monthly subscription required.

<div align="center">
<h3>🔔 Don't miss the launch!</h3>
<p>Subscribe to updates via GitHub Issues.</p>
</div>
