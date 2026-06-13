import os
import tkinter as tk

import allure
from allure import severity_level
from dotenv import load_dotenv
from playwright.sync_api import Browser

load_dotenv()

SCREEN_WIDTH = tk.Tk().winfo_screenwidth() if os.getenv("DISPLAY") is not None else 1920
SCREEN_HEIGHT = (
    tk.Tk().winfo_screenheight() if os.getenv("DISPLAY") is not None else 1080
)


@allure.id("SC001")
@allure.label("positive case")
@allure.feature("pay order")
@allure.tag("pay", "order")
@allure.severity(severity_level.NORMAL)
@allure.description("This is scenario for pay order")
def test_order_item(browser: Browser):
    context = browser.new_context(
        viewport={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT},
        record_video_dir="videos/",
        record_video_size={"width": SCREEN_WIDTH, "height": SCREEN_HEIGHT},
    )

    page = context.new_page()

    with allure.step("Home page"):
        page.goto(os.getenv("BASE_URL"))
        homepage_img = page.screenshot(
            full_page=True, path="screenshot/000_homepage.png"
        )
        allure.attach(
            homepage_img,
            name="home page",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Login page"):
        page.locator("#btn-login").click()
        page.locator("#input-login-username").fill("admin")
        page.locator("#input-login-password").fill("admin123")
        login_img = page.screenshot(full_page=True, path="screenshot/001_login.png")
        allure.attach(
            login_img,
            name="login page",
            attachment_type=allure.attachment_type.PNG,
        )
        page.get_by_role("button").get_by_text("Log in").nth(1).click()

    with allure.step("Select first item"):
        page.locator("a:has-text('📱 Phones')").click()
        page.get_by_title("Biru").nth(1).click()
        page.get_by_text("+ Cart").nth(1).click()
        first_item_img = page.screenshot(
            full_page=True, path="screenshot/002_first_item.png"
        )
        allure.attach(
            first_item_img,
            name="first item page",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Select second item"):
        page.locator("a:has-text('🖥️ Monitors')").click()
        page.get_by_title("Biru").nth(2).click()
        page.get_by_text("+ Cart").nth(2).click()
        second_item_img = page.screenshot(
            full_page=True, path="screenshot/003_second_item.png"
        )
        allure.attach(
            second_item_img,
            name="second item page",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Cart"):
        page.get_by_label("Open cart").click()
        page.get_by_text("Place Order →").click()
        cart_item_img = page.screenshot(
            full_page=True, path="screenshot/004_cart_item.png"
        )
        allure.attach(
            cart_item_img,
            name="cart item page",
            attachment_type=allure.attachment_type.PNG,
        )

    with allure.step("Pay Order"):
        page.locator("#order-country").select_option(value="Indonesia")
        page.locator("#order-city").select_option(value="Jakarta")
        page.locator("#order-card").fill("1234567812345678")
        page.locator("#order-month").select_option(value="08")
        page.locator("#order-year").select_option(value="2026")
        pay_order_img = page.screenshot(
            full_page=True, path="screenshot/005_pay_order.png"
        )
        allure.attach(
            pay_order_img,
            name="pay order page",
            attachment_type=allure.attachment_type.PNG,
        )
        page.get_by_text("Pay Now").click()

        page.get_by_text("Log out").click()
        logout_img = page.screenshot(full_page=True, path="screenshot/006_logout.png")
        allure.attach(
            logout_img,
            name="logout page",
            attachment_type=allure.attachment_type.PNG,
        )
