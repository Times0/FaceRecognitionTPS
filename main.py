from deepface import DeepFace

result = DeepFace.find(
    img_path="data/IMG_4035.heic.jpg",
    db_path="data",
)

print(result)
