import asyncio
from pyppeteer import launch

from utils import go4screenshot

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport(
        {
            "width": 1920,
            "height": 1080,
            "deviceScaleFactor": 1,
        }
    )

    await go4screenshot(
        page,
        '/',
        'anonymous-home.jpg'
    )

    await go4screenshot(
        page,
        '/classification',
        'anonymous-classification.jpg'
    )

    await asyncio.gather(
        page.waitForSelector('a[href="/classification"]'),
        page.click(
            'a#ClassificationDropdown'
        ),
    )
    await asyncio.gather(
        page.waitForSelector('.card-flex-box'),
        page.click(
            'a[href="/classification"]'
        ),
    )
    await page.screenshot(
        {
            'path': 'anonymous-classification.jpg',  
            'quality': 60,
        }
    )

    await page.goto(
        '{}/classification/image/1'.format(DOMAIN),
        {
            'waitUntil': 'networkidle0'
        }
    )
    await page.screenshot(
        {
            'path': 'anonymous-classification-details.jpg',  
            'quality': 60,
        }
    )

    await asyncio.gather(
        page.waitForNavigation(
            {
                'waitUntil': 'networkidle0'
            }
        ),
        page.click(
            'a[href="/downloads"]'
        ),
    )
    await page.screenshot(
        {
            'path': 'anonymous-downloads.jpg',  
            'quality': 60,
        }
    )

    await browser.close()

asyncio.get_event_loop().run_until_complete(
    main()
)
