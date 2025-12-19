# JavaScript Rendering

Modern websites often rely on JavaScript to dynamically generate or modify page
content after the initial HTML is loaded.

## Server-Side Rendering (SSR)
- HTML is fully generated on the server
- Content is visible in page source
- Easily accessible to basic scrapers

## Client-Side Rendering (CSR)
- HTML contains placeholders
- JavaScript fetches and injects content
- Data appears only after execution

## Impact on Scraping
- Static scrapers cannot access JS-rendered content
- Browser automation tools may be required

## Common Indicators
- Empty containers in HTML
- Content appears after scrolling or clicking
- Network calls made via JavaScript APIs

## Trade-offs
JS rendering increases interactivity but complicates automation and data access.
