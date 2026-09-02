import asyncio
import os
import sys
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))

async def main():
    # Uso: python3 render_pdf.py <YYYY-MM-DD>
    # Rilegge generator/report.html (generato da generate_html.py) e produce
    # il PDF finale nella cartella superiore della repo.
    date = sys.argv[1] if len(sys.argv) > 1 else 'YYYY-MM-DD'
    out_path = os.path.join(HERE, '..', f'PED_Digitiamo_{date}.pdf')

    async with async_playwright() as p:
        browser = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium')
        page = await browser.new_page()
        await page.goto(f'file://{HERE}/report.html')
        await page.wait_for_timeout(500)
        await page.pdf(
            path=out_path,
            width='794px',
            height='1123px',
            print_background=True,
            margin={'top': '0', 'bottom': '0', 'left': '0', 'right': '0'},
        )
        await browser.close()
    print('saved', out_path)

asyncio.run(main())
