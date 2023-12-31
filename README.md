# Flask App
Recognize Anything model(RAM) is an image tagging model, which can recognize any common category with high accuracy.

[Grounded Segment Anything Model(GSAM)](https://github.com/chenxwh/Grounded-Segment-Anything) combines [Grounding DINO](https://github.com/IDEA-Research/GroundingDINO) with [Segment Anything](https://github.com/facebookresearch/segment-anything)

[Scene Explain](https://scenex.jina.ai/) explains the image. Different models with different options are available.

# Environment setup, to run the app locally
- ignore this if you're using Dockerfile
- Create a .env file similar to .env.example
- Get replicate API key from [here](https://replicate.com/)
- Get scene explain API key from [here](https://scenex.jina.ai/)
- Fill in some secret key

# Run app locally
```
python run.py
```

# Run app using Docker

In the root dir(btb_ai/),  run
```
docker build -t btb_ai:version .
docker run -p 8000:5000 btb_ai:version

```
For current version, check CHANGELOG.md

# Tests

run this at the root dir
```
pytest
```

# Packaging and Distribution

pending...
