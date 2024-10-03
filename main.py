from deepface import DeepFace

result = DeepFace.verify(
  img1_path = "data/IMG_4139.jpg",
  img2_path = "data/IMG_4139.jpg",
)

print(result)