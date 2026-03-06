import replicate
import os
import urllib.request
import time
import concurrent.futures

os.environ.setdefault("REPLICATE_API_TOKEN", os.getenv("REPLICATE_API_TOKEN", ""))

ASSETS_DIR = "/Users/chinmay/Desktop/Presentation/assets"

prompts = {
    "hero-person": {
        "prompt": "Professional confident Indian male tech CEO in his 40s, wearing a sharp navy blazer over a crisp white shirt, standing with arms crossed, warm smile, shot from the waist up. Clean bright white studio background. Professional corporate headshot style, soft natural lighting, shallow depth of field, photorealistic, high quality.",
        "aspect_ratio": "3:4",
        "resolution": "1K"
    },
    "hero-woman": {
        "prompt": "Professional confident Indian female AI researcher in her 30s, wearing a modern teal blouse, looking directly at camera with a warm engaging smile, holding a tablet. Clean bright white studio background. Corporate headshot style, soft diffused studio lighting, photorealistic, high quality.",
        "aspect_ratio": "3:4",
        "resolution": "1K"
    },
    "team-group": {
        "prompt": "Four diverse Indian tech professionals standing together in a modern bright office, two men and two women, wearing smart casual business attire, smiling confidently at camera. Large windows with natural light behind them. Professional team photo, photorealistic, warm tones, high quality.",
        "aspect_ratio": "16:9",
        "resolution": "1K"
    },
    "person-presenting": {
        "prompt": "Young Indian male software engineer in a grey henley shirt, pointing at a large screen showing AI neural network diagrams and code, looking back at camera with an enthusiastic smile. Modern bright tech office setting. Candid professional photo, natural lighting, photorealistic, high quality.",
        "aspect_ratio": "4:3",
        "resolution": "1K"
    },
    "person-data": {
        "prompt": "Indian female data scientist in her late 20s, wearing glasses and a white button-down shirt, looking at floating holographic data visualizations and charts. Modern bright office with blue accent lighting. Professional tech photography, cinematic quality, photorealistic.",
        "aspect_ratio": "4:3",
        "resolution": "1K"
    },
    "cover-abstract": {
        "prompt": "Stunning abstract 3D render of interconnected luminous spheres and flowing light ribbons in blue (#2ea3f2) and teal (#00C3AA) colors, floating in a vast bright white space. Dramatic depth, ultra clean composition, premium tech aesthetic. Cinema 4D quality, 8K render, volumetric lighting, glass and chrome materials.",
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
    print(f"Generating {len(prompts)} people/cover images...\n")
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(generate_image, n, c): n for n, c in prompts.items()}
        for f in concurrent.futures.as_completed(futures):
            name, ok = f.result()
            results[name] = ok
    elapsed = time.time() - start
    ok_count = sum(1 for v in results.values() if v)
    print(f"\nComplete: {ok_count}/{len(prompts)} in {elapsed:.0f}s")
    for n, ok in sorted(results.items()):
        print(f"  [{'ok' if ok else 'FAIL'}] {n}")
