# RAM with GSAM Flask App
Recognize Anything model(RAM) is an image tagging model, which can recognize any common category with high accuracy.

[Grounded Segment Anything Model(GSAM)](https://github.com/chenxwh/Grounded-Segment-Anything) combines [Grounding DINO](https://github.com/IDEA-Research/GroundingDINO) with [Segment Anything](https://github.com/facebookresearch/segment-anything)

# Environment setup
- Create a .env file similar to .env.example
- Get replicate API key from [here](https://replicate.com/)
- Fill in some secret key 


# RUN

In the root dir(BTB_AI/),  run
```
docker build -t btb_ai:v0.0.1 .
docker run -p 8000:5000 btb_ai:v0.0.1

```

# Tests

run this at the root dir
```
pytest
```

# Packaging

pending
