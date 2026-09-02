import asyncio
import os
import sys
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))

async def main():
    # Uso: python3 render_carousel.py <slug> <YYYY-MM-DD>
    # Rilegge generator/carousel_slides.html e salva le slide PNG nella
    # cartella di output (default: la cartella superiore della repo).
    slug = sys.argv[1] if len(sys.argv) > 1 else 'ai-act'
    date = sys.argv[2] if len(sys.argv) > 2 else 'YYYY-MM-DD'
    out_dir = os.path.join(HERE, '..')

    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        page = await browser.new_page(viewport={'width': 1080, 'height': 1350})
        await page.goto(f'file://{HERE}/carousel_slides.html')
        slides = await page.query_selector_all('.slide')
        print(f'Found {len(slides)} slides')
        for i, slide in enumerate(slides, start=1):
            path = os.path.join(out_dir, f'carosello_{slug}_{date}_slide{i}.png')
            await slide.screenshot(path=path)
            print('saved', path)
        await browser.close()

asyncio.run(main())
