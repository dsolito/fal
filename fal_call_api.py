import fal_client

handler = fal_client.submit(
    "fal-ai/aura-flow",
    arguments={
        "prompt": "Close-up portrait of a majestic iguana with vibrant blue-green scales, piercing amber eyes, and orange spiky crest. Intricate textures and details visible on scaly skin. Wrapped in dark hood, giving regal appearance. Dramatic lighting against black background. Hyper-realistic, high-resolution image showcasing the reptile's expressive features and coloration."
    },
)

result = handler.get()
print(result)

handler = fal_client.submit(
    "fal-ai/fast-sdxl",
    arguments={
        "prompt": "photo of a rhino dressed suit and tie sitting at a table in a bar with a bar stools, award winning photography, Elke vogelsang"
    },
)

result = handler.get()
print(result)