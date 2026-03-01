from playwright.sync_api import sync_playwright

seeds = [77,78,79,80,81,82,83,84,85,86]

grand_total = 0

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    for seed in seeds:
        url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
        page.goto(url)

        # Wait for table to load
        page.wait_for_selector("table")

        # Extract all table cell values
        cells = page.query_selector_all("table td")

        numbers = []
        for cell in cells:
            text = cell.inner_text()
            try:
                number = int(text)
                numbers.append(number)
            except:
                pass

        seed_sum = sum(numbers)
        print(f"Seed {seed} sum = {seed_sum}")

        grand_total += seed_sum

    print("=================================")
    print("FINAL TOTAL:", grand_total)
    print("=================================")

    browser.close()
