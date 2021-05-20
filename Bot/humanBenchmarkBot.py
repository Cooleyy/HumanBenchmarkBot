from webbot import Browser
import tests
import time

def main():
    skipTests = ["sequence_memory", "chimp_test", "aim_trainer", "typing", "verbal_memory"]

    driver = Browser()
    dashURL = "https://humanbenchmark.com/dashboard"
    driver.implicitly_wait(0.05)
    driver.go_to(dashURL)
    driver.click('Accept all')

    for test in tests.get_tests():
        if test.__name__ in skipTests:
            print("Skipping:", test.__name__)
            continue

        print("Completing:", test.__name__)

        if driver.get_current_url() != dashURL:
            print("At incorrect page:", driver.get_current_url())
            driver.go_to(dashURL)

        time.sleep(1)
        test(driver)
        
        time.sleep(0.1)
        driver.click('Save score')
        driver.implicitly_wait(0.05)
        driver.go_to(dashURL)

    #Keep browser open until user exit
    _ = input("Press enter to exit:")

if __name__ == '__main__':
    main()