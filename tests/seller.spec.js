import {test, expect} from '@playwright/test';
import path from 'path';


test("Seller login", async({page})=>{
    const uniqueId = Date.now().toString(36);
    await page.goto('http://127.0.0.1:8000/');
    await page.getByRole('link', { name: 'Register' }).click();
    await page.getByText('✦ Artisan Seller Showcase and').click();
    await page.getByRole('textbox', { name: 'First Name' }).click();
    await page.getByRole('textbox', { name: 'First Name' }).fill(`John${uniqueId}`);
    await page.getByRole('textbox', { name: 'First Name' }).press('Tab');
    await page.getByRole('textbox', { name: 'Last Name' }).fill(`New${uniqueId}`);
    await page.getByRole('textbox', { name: 'Last Name' }).press('Tab');
    await page.getByRole('textbox', { name: 'Email Address' }).fill(`seller_${uniqueId}@example.com`);
    await page.getByRole('textbox', { name: 'Email Address' }).press('Tab');
    await page.getByRole('textbox', { name: 'Password', exact: true }).fill('12345678');
    await page.getByRole('textbox', { name: 'Confirm Password' }).click();
    await page.getByRole('textbox', { name: 'Confirm Password' }).fill('12345678');
    await page.getByRole('checkbox', { name: 'I agree to the Terms of Craft' }).check();
    await page.getByRole('button', { name: 'Join the Guild' }).click();
    await page.getByRole('link', { name: 'Create Your First Listing' }).click();
    await page.getByRole('textbox', { name: 'Title' }).click();
    await page.getByRole('textbox', { name: 'Title' }).fill('A new hand made vase');
    await page.getByRole('textbox', { name: 'Description' }).click();
    await page.getByRole('textbox', { name: 'Description' }).fill('a vase that was made by me');
    const testImage = path.join(__dirname, 'test-image.jpg');
    await page.locator('input[name="image"]').setInputFiles(testImage);
    await page.getByRole('spinbutton', { name: 'Price (optional)' }).click();
    await page.getByRole('spinbutton', { name: 'Price (optional)' }).fill('14000');
    await page.getByRole('button', { name: 'Publish Listing' }).click();
    await page.getByRole('link', { name: 'Log Out' }).click();
})
