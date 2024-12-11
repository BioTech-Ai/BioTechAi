from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the Selenium WebDriver (make sure you have the correct path for the ChromeDriver)
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

# Login to Twitter
def login(username, password):
    driver.get("https://twitter.com/login")
    time.sleep(2)

    username_field = driver.find_element_by_name("text")
    username_field.send_keys(username)
    username_field.send_keys(Keys.RETURN)
    time.sleep(2)

    password_field = driver.find_element_by_name("password")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
    time.sleep(5)

# Check for new followers and reply
def check_and_reply():
    driver.get("https://twitter.com/BioFusionAgent/followers")
    time.sleep(5)

    # Look for followers (you can adjust this to better identify new followers)
    followers_list = driver.find_elements_by_xpath("//div[@aria-label='Timeline: Followers']")

    for follower in followers_list:
        username = follower.find_element_by_xpath(".//span[@class='username']").text
        print(f"New follower detected: {username}")

        # Go to the follower's profile and reply
        driver.get(f"https://twitter.com/{username}")
        time.sleep(2)

        tweet_box = driver.find_element_by_xpath("//div[@aria-label='Tweet text']")
        tweet_box.click()
        tweet_box.send_keys(f"Hi @{username}! Welcome to the BioFusion community! Check out our latest post: https://twitter.com/BioFusionAgent/status/your_latest_tweet_id")
        tweet_box.send_keys(Keys.RETURN)

        time.sleep(3)

# Replace with your Twitter credentials
login('your_twitter_username', 'your_twitter_password')

# Run the script (this will continuously check for followers)
while True:
    check_and_reply()
    time.sleep(60)  # Wait for a minute before checking again
