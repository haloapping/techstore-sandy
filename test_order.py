import os
import tkinter as tk

from dotenv import load_dotenv
from playwright.sync_api import Browser

load_dotenv()

SCREEN_WIDTH = tk.Tk().winfo_screenwidth() if os.getenv("DISPLAY") is not None else 1920
SCREEN_HEIGHT = (
    tk.Tk().winfo_screenheight() if os.getenv("DISPLAY") is not None else 1080
)


def test_order_item(browser: Browser):
    context = browser.new_context(
        viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT},
        record_video_dir="videos/",
        record_video_size={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT},
    )

    page = context.new_page()

    page.goto(os.getenv("BASE_URL"))
    page.screenshot(full_page=True, path="screenshot/000_homepage.png")

    # login
    page.locator("#btn-login").click()
    page.locator("#input-login-username").fill("admin")
    page.locator("#input-login-password").fill("admin123")
    page.screenshot(full_page=True, path="screenshot/001_login.png")
    page.locator("button[onclick='doLogin()']").click()

    # first item
    page.locator("a:has-text('📱 Phones')").click()
    page.get_by_title("Biru").nth(1).click()
    page.get_by_text("+ Cart").nth(1).click()
    page.screenshot(full_page=True, path="screenshot/002_first_item.png")

    # second item
    page.locator("a:has-text('🖥️ Monitors')").click()
    page.get_by_title("Biru").nth(2).click()
    page.get_by_text("+ Cart").nth(2).click()
    page.screenshot(full_page=True, path="screenshot/003_second_item.png")

    # cart
    page.get_by_label("Open cart").click()
    page.get_by_text("Place Order →").click()
    page.screenshot(full_page=True, path="screenshot/004_cart_item.png")

    page.locator("#order-country").select_option(value="Indonesia")
    page.locator("#order-city").select_option(value="Jakarta")
    page.locator("#order-card").fill("1234567812345678")
    page.locator("#order-month").select_option(value="08")
    page.locator("#order-year").select_option(value="2026")
    page.screenshot(full_page=True, path="screenshot/005_pay_order.png")
    page.get_by_text("Pay Now").click()

    page.get_by_text("Log out").click()
    page.screenshot(full_page=True, path="screenshot/006_logout.png")
