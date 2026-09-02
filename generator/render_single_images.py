import asyncio
import os
import sys
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))

# Nomi delle 4 idee, nello stesso ordine delle slide dentro single_images.html
names = [
    'idea1-claudeforce',
    'idea2-vibecoding-mito',
    'idea4-esperienza-diretta',
    'idea5-rag-datapizza',
]

async def main():
    # Uso: python3 render_single_images.py <YYYY-MM-DD>
    date = sys.argv[1] if len(sys.argv) > 1 else 'YYYY-MM-DD'
    out_dir = os.path.join(HERE, '..')

    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        page = await browser.new_page(viewport={'width': 1080, 'height': 1350})
        await page.goto(f'file://{HERE}/single_images.html')
        slides = await page.query_selector_all('.slide')
        print(f'Found {len(slides)} slides')
        for i, slide in enumerate(slides):
            path = os.path.join(out_dir, f'brandstyle_{names[i]}_{date}.png')
            await slide.screenshot(path=path)
            print('saved', path)
        await browser.close()

asyncio.run(main())
