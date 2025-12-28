from playwright.sync_api import sync_playwright
import pandas as pd
import time
from datetime import datetime

SIGNUP_URL = "https://signup.live.com/signup"


# ==============================
# Ask for proxy
# ==============================
def ask_for_proxy():
    print("\nProxy configuration:")
    print("1 - Use proxy")
    print("2 - No proxy")

    choice = input("Enter choice (1 or 2): ").strip()
    if choice != "1":
        return None

    server = input("Proxy server (http://IP:PORT): ").strip()
    if not server:
        return None

    username = input("Proxy username (optional): ").strip()
    password = input("Proxy password (optional): ").strip()

    proxy = {"server": server}
    if username and password:
        proxy["username"] = username
        proxy["password"] = password

    return proxy


# ==============================
# Ask how to handle proxy next run
# ==============================
def ask_proxy_next_run(current_proxy):
    print("\nProxy for next run:")
    print("1 - Keep same proxy")
    print("2 - Use a new proxy")
    print("3 - No proxy")

    choice = input("Enter choice (1, 2, or 3): ").strip()

    if choice == "1":
        return current_proxy
    elif choice == "2":
        return ask_for_proxy()
    elif choice == "3":
        return None
    else:
        print("Invalid choice. Keeping same proxy.")
        return current_proxy


# ==============================
# Ask for email input
# ==============================
def get_emails():
    print("\nChoose input method:")
    print("1 - Paste emails manually")
    print("2 - Load from CSV file")

    choice = input("Enter choice (1 or 2): ").strip()
    emails = []

    if choice == "1":
        print("\nPaste emails (one per line).")
        print("Press ENTER twice when done:\n")
        while True:
            line = input().strip()
            if not line:
                break
            emails.append(line)

    elif choice == "2":
        path = input("\nEnter path to CSV file: ").strip()
        df = pd.read_csv(path)
        if "email" not in df.columns:
            raise ValueError("CSV must contain a column named 'email'")
        emails = df["email"].astype(str).tolist()

    else:
        raise ValueError("Invalid choice")

    return emails


# ==============================
# One full run
# ==============================
def run_checker(proxy):
    emails = get_emails()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_file = f"results-{timestamp}.csv"
    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=False,
            proxy=proxy if proxy else None
        )

        context = browser.new_context()

        # Speed optimization
        context.route(
            "**/*",
            lambda route: route.abort()
            if route.request.resource_type in ["image", "font", "media"]
            else route.continue_()
        )

        page = context.new_page()
        page.goto(SIGNUP_URL, timeout=60000)

        for email in emails:
            print(f"\nChecking {email} ...")

            page.wait_for_selector('input[type="email"]', timeout=20000)
            email_input = page.locator('input[type="email"]')

            email_input.fill("")
            email_input.type(email, delay=40)
            page.keyboard.press("Tab")
            time.sleep(1)

            page.locator('button[data-testid="primaryButton"]').click()
            time.sleep(2)

            still_on_email_page = page.locator('input[type="email"]').count() > 0

            if still_on_email_page:
                status = "TAKEN"
                print(" → TAKEN")
            else:
                status = "AVAILABLE"
                print(" → AVAILABLE")

            results.append({
                "email": email,
                "status": status
            })

            page.goto(SIGNUP_URL)
            time.sleep(2)

        browser.close()

    pd.DataFrame(results).to_csv(output_file, index=False)
    print(f"\nResults saved to {output_file}")


# ==============================
# Main loop
# ==============================
def main():
    print("=== Microsoft Email Availability Checker ===")

    # First run: ask for proxy
    current_proxy = ask_for_proxy()

    while True:
        run_checker(current_proxy)

        print("\nDo you want to run another check?")
        print("1 - Yes")
        print("2 - No")

        choice = input("Enter choice (1 or 2): ").strip()
        if choice != "1":
            print("\nExiting. Goodbye 👋")
            break

        # Decide proxy behavior for next run
        current_proxy = ask_proxy_next_run(current_proxy)


if __name__ == "__main__":
    main()
