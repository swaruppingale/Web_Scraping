# Web Scraping Project 

## What is Web Scraping?

Web scraping is **extracting data from websites**
by requesting web pages, parsing their content, and converting unstructured
information into structured formats such as CSV, JSON, or databases.

Web scraping is commonly used when:
- A website does not provide a public API
- Data is available only through web pages
- Information is spread across multiple sources

---

## Why Web Scraping in Cybersecurity?

### The Problem

While vulnerability databases provide CVE metadata, **exploit activity** is
frequently described only in natural-language statements such as:
- “This vulnerability is actively exploited in the wild”
- “Observed exploitation in real-world attacks”

To extract and monitor this intelligence in a structured way, **web scraping is
required**.

### Real-World Scenarios
- Threat intelligence aggregation
- Patch prioritization based on active exploitation
- SOC and incident-response enrichment
- Vulnerability risk assessment
- Security research and monitoring

---

## Static vs Dynamic Scraping

### Static Scraping (requests + BeautifulSoup)

**What**  
The server sends the complete HTML content in the initial HTTP response.

**When to use**  
- Vendor security advisories
- Research blogs
- Traditional CMS-based websites  
(Data is visible in “View Page Source”)

**How it works**
1. Send an HTTP GET request
2. Receive HTML response
3. Parse HTML using BeautifulSoup
4. Extract text and indicators (CVE IDs, exploit keywords)

This project primarily uses **static scraping**, as most security blogs are
server-rendered.

---

### Dynamic Scraping (Playwright / Selenium)

**What**  
Content is loaded or modified by JavaScript after page load.

**When to use**
- Single-Page Applications (React, Vue, Angular)
- Infinite scrolling
- Content loaded via AJAX / fetch calls

**How it works**
1. Launch a headless browser
2. Execute JavaScript
3. Wait for dynamic content to render
4. Extract data from rendered DOM

---

## Logic


### Detection Approach
- Extract full article text
- Search for exploitation indicators such as:
  - “exploited in the wild”
  - “actively exploited”
  - “observed exploitation”
  - “zero-day exploited”

Keyword-based detection provides transparency and auditability.

---

## Security Challenges in Web Scraping

### CAPTCHA
**Purpose**: Distinguish humans from bots  
**Handling**:
- Avoid triggering via rate limiting
- No CAPTCHA solving or bypassing

---

### IP Blocking
**Why it happens**:
- High request volume
- Suspicious traffic patterns

**Prevention**:
- Request throttling
- Realistic headers

---

### Other Protections
- Session cookies
- Bot-detection JavaScript
- Honeypot links

---

## Installation

Install the required dependencies using pip:

```bash
pip install -r requirements.txt

Usage

Run the scraping pipeline using:

python scripts/run_pipeline.py

Output

The pipeline generates a structured CSV file containing:

Source

CVE references

Exploit status indicators


Project Structure

├── src/                    # Core scraping and analysis logic
├── docs/                   # Conceptual documentation
├── data/                   # Output files and snapshots
├── scripts/                # Pipeline execution
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation


