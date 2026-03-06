import replicate
import os
import urllib.request
import time
import concurrent.futures

os.environ.setdefault("REPLICATE_API_TOKEN", os.getenv("REPLICATE_API_TOKEN", ""))

ASSETS_DIR = "/Users/chinmay/Desktop/Presentation/assets"

prompts = {
    "hero-texture": {
        "prompt": "Abstract futuristic technology background with flowing luminous blue (#2ea3f2) and teal (#00C3AA) light streams on a clean bright white surface. Subtle geometric mesh pattern, soft depth of field, ultra minimal and elegant. Digital art, professional, light airy atmosphere, high quality.",
        "aspect_ratio": "16:9",
        "resolution": "1K"
    },
    "ai-network": {
        "prompt": "Abstract neural network visualization with interconnected glowing nodes in blue and teal colors connected by thin elegant lines on a bright white background. Clean modern data flow illustration, professional minimal style, soft diffused lighting, digital art, high quality.",
        "aspect_ratio": "16:9",
        "resolution": "1K"
    },
    "india-map": {
        "prompt": "Stylized geometric outline map of India composed of glowing blue circuit board traces and luminous data nodes. Bright clean white background with subtle grid pattern. Technology infrastructure visualization, modern flat design, professional, high quality.",
        "aspect_ratio": "4:3",
        "resolution": "1K"
    },
    "team-collab": {
        "prompt": "Modern bright technology office environment, diverse professional Indian team collaborating around holographic AI displays showing neural network diagrams and code. Natural sunlight flooding through floor-to-ceiling windows, warm professional atmosphere, photorealistic, cinematic lighting, high quality.",
        "aspect_ratio": "3:2",
        "resolution": "1K"
    },
    "product-boliye": {
        "prompt": "Abstract elegant visualization of an AI voice assistant. Beautiful colorful sound waves transforming into geometric chat bubbles. Blue (#2ea3f2) and teal (#00C3AA) gradient accents on clean white background. Modern minimal illustration, smooth shapes, professional digital art, high quality.",
        "aspect_ratio": "4:3",
        "resolution": "1K"
    },
    "product-septa": {
        "prompt": "Abstract elegant data analytics visualization with floating holographic charts, bar graphs and line charts in blue and teal colors. Clean white background with subtle geometric patterns. Modern minimal professional illustration, digital art, high quality.",
        "aspect_ratio": "4:3",
        "resolution": "1K"
    },
    "product-piivacy": {
        "prompt": "Abstract digital privacy and security visualization. An elegant geometric shield with flowing encrypted data streams being protected, glowing in purple and blue gradients. Clean white background, modern minimal illustration, professional digital art, high quality.",
        "aspect_ratio": "4:3",
        "resolution": "1K"
    },
    "closing-bg": {
        "prompt": "Futuristic bright panoramic view of India's technology landscape. Modern glass skyscrapers with AI data streams flowing upward into a brilliant sunrise sky. Blend of Indian architectural elements and cutting-edge tech infrastructure. Blue and teal color palette, hopeful and aspirational mood, photorealistic, cinematic, high quality.",
        "aspect_ratio": "16:9",
        "resolution": "1K"
    },
    "texture-grid": {
        "prompt": "Seamless minimal geometric grid pattern of thin blue (#2ea3f2) intersecting lines forming a subtle perspective grid on pure white background. Very clean, very subtle, professional texture pattern, flat design, high quality.",
        "aspect_ratio": "1:1",
        "resolution": "1K"
    },
    "pipeline-flow": {
        "prompt": "Abstract horizontal technology pipeline flow visualization. Seven connected glowing blue and teal geometric stages flowing from left to right with elegant arrow connections. Bright white background, clean minimal illustration, professional digital art, high quality.",
        "aspect_ratio": "16:9",
        "resolution": "1K"
    }
}

def generate_image(name, config):
    print(f"  Generating: {name}...")
    try:
        output = replicate.run(
            "google/nano-banana-2",
            input={
                "prompt": config["prompt"],
                "aspect_ratio": config.get("aspect_ratio", "16:9"),
                "resolution": config.get("resolution", "1K"),
                "output_format": "png"
            }
        )

        if output:
            url = output[0] if isinstance(output, list) else str(output)
            filepath = os.path.join(ASSETS_DIR, f"{name}.png")
            urllib.request.urlretrieve(str(url), filepath)
            size = os.path.getsize(filepath)
            print(f"  Done: {name}.png ({size/1024:.0f}KB)")
            return name, True
        else:
            print(f"  Failed: {name} — no output")
            return name, False
    except Exception as e:
        print(f"  Failed: {name} — {e}")
        return name, False

if __name__ == "__main__":
    start = time.time()
    print(f"Generating {len(prompts)} images with Google Nano Banana 2...\n")

    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {
            executor.submit(generate_image, name, config): name
            for name, config in prompts.items()
        }
        for future in concurrent.futures.as_completed(futures):
            name, success = future.result()
            results[name] = success

    elapsed = time.time() - start
    success_count = sum(1 for v in results.values() if v)
    print(f"\n{'='*50}")
    print(f"Complete: {success_count}/{len(prompts)} images in {elapsed:.0f}s")

    for name, ok in sorted(results.items()):
        status = "ok" if ok else "FAILED"
        print(f"  [{status}] {name}")
