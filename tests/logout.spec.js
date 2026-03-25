import {test, expect} from '@playwright/test'



test('logout', async({page})=>{
    await page.goto('http://127.0.0.1:8000/')
    await page.getByRole('link', { name: 'Log In' }).click();
    await page.getByRole('textbox', { name: 'Email Address' }).click();
    await page.getByRole('textbox', { name: 'Email Address' }).fill('johncena@example.com');
    await page.getByRole('textbox', { name: 'Email Address' }).press('Tab');
    await page.getByRole('textbox', { name: 'Password' }).fill('12345678');
    await page.getByRole('button', { name: 'Enter the Guild' }).click();
    await page.getByRole('link', { name: 'Log Out' }).click();
})