import {test,expect} from '@playwright/test';


test('registner new user', async ({page}) => {
    await page.goto('http://localhost:8000/');
    await page.getByRole('link', { name: 'Register' }).click();
    await page.getByRole('textbox', { name: 'First Name' }).click();
    await page.getByRole('textbox', { name: 'First Name' }).fill('John');
    await page.getByRole('textbox', { name: 'First Name' }).press('Tab');
    await page.getByRole('textbox', { name: 'First Name' }).click();
    await page.getByRole('textbox', { name: 'First Name' }).fill('John');
    await page.getByRole('textbox', { name: 'First Name' }).press('Tab');
    await page.getByRole('textbox', { name: 'Last Name' }).fill('Cena');
    await page.getByRole('textbox', { name: 'Email Address' }).click();
    await page.getByRole('textbox', { name: 'Email Address' }).fill('johncena@example.com');
    await page.getByRole('textbox', { name: 'Email Address' }).press('Tab');
    await page.getByRole('textbox', { name: 'Password', exact: true }).fill('12345678');
    await page.getByRole('textbox', { name: 'Password', exact: true }).press('Tab');
    await page.getByRole('textbox', { name: 'Confirm Password' }).fill('12345678');
    await page.getByRole('checkbox', { name: 'I agree to the Terms of Craft' }).check();
    await page.getByRole('button', { name: 'Join the Guild' }).click();
});


