(async () => {
    require('dotenv').config();
    const puppeteer = require('puppeteer');
    var browser = await puppeteer.launch({headless: false});
    var page = await browser.newPage();
    await page.setViewport({width: 1366, height: 768});
    await page.goto('https://www.linkedin.com/login', {waitUntil: 'networkidle2'});
    await page.click('#username');
    await page.keyboard.type(process.env.LINKEDIN_USERNAME || '');
    await page.click('#password');
    await page.keyboard.type(process.env.LINKEDIN_PASSWORD || '');
    await page.click('[type="submit"]');
    await page.waitForNavigation();
    await page.screenshot({path: './linkedin.jpg'});
    await browser.close();
    console.log('Saved to linkedin.jpg');
})();